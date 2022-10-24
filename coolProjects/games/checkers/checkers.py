import os, time


def setupboard():
    global board, wboard
    board = [list("00000000") for x in range(8)]
    wboard = []
    for x in range(8):
        if x%2==0: wboard.append([False, True]*4)
        elif x%2==1: wboard.append([True, False]*4)
    
    adder=1
    for rows in range(0,3): # 0, 1, 2
        for single in range(0,8):
            if wboard[rows][single]:
                board[rows][single] = "w"+str(adder)
                adder += 1
    
    adder=1
    for rows in range(5,8): 
        for single in range(0,8):
            if wboard[rows][single]:
                board[rows][single] = "b"+str(adder)
                adder += 1
    
def printboard(board):
    # Needs work
    for x in board: print(x)

def moveCoin(board, fromlocation=(0,0), tolocation=(0,0)):
    fx, fy = fromlocation
    tx, ty = tolocation
    if coinMoveAble(board, fromlocation, tolocation): board[tx][ty] = board[fx][fy]

def coinMoveAble(board, fromlocation, tolocation):
    """
    needs coding and updating
    return true if coin move is valid
    return false if coin move is invalid
    
    """
    return False

setupboard()
printboard(board)



# I gotta redo all of this