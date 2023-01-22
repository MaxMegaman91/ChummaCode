#=#
# imports
import socket, threading, time, os

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
                sendMsg(client, msg)
            elif request == "%ANSWRQST":
                os.system('clear' if os.name == 'posix' else 'cls')
                msg = input("Which is the answer 1-4? \n> ")
                sendMsg(client, msg)
            elif request[:9] == "%POINTCHK":
                points = request[10:]
                print(f"You have {points} points!")
            else: msg = "%NULLVAL"
            
    
#=#
# Init
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(("&PLAYJOIN").encode(FORMAT))

requestsManager(client)