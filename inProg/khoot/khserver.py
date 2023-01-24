# khserver !
#=#
# Imports
import socket, threading, json
import time, random, os, sys, select, base64

#=#
# Constants
HEADER = 64
SERVER = "192.168.86.21" # VIRGIN379 on aarushmac
try: PORT = int(sys.argv[1]) if sys.argv[1] else 14014
except: PORT = 14014
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "%DISCONNECT"
host = None
contactList = []
gameState = "NotRunning"

#=#
# Methods and Classes


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
    
    while gameState == "asking":
        msg_length = sock.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            t1 = time.perf_counter()
            msg_length = int(msg_length)
            
            msg = sock.recv(msg_length).decode(FORMAT)
            
            if not msg.isnumeric():
                return getAnsFrom(conn)
            
            conn.answer = Answer(msg, time.perf_counter()-t0)
            
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
    gameManager()
    

def readyState(post=True, DEBUG=True):
    global host
    sock = host.sock
    if host.name: name = host.name
    else: name = host.addr
    sock.send("%READYUP?".encode(FORMAT))
    prevSent=0
    
    while True:
        if len(contactList) > prevSent:
            host.sock.send("%PLAYRCNT" + str(len(contactList)))
            prevSent = len(contactList)
        
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
            
            return True if msg == "&STRTGAME" else False
        
        
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
    global host
    while True:
        fm = sock.recv(9).decode(FORMAT)
        # $ recv 9 because first message is either hostjoin or playjoin
        
        if fm:
            if fm == "&HOSTJOIN":
                conn = Connection(sock, addr, True)
                host = conn
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
    if type(conn.answer) == Answer:
        if str(conn.answer.answer) == str(answer):
            # use time algorithm/calculation
            conn.points += 100
    conn.sock.send((f"%POINTCHK:{conn.points}").encode(FORMAT))
    conn.answer = 0 
    

def gameManager():
    """Starts and manages a kahoot game."""
    global gameState
    while True:
        if readyState():
            
            print("[HOST] Game starting! ")
            gameState = "Running!"
            
            pointboard = {}

            with open(os.path.join(os.path.dirname(__file__), "questions.txt"), "r") as file: 
                lines = file.readlines()
            # read all questions

            random.shuffle(lines) #shuffle lines

            for line in lines:
                gameState = "asking"
                question, ans = line[:-2], line[-2]
                
                host.sock.send((f"%QUESTION:{question}").encode(FORMAT))
                print((f"[QUESTION] {question}"))
                
                contactThreads = []
                for contact in contactList:
                    contact.answer = 0
                    contactThreads.append(threading.Thread(target = lambda: getAnsFrom(contact)))
                    contactThreads[-1].start()
                
                while getMsgFrom(host, "%QSTNFNSH") != "&NEXTQSTN": continue
                
                gameState = "returning"
                
                
                
                for contact in contactList:
                    answerEvaluate(contact, ans)
                    pointboard[contact.name] = contact.points
                    
                serialPoints = json.dumps( sorted(pointboard.items(), key=lambda x:x[1], reverse=True) )
                _ = getMsgFrom(host, (f"%LDRBOARD:{serialPoints}"))
                

            pointboard = sorted(pointboard.items(), key=lambda x:x[1], reverse=True)
            for n in range(len(pointboard)):
                for contact in contactList:
                    if pointboard[n][0] == contact.name:
                        contact.sock.send(("%RANKINGL:"+str(n+1)).encode(FORMAT))
            _ = getMsgFrom(host, ("%GAMEOVER"))
            
    

    
    

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

except: 
    for conn in list(host)+contactList:
        conn.sock.close()

#=#
# Notes
"""
# &HOSTJOIN : sent from client to indicate that the connection is from the host,
    only sent once at start of connection
# &PLAYJOIN : sent from client to indicate that the connection is from a player,
    only sent once at start of connection
# &STRTGAME : sent from host character to indicate the start of the game
# %NAMEREQR : sent from server to assign nickname to computer
# %READYUP? : sent from server to ask if the game can start
# %QUESTION : sent from server to host only, along with question for printing
# %ANSWRQST : sent from server to players only, to ask them for their answer
# %POINTCHK : sent from server to players, to give them a refresh of their score
# %QSTNFNSH : sent from server to host to request skip button input
# &NEXTQSTN : sent from host to server to go to next question
# %LDRBOARD : sent from server to host, pickled leaderboard
# %GAMEOVER : sent from server to host, notifies the game is over
# %RANKINGL : sent from server to player, notifies their rank in the game
"""
