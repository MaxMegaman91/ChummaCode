import socket
import threading
import time, os


HEADER = 64 # first message from the client should be 64 bytes 
PORT = 65433 # server port number
FORMAT = 'utf-8' # decode format from bytes
DISCONNECT_MESSAGE = "!DISCONNECT" # the message sent from the client to let the server know 
    # .. that you are disconnecting from the server

SERVER = "192.168.2.14" # server computer ip address (!SHOULD BE REPLACED FOR OTHER SERVER COMPS!)
ADDR = (SERVER, PORT) # makes the server and port information convenient for binding

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT) # encoding the msg to bytes
    msg_length = len(message) # the length of the bytes
    send_length = str(msg_length).encode(FORMAT) # turning the length from int -> str -> bytes
    send_length += b' ' * (HEADER - len(send_length)) # adding blankspace after the sendlength to fullfill to HEADER bytes

    client.send(send_length) # sends length in HEADER bytes
    client.send(message) # sends message to server

    # print(client.recv(2048).decode(FORMAT))
 
def printBoard(board):
    print("""
 {0} | {1} | {2} 
-----------
 {3} | {4} | {5} 
-----------
 {6} | {7} | {8}    
""".format(*board))

try:
    time.sleep(3) #initialize connection
    while True: 
        servermsg = client.recv(2048).decode(FORMAT)
        if servermsg and servermsg != "!WAIT":
            if servermsg == "!TURN":
                send(input("> "))
            elif servermsg[:2] == "!B":
                os.system("cls")
                printBoard(servermsg[2:])
            elif servermsg == "!NG":
                input("Play again? Press Enter or CTRL+C\n> ")
            elif servermsg != "!TURN":
                print(servermsg)
except KeyboardInterrupt:
    send(DISCONNECT_MESSAGE)
# !BX
