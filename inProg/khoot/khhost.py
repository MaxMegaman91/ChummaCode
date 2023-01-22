#=#
# imports
import socket, threading, time, sys, select, json, os

#=#
# Constants
HEADER = 64
SERVER = "192.168.86.21"
PORT = 14014
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "%DISCONNECT"

def rawIn(prompt, timeout=30.0):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ready, _, _ = select.select([sys.stdin], [],[], timeout)
    if ready:
        return sys.stdin.readline().rstrip('\n') # expect stdin to be line-buffered
    else:
        print("\n")
    return "1"

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
                question, *options = question.split("||")
                os.system('clear' if os.name == 'posix' else 'cls')
                print(f"QUESTION: {question}")
                print(f"OPTIONS: \n1. {options[0]} \n2. {options[1]} \n3. {options[2]} \n4. {options[3]}")
                print("\n")
                continue
            elif request == "%QSTNFNSH":
                rawIn("Enter to next question \n> ")
                msg = "&NEXTQSTN"
                print("\n")
            elif request[:9] == "%LDRBOARD":
                os.system('clear' if os.name == 'posix' else 'cls')
                serialLeader = request[10:]
                leaderboard = json.loads(serialLeader)
                # [[aarush, 100]]
                if len(leaderboard) > 5:
                    leaderSpots = 4
                else:
                    leaderSpots = len(leaderboard)
                for n in range(leaderSpots):
                    player, score = leaderboard[n]
                    print(f"At #{n+1}, {player} scored {score} points!")
                print("\n")
                msg = "go"
            elif request == "%GAMEOVER":
                if len(leaderboard) < 3:
                    x = len(leaderboard)
                else: x = len(leaderboard)
                for n in reversed(range(x)):
                    player, score = leaderboard[n]
                    print(f"At #{n+1}, {player} scored {score} points! \n")
                print("\n")
                
            sendMsg(client, msg)
    
#=#
# Init
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(("&HOSTJOIN").encode(FORMAT))

requestsManager(client)