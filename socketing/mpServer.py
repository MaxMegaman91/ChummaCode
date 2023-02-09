# imports

import socket     # main module for socket programming
import threading  # module for python scripts to be run by multiple threads
import time       # sleep
# =================================================================================================== #

# if playernum == 0, then char = x, if playernum = 1, char = o
HEADER = 64 # first message from any client should be 64 bytes
PORT = 65433 # above 1024 (not 8080) and under 65535
# SERVER = "127.0.0.1" # loopback ip address for testing on same computer
# SERVER = "192.168.2.14" # local ip address for testing on local computer, but requires
    # recoding when server code is shifted
SERVER = socket.gethostbyname(socket.gethostname()) # the local ip of your computer
    # referencing the ip of the name of your computer
ADDR = (SERVER, PORT) # makes the server and port information convienient for binding
FORMAT = 'utf-8' # decode format from bytes
DISCONNECT_MESSAGE = "!DISCONNECT" # the message sent from the client to let the server know 
    # .. that they are disconnecting from the server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket class for I/O
server.bind(ADDR) # binding SERVER and PORT info to the server object

ADDRlist = []
USERLIST = {}
connaddr = {}
PlayerCount = 0


def stringify(board):
    return "".join(["".join(x) for x in board])

def valid(move):
    global board
    try:
        r, c, *e = move
        r = int(r)
        c = int(c)
        if r>0 and r<4 and c>0 and c<4:
            if board[r-1][c-1] == " ":
                return True
        return False
    except: return False

def boardUpdate(board, msg, addr):
    global TurnADDR, WaitADDR, ADDRlist, connaddr
    if ADDRlist.index(addr) == 0: playerNum = 0
    else: playerNum = 1
    r, c, *e = msg
    r = int(r)
    c = int(c)

    board[r-1][c-1] = "X" if playerNum == 0 else "O"
    WaitADDR, TurnADDR = TurnADDR, WaitADDR

    for addr in connaddr: connaddr[addr].send(("!B"+stringify(board)).encode(FORMAT)) 

    if winDetect(board) != None: return

    connaddr[TurnADDR].send("!TURN".encode(FORMAT))
    connaddr[WaitADDR].send("!WAIT".encode(FORMAT))


def winDetect(board):
    # horizontal
    for x in board:
        if x[0] == x[1] and x[1] == x[2] and x[0] != " ":
            return ADDRlist[0] if x[1] == "X" else ADDRlist[1]
    
    # vertical
    for x in range(3):
        if board[0][x] == board[1][x] and board[1][x] == board[2][x] and board[1][x] != " ":
            return ADDRlist[0] if board[1][x] == "X" else ADDRlist[1]

    # diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != " ":
        return ADDRlist[0] if board[1][1] == "X" else ADDRlist[1]
    if board[0][2] == board[1][1] and board [1][1] == board[2][0] and board[1][1] != " ":
        return ADDRlist[0] if board[1][1] == "X" else ADDRlist[1]
    
    return None

# =================================================================================================== #
def tictactoeCLIENT(ADDRlist, USERLIST, connaddr):
    global PlayerCount, TurnADDR, board, WaitADDR
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    while PlayerCount != 2: # set to 2
        print(f"[TICTACTOE CLIENT] [ALERT] Only {PlayerCount} players available, requires 2.")
        time.sleep(1)
    
    print(f"Game in session between {ADDRlist[0]} and {ADDRlist[1]}.")
    TurnADDR, WaitADDR = ADDRlist[0], ADDRlist[1]

    for addr in connaddr:
        connaddr[addr].send(("!B"+stringify(board)).encode(FORMAT))

    connaddr[TurnADDR].send("!TURN".encode(FORMAT))
    connaddr[WaitADDR].send("!WAIT".encode(FORMAT))

    while winDetect(board) == None:
        time.sleep(1)

    winADDR = winDetect(board)
    print(f"{winADDR} won the match! ")

    
    if winADDR == TurnADDR: loseADDR = WaitADDR
    elif winADDR == WaitADDR: loseADDR = TurnADDR

    connaddr[winADDR].send("YOU WIN".encode(FORMAT))
    connaddr[loseADDR].send("YOU LOST".encode(FORMAT))

    connaddr[winADDR].send("!NG".encode(FORMAT))
    connaddr[loseADDR].send("!NG".encode(FORMAT))

    time.sleep(5)
    while PlayerCount >= 2:
        tictactoeCLIENT(ADDRlist, USERLIST, connaddr)

    


def handle_client(conn, addr):
    global PlayerCount, USERLIST, connaddr
    
    print(f"\n[NEW CONNECTION] {addr} connected.")

    ADDRlist.append(addr)
    USERLIST[addr] = PlayerCount
    connaddr[addr] = conn
    PlayerCount += 1

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            # this is a blocking line (wont pass until info recvd). recieves 64 bytes from conn
            # this first msg tells us how many bytes we need to listen for the next "real" msg
            # .decode(FORMAT) tells us to decode the bytes into utf8 which is string characters
            # then int changes from the string to the length as an integer to recieve in the next msg
            
            msg = conn.recv(msg_length).decode(FORMAT)
            # recieve the real msg from the conn and decode it with the previously provided info

            if msg == DISCONNECT_MESSAGE: # cut connection when the disconnect msg is sent
                break

            """""" #program space
            validity = valid(msg)
            if validity and TurnADDR == addr:
                boardUpdate(board, msg, addr)
            elif validity and TurnADDR != addr:
                conn.send("NOT YOUR TURN! ".encode(FORMAT))
                conn.send("!WAIT".encode(FORMAT))
            elif not validity:
                conn.send("INVALID COORDS! ".encode(FORMAT))
                conn.send("!TURN".encode(FORMAT))

            # conn.send(input("> ").encode(FORMAT)) # send confirmation 

            """""" #program space
    
    conn.close()


def start():
    server.listen() # waiting for a connection from any computer

    print(f'[LISTENING] Server is listening on {SERVER}:{PORT}.')

    thread2 = threading.Thread(target=tictactoeCLIENT, args=(ADDRlist, USERLIST, connaddr))
    thread2.start()

    while True:
        
        conn, addr = server.accept() # where conn is the socket object for returning I/O
                                     # addr is the IP and PORT of the connecting client
                                     # server.accept() is accepting the connection from 
                                     
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        # create new thread to execute func handle_client when a client connects
        thread.start() # start thread execution

        
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 2} threads/connections")


print("[STARTING] Server is starting...")
try: start()
except KeyboardInterrupt(): server.close()
print("GEEEEEEEEE#")