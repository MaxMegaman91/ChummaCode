# imports

import socket     # main module for socket programming
import threading  # module for python scripts to be run by multiple threads

# =================================================================================================== #

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


# =================================================================================================== #

def handle_client(conn, addr):
    print(f"\n[NEW CONNECTION] {addr} connected.")

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
                connected = False

            print(f"[{addr}] {msg}") #print addr that sent the msg and the msg itself

            conn.send(input("> ").encode(FORMAT)) # send confirmation 
    
    conn.close()


def start():
    server.listen() # waiting for a connection from any computer

    print(f'[LISTENING] Server is listening on {SERVER}:{PORT}.')
    while True:

        conn, addr = server.accept() # where conn is the socket object for returning I/O
                                     # addr is the IP and PORT of the connecting client
                                     # server.accept() is accepting the connection from 
                                     
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        # create new thread to execute func handle_client when a client connects
        thread.start() # start thread execution
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1} threads/connections")


print("[STARTING] Server is starting...")
try: start()
except KeyboardInterrupt(): exit()