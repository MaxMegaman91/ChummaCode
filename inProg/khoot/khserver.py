# khserver !
#=#
# Imports
import socket, threading
import time, random, os




class Connection():
    def __init__(self, sock, addr, isHost=False, *kwargs):
        """The connection object with attributes all for conformed data structures.

        Args:
            sock (socket.socket): used to recv and send data to/from the player/host
            addr ((IP, PORT)): used to differentiate users from each other (ID)
            isHost (bool, optional): True if the connection is from a host. Defaults to False.
            
        Also includes:
        
        Extras for Kwargs,
        Points for Kahoot Score,
        Name for Reference Nickname,
        Answer for Answer Object.
        """
        
        self.sock = sock
        self.addr = addr
        self.isHost = isHost
        self.extras = kwargs
        self.points = 0
        self.name = ""
        self.answer = 0
    
    def __repr__(self):
        return "Connection()"
    
    def __str__(self):
        return self.name
    

class Answer():
    def __init__(self, answer, time, *kwargs):
        """Answer object to evaluate and store answer data.

        Args:
            answer (Integer): Answer option between 1-4.
            time (Integer): Seconds passed from question to answer.
        
        Also has: Extras for kwargs.
        """
        self.answer = answer
        self.answertime = time
        self.extras = kwargs
    
    def __repr__(self):
        return "Answer()"
    
    def __str__(self):
        return f"{str(self.answer)} in {str(self.answertime)} seconds." 
    
    
def getMsgFrom(conn:Connection, requestMSG="%UNKREQST", post=True, DEBUG=True):
    """Uses a connection object to send {requestMSG} and receive message from user
    
    Args:
        conn (Connection): The connection object, must have a socket and addr for communication purposes
        requestMSG (str, optional): The request sent, understanded by khplayer or khhost, starting with & or %. Defaults to "%UNKREQST".
        post (bool, optional): Post the messages on server as chat. Defaults to True.
        DEBUG (bool, optional): Defaults to True.

    Returns:
        String: Message Received
    """
    
    sock = conn.sock
    if conn.name: name = conn.name
    else: name = conn.addr
    sock.send(requestMSG.encode(FORMAT))
    
    while True:
        msg_length = sock.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            
            msg = sock.recv(msg_length).decode(FORMAT)
            
            if post and msg != "": #indexerror if msg is 0 in length
                if not msg[0] in "&%": print(f"[{name}] {msg}")
            
            elif DEBUG:
                print(f"[{name}] {msg}")
            
            if msg == DISCONNECT_MESSAGE:
                print(f"[Disconnection] {addr} is disconnecting! ")
                sock.close()
                del conn
            
            return msg
            

    
def getAnsFrom(conn:Connection, DEBUG = True):
    """Similar to getMsgFrom, using a connection object to communicate with a player to request the answer {%ANSWRQST}
    and return an answer object to Connection.answer for evaluation, using time and answer option.

    Args:
        conn (Connection): The connection object, must have a socket and addr for communication purposes
        DEBUG (bool, optional): Defaults to True.

    Returns:
        None
    """
    requestMSG = "%ANSWRQST"
    
    sock = conn.sock
    if conn.name: name = conn.name
    else: name = conn.addr
    sock.send(requestMSG.encode(FORMAT))
    t0 = time.perf_counter()
    
    while time.perf_counter()-t0 <= 30:
        msg_length = sock.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            t1 = time.perf_counter()
            msg_length = int(msg_length)
            
            msg = sock.recv(msg_length).decode(FORMAT)
            
            if not msg.isnumeric():
                return getAnsFrom(conn)
            
            msg = int(msg)
            conn.answer = Answer(msg, t0-t1)
            
            if DEBUG:
                print(f"[{name}] {msg}")
            
            if msg == DISCONNECT_MESSAGE:
                print(f"[Disconnection] {addr} is disconnecting! ")
                sock.close()
                del conn
            
            return

