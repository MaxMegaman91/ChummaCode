#=#
# imports
import socket, threading, time

#=#
# Constants
HEADER = 64
SERVER = "192.168.86.21"
PORT = 14014
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "%DISCONNECT"

def sendMsg(client, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)


def requestsManager(client):
    while True:
        request = client.recv(2048).decode(FORMAT)
        
        if request:
            if request == "%NAMEREQR":
                msg = input("Nickname for reference? \n> ")
            elif request == "%READYUP?":
                input("Enter to start game! \n> ")
                msg = "&STRTGAME"
            elif request[:9] == "%QUESTION":
                question = request[10:]
                print(f"QUESTION: {question}")
                time.sleep(30)
                msg = ""
            sendMsg(client, msg)
    
#=#
# Init
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(("&HOSTJOIN").encode(FORMAT))

requestsManager(client)