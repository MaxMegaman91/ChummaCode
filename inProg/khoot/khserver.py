# khserver !
#=#
# Imports
import socket, threading
import time, random

class Connection():
    def __init__(self, conn, addr, isHost=False, *args):
        self.conn = conn
        self.addr = addr
        self.isHost = isHost
        self.extras = args
        # self.name = ""
    
    def __repr__(self):
        return "Connection()"
    
    def __str__(self):
        return self.addr

def asHost(Connection:Connection):
    print(f"[New Connection] {Connection.addr} connected as HOST! ")
    conn = Connection.conn
    
    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            msg_length = int(msg_length)
            
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                break
            
            if msg == "%STARTGAME":
                global gameState
                print("[HOST] Game starting! ")
                gameState = "Running!"
                gameManager(contactList)
                
            
            print(f"[{addr}] {msg}")
    print()
    
def asPlay(Connection:Connection):
    print(f"[New Connection] {Connection.addr} connected as PLAYER! ")
    conn = Connection.conn
    
    while gameState == "NotRunning":
        pass
    
    
    
def establishConn(conn, addr):
    while True:
        fm = conn.recv(9).decode(FORMAT)
        # $ recv 9 because first message is either hostjoin or playjoin
        
        if fm:
            if fm == "%HOSTJOIN":
                connClass = Connection(conn, addr, True)
                hostList.append(connClass)
                return asHost(connClass)
            elif fm == "%PLAYJOIN":
                connClass = Connection(conn, addr)
                contactList.append(connClass)
                return asPlay(connClass)
            else: continue


def gameManager(contactList):
    with open("questions.txt", "r") as file:
        lines = file.readlines()
    
    for contact in contactList:
        contact.send(("%REQUESTS").encode(FORMAT))
    
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
        
        print(f"[Server] Server listening on {ADDR}]!")
        
        conn, addr = server.accept()
        
        threading.Thread(target=establishConn, args=(conn, addr)).start()

except: exit()