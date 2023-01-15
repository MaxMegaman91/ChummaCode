#=#
# imports
import socket, threading, time

#=#
# Constants
HEADER = 64
SERVER = "192.168.2.112"
PORT = 14014
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "%DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(("%HOSTJOIN").encode(FORMAT))
time.sleep(1)
client.send(("10").encode(FORMAT))
client.send(("%STARTGAME").encode(FORMAT))