def asHost(conn:Connection):
    """Inner function to execute certain methods to set up a host.

    Args:
        conn (Connection): The connection object, must have a socket and addr for communication purposes
    """
    print(f"[New Connection] {conn.addr} connected as HOST! ")
    sock = conn.sock
    
    
    conn.name = getMsgFrom(conn, "%NAMEREQR")
    
    print(f"[RENAME] {conn.addr} renamed and hereby addressed as {conn.name}.")
    
    while True:
        if getMsgFrom(conn,"%READYUP?") == "&STRTGAME":
            global gameState
            print("[HOST] Game starting! ")
            gameState = "Running!"
            gameManager()
        
        
def asPlay(conn:Connection):
    """Inner function to execute certain methods to set up a host.

    Args:
        conn (Connection): The connection object, must have a socket and addr for communication purposes
    """
    print(f"[New Connection] {conn.addr} connected as PLAYER! ")
    sock = conn.sock
    
    conn.name = getMsgFrom(conn, "%NAMEREQR")
    
    print(f"[RENAME] {conn.addr} renamed and hereby addressed as {conn.name}.")
    
    while gameState:
        pass
    

    
def establishConn(sock, addr):
    """On acceptance of connection to server, split hosts and players and set them up. 

    Args:
        sock (socket.socket): The socket to send and recv information on
        addr ((IP, PORT)): IP and port information to address the computer.

    Returns:
        None
    """
    while True:
        fm = sock.recv(9).decode(FORMAT)
        # $ recv 9 because first message is either hostjoin or playjoin
        
        if fm:
            if fm == "&HOSTJOIN":
                conn = Connection(sock, addr, True)
                hostList.append(conn)
                return asHost(conn)
            elif fm == "&PLAYJOIN":
                conn = Connection(sock, addr)
                contactList.append(conn)
                return asPlay(conn)
            else: 
                sock.close()

def answerEvaluate(conn:Connection, answer):
    """Evaluates answer submitted with correct answer. Uses time from Answer object to add speed bonus.

    Args:
        conn (Connection): The connection object, must have a socket and addr for communication purposes
        answer (Integer): Correct answer option from 1-4
    """
    if conn.answer.answer == answer: # answer as \n because last character of a line is newline :(
        # use time algorithm/calculation
        conn.points += 10
    conn.sock.send((f"%POINTCHK:{conn.points}").encode(FORMAT))
    conn.answer = 0 
    


def gameManager():
    """Starts and manages a kahoot game."""
    
    with open(os.path.join(os.path.dirname(__file__), "questions.txt"), "r") as file: 
        lines = file.readlines()
    
    line = random.choice(lines)
    question, ans = line[:-2], line[-1]
    
    for host in hostList:
        try: 
            host.sock.send((f"%QUESTION:{question}").encode(FORMAT))
            print((f"[QUESTION] {question}"))
        except: pass
    
    contactThreads = []
    for contact in contactList:
        contact.answer = 0
        contactThreads.append(threading.Thread(target = lambda: getAnsFrom(contact)))
        contactThreads[-1].start()
    
    time.sleep(30)
    
    # contact Threads stop all
    
    # send hosts the point data and leaderboard, as well as # of answered peple
    
    for contact in contactList:
        answerEvaluate(contact, ans)
    
    
    
        
    
    
    
    
    #eval answers 
    

    
    
#=#
# Constants
HEADER = 64
SERVER = "192.168.86.21" # VIRGIN379 on aarushmac
PORT = 14014
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "%DISCONNECT"
hostList = []
contactList = []
gameState = "NotRunning"

#=#
# Init

print("[Server] Server starting up!")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

try:
    print(f"[Server] Server listening on {ADDR}]!")
    
    while True:
        server.listen()
        
        sock, addr = server.accept()
        
        threading.Thread(target=establishConn, args=(sock, addr)).start()

except: exit()
"""
# &HOSTJOIN : sent from client to indicate that the connection is from the host,
    only sent once at start of connection
# &PLAYJOIN : sent from client to indicate that the connection is from a player,
    only sent once at start of connection
# &STRTGAME : sent from host character to indicate the start of the game
# %NAMEREQR : sent from server to assign nickname to computer
# %READYUP? : sent from server to ask if the game can start
# %QUESTION : sent from server to host only, to show question on host screen
# %ANSWRQST : sent from server to players only, to ask them for their answer
# %POINTCHK : sent from server to players, to give them a refresh of their score
"""
