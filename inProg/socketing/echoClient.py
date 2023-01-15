# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def drawBoard(board):
    print(""" {0} | {1} | {2} 
-----------
 {3} | {4} | {5} 
-----------
 {6} | {7} | {8} """.format(*board))
    
    return True



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(input().encode())
        data = s.recv(1024).decode()
        drawBoard(list(data))
