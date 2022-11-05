"""import os, time

board = [[" "," "," "],[" "," "," "],[" "," "," "]]
activePlayer = True

def print_board(board):
    print("\n")
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("---+---+---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("---+---+---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")
    print("\n")
    return

def change_board(location, val="x"):
    global board
    """"""
    Takes 2 arguments and modifies board to put in user input
    1) location as string with horizontal letter and vertical number (ex. a1, c3, etc.)
    2) value as either x or o, or " " to clear
    """"""
    location = list(location)
    realLocation = [int({"a":1,"b":2,"c":3}[location[0]]), int(location[1])]
    
    if board[realLocation[0]-1][realLocation[1]-1] in ["x", "o"]: return True 
    
    board[realLocation[0]-1][realLocation[1]-1] = val

    return False

def checkWin(board):
    # Horizontal checks
    for x, y, z in board:
        if x==y and y==z and x != " ": return x
    
    # Vertical checks
    for x in range(3):
        if board[0][x] == board[1][x] and board[1][x] == board[2][x] and board[0][x] != " ": return board[0][x]
    
    # Diagonal checks
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ": return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != " ": return board[1][1]

    return False


while True:

    activePlayer = not activePlayer
    playerid = "o" if activePlayer else "x"

    os.system('cls' if os.name == 'nt' else 'clear')

    print_board(board)
    while change_board(input("Where do you place your " + playerid + "? -> "), playerid): time.sleep(1)
    if checkWin(board): 
        os.system('cls' if os.name == 'nt' else 'clear')

        print_board(board)
        print(checkWin(board) + " wins! ")
        time.sleep(15)
        quit()
    




"""

import tkinter as tk

window = tk.Tk()

