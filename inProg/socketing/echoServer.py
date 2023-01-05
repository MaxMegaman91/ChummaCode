# echo-server.py

import socket, socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

board = [[" "," "," "],[" "," "," "],[" "," "," "]]

def boardStringify(board):
    ret = []
    for x in board:
        ret.append("".join(x))
    return "".join(ret)

def construct(inp, board):
    char, row, col = inp.decode()

    try: board[int(row)-1][int(col)-1] = char
    except IndexError: pass
    return board

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:

        socket.bind((HOST, PORT))
        socket.listen()
        conn, addr = socket.accept()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket2:
            socket2.bind((HOST, PORT+1))
            socket2.listen()
            conn2, addr2 = socket2.accept()

            with conn, conn2:
                print(f"Connected by {addr}")
                print(f"Connected by {addr2}")
                while True:
                    data = conn.recv(1024)
                    if data:
                        construct(data, board)
                    conn.sendall(boardStringify(board).encode())

                    data = conn2.recv(1024)
                    if data:
                        construct(data, board)
                    conn.sendall(boardStringify(board).encode())

# except ConnectionAbortedError: cleanup()