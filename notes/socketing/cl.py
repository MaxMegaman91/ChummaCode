import socket
import threading
import time


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

    print(client.recv(2048).decode(FORMAT))


def UI():
    while True: send(input("> "))

def BI():
    while True: 
        print(client.recv(2048).decode(FORMAT))
        time.sleep(3)


threading.Thread(target=UI).start()
threading.Thread(target=BI).start()
