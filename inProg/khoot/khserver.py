# khserver !
#=#
# Imports
import socket, threading
import time, random, os

class Connection():
    def __init__(self, sock, addr, isHost=False, *args):
        self.sock = sock
        self.addr = addr
        self.isHost = isHost
        self.extras = args
        self.name = ""
        self.answer = None
    
    def __repr__(self):
        return "Connection()"
    
    def __str__(self):
        return self.name
    
def getMsgFrom(conn, requestMSG="%UNKREQST", post=True, DEBUG=True):
    sock = conn.sock
    if conn.name: name = conn.name
    else: name = conn.addr
    sock.send(requestMSG.encode(FORMAT))
    
    while True:
        msg_length = sock.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            
            msg = sock.recv(msg_length).decode(FORMAT)
            
            if post and msg[0] not in "&%": #indexerror if msg is 0 in length
                print(f"[{addr}] {msg}")
            
            elif DEBUG:
                print(f"[{addr}] {msg}")
            
            if msg == DISCONNECT_MESSAGE:
                print(f"[Disconnection] {addr} is disconnecting! ")
                sock.close()
                del conn
            
            return msg
            
            

def asHost(conn:Connection):
    print(f"[New Connection] {conn.addr} connected as HOST! ")
    sock = conn.sock
    
    
    conn.name = getMsgFrom(conn, "%NAMEREQR")
    
    print(f"[RENAME] {conn.addr} renamed and hereby addressed as {conn.name}.")
    
    while True:
        if getMsgFrom(conn,"%READYUP?") == "&STRTGAME":
            global gameState
            print("[HOST] Game starting! ")
            gameState = "Running!"
            gameManager(contactList)
        
        
def asPlay(conn:Connection):
    print(f"[New Connection] {conn.addr} connected as PLAYER! ")
    sock = conn.sock
    
    conn.name = getMsgFrom(conn, "%NAMEREQR")
    
    print(f"[RENAME] {conn.addr} renamed and hereby addressed as {conn.name}.")
    
    while gameState == "NotRunning":
        pass
    
    
    
    
    
    
def establishConn(sock, addr):
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


def gameManager(contactList):
    with open(os.path.join(os.path.dirname(__file__), "questions.txt"), "r") as file:
        lines = file.readlines()
    
    question = random.choice(lines)
    
    for contact in contactList:
        contact.sock.send(("%REQUESTS").encode(FORMAT))
    
    for host in hostList:
        host.sock.send((f"%QUESTION:{question}").encode(FORMAT))
    
    #recv answers
    
        
    
    
#=#
# Constants
HEADER = 64
SERVER = "192.168.2.112" # VIRGIN379 on aarushmac
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
# 
"""