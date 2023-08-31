import os
import time
import copy

pieces = {
    "pawn": ["♟", "♙"],
    "rook": ["♜", "♖"],
    "knight": ["♞", "♘"],
    "bishop": ["♝", "♗"],
    "queen": ["♛", "♕"],
    "king": ["♚", "♔"],
    "whitepawn": "♟",
    "blackpawn": "♙",
    "whiterook": "♜",
    "blackrook": "♖",
    "whitebishop": "♝",
    "blackbishop": "♗",
    "whiteknight": "♞",
    "blackknight": "♘",
    "whitequeen": "♛",
    "blackqueen": "♕",
    "whiteking": "♚",
    "blackking": "♔",
    "♟": ["white", "pawn"],
    "♙": ["black", "pawn"],
    "♜": ["white", "rook"],
    "♖": ["black", "rook"],
    "♞": ["white", "knight"],
    "♘": ["black", "knight"],
    "♝": ["white", "bishop"],
    "♗": ["black", "bishop"],
    "♛": ["white", "queen"],
    "♕": ["black", "queen"],
    "♚": ["white", "king"],
    "♔": ["black", "king"],
    "white": ["♟︎", "♜", "♞", "♝", "♛", "♚"],
    "black": ["♙", "♖", "♘", "♗", "♕", "♔"],
    0: ["empty", ""]
}

board = [
    list("♜♞♝♛♚♝♞♜"),
    list("♟♟♟♟♟♟♟♟"), [0 for x in range(8)], [0 for x in range(8)],
    [0 for x in range(8)], [0 for x in range(8)],
    list("♙♙♙♙♙♙♙♙"),
    list("♖♘♗♔♕♗♘♖")
]

studyboard = copy.deepcopy(board)

def abs(x):
    if x < 0:
        return -x
    return x


def printBoard(Bout=None):
    if Bout == None:
        Bout = board

    for x in board:
        for y in x:
            print(y, "", end='')

        print()

    return


def isValidMove(board, fromxy, toxy):
    # TODO: see if the from or to coords are out of the board
    fx, fy = fromxy
    tx, ty = toxy
    fpiece = board[fx][fy]
    tpiece = board[tx][ty]
    isCapture = False if tpiece == 0 else True
    fpieceData = pieces[fpiece]
    fpieceColor, fpiecetype = fpieceData
    tpieceData = pieces[tpiece]
    tpieceColor, tpiecetype = tpieceData

    if fpiece == 0:
        return False, "theres nothing to move there"
    elif tpieceColor == fpieceColor:
        return False, "killin ur own piece, huh?"

    if fpiece in pieces['rook']:
        if fx == tx and fy != ty:  #70-50
            if fy > ty:
                for cy in range(ty + 1, fy):
                    if not (board[fx][cy] == 0):
                        return (False, "invalid rook move (004)"
                                ) if not isCapture else (
                                    False, "invalid rook move (005)")

                return True, ""
            elif fy < ty:
                for cy in range(fy + 1, ty):
                    if not (board[fx][cy] == 0):
                        return (False, "invalid rook move (004)"
                                ) if not isCapture else (
                                    False, "invalid rook move (005)")
        elif fy == ty and fx != tx:
            if fx > tx:
                for cx in range(tx + 1, fx):
                    if not (board[cx][fy] == 0):
                        return (False, "invalid rook move (004)"
                                ) if not isCapture else (
                                    False, "invalid rook move (005)")

                return True, "42-"

            elif fx < tx:
                for cx in range(fx + 1, tx):
                    if not (board[cx][fy] == 0):
                        return (False, "invalid rook move (004)"
                                ) if not isCapture else (
                                    False, "invalid rook move (005)")

                return True, ""
        return False, "invalid rook move (001)"
    
    elif fpiece in pieces['knight']:
        if (abs(fx-tx)==2 and abs(fy-ty)==1) or (abs(fy-ty)==2 and abs(fx-tx)==1):
            return True, ""
        return False, "invalid knight move"            
                
            
    elif fpiece in pieces['pawn']:
        if abs(ty-fy) > 2 or abs(tx-fx) > 3:
            return False, ""
        if fpieceColor == "white":
            if isCapture:
                if tx - fx == 1 and (abs(fy-ty) == 1):
                    return True, "pawn capture"
                return False, "invalid pawn move (002)"
            else:
                movedistance = tx - fx
                if movedistance == 1 and fy - ty == 0:
                    return True, "pawn step 1"
                elif (movedistance == 2 and fx == 1 and fy - ty == 0
                        and board[2][fy] == 0):
                    return True, "pawn step 2"
                elif movedistance == 2 and fx == 1 and fy - ty == 0:
                    return False, "invalid pawn move (003)"
                return False, "invalid pawn move (001)"

        elif fpieceColor == "black":
            if isCapture:
                if (fx - tx == 1 and (abs(ty-fy) == 1)):
                    return True, "pawn capture"
                return False, "invalid pawn move (002)"
            else:
                movedistance = fx - tx
                if movedistance == 1 and fy - ty == 0:
                    return True, "pawn step 1"
                elif (movedistance == 2 and fx == 6 and fy - ty == 0
                        and board[5][fy] == 0):
                    return True, "pawn step 2"
                elif movedistance == 2 and fx == 6 and fy - ty == 0:
                    return False, "invalid pawn move (003)"
                return False, "invalid pawn move (001)"

    elif fpiece in pieces["queen"]:
        # rook moves
        if fx == tx and fy != ty:  #70-50
            if fy > ty:
                for cy in range(ty + 1, fy):
                    if not (board[fx][cy] == 0):
                        return (False, "invalid rook move (004)"
                                ) if not isCapture else (
                                    False, "invalid rook move (005)")

                return True, ""
            elif fy < ty:
                for cy in range(fy + 1, ty):
                    if not (board[fx][cy] == 0):
                        return (False, "invalid rook move (004)"
                                ) if not isCapture else (
                                    False, "invalid rook move (005)")
        elif fy == ty and fx != tx:
            if fx > tx:
                for cx in range(tx + 1, fx):
                    if not (board[cx][fy] == 0):
                        return (False, "invalid rook move (004)"
                                ) if not isCapture else (
                                    False, "invalid rook move (005)")

                return True, ""

            elif fx < tx:
                for cx in range(fx + 1, tx):
                    if not (board[cx][fy] == 0):
                        return (False, "invalid rook move (004)"
                                ) if not isCapture else (
                                    False, "invalid rook move (005)")

                return True, ""
        #bishop moves
        if abs(fx-tx) == fx-tx: # meaning its positive
            #right side bishop move
            if abs(fy-ty) == fy-ty:
                # downward bishop move
                for iter in range(1, abs(fy-ty)): # 1, 2
                    if not (board[fx+iter][fy+iter] == 0):
                        return (False, "invalid bishop move(004)")
                return True, ""
            elif abs(fy-ty) == -(fy-ty):
                # upward bishop move
                for iter in range(1, abs(fy-ty)): # 1, 2
                    if not (board[fx-iter][fy+iter] == 0):
                        return (False, "invalid bishop move(004)")
                return True, ""       
        elif abs(fx-tx) == -(fx-tx): #meaning its negative
            # left side bishop move
            if abs(fy-ty) == fy-ty:
                # downward bishop move
                for iter in range(1, abs(fy-ty)): # 1, 2
                    if not (board[fx+iter][fy-iter] == 0):
                        return (False, "invalid bishop move(004)")
                return True, ""
                
            elif abs(fy-ty) == -(fy-ty):
                # upward bishop move
                for iter in range(1, abs(fy-ty)): # 1, 2
                    if not (board[fx-iter][fy-iter] == 0):
                        return (False, "invalid bishop move (004)")
                return True, ""

    elif fpiece in pieces["bishop"]:
        if abs(fx-tx) == abs(fy-ty):
            #bishop moves
            if abs(fx-tx) == fy-ty: # meaning its positive
                #right side bishop move
                if abs(fy-ty) == fy-ty:
                    # downward bishop move
                    for iter in range(1, abs(fy-ty)): # 1, 2
                        if not (board[fx+iter][fy+iter] == 0):
                            return (False, "invalid bishop move(004)")
                    return True, ""
                elif abs(fy-ty) == -(fy-ty):
                    # upward bishop move
                    for iter in range(1, abs(fy-ty)): # 1, 2
                        if not (board[fx-iter][fy+iter] == 0):
                            return (False, "invalid bishop move(004)")
                    return True, ""       
            elif abs(fx-tx) == -(fx-tx): #meaning its negative
                # left side bishop move
                if abs(fy-ty) == fy-ty:
                    # downward bishop move
                    for iter in range(1, abs(fy-ty)): # 1, 2
                        if not (board[fx+iter][fy-iter] == 0):
                            return (False, "invalid bishop move(004)")
                    return True, ""
                    
                elif abs(fy-ty) == -(fy-ty):
                    # upward bishop move
                    for iter in range(1, abs(fy-ty)): # 1, 2
                        if not (board[fx-iter][fy-iter] == 0):
                            return (False, "invalid bishop move (004)")
                    return True, ""

    elif fpiece in pieces['king']:
        if abs(fx-tx)<2 and abs(fy-ty)<2:
            return True, ""
        return False, "invalid king move (001)"
    return False, "unmapped"

def alphaToColor(l):
    if l == "w": return "white"
    if l == "b": return "black"
    return

def oppositeColor(color):
    if color == "white": return "black"
    if color == "black": return "white"
    return

def findKing(board1, mover):
    for x in range(0,8):
        for y in range(0,8):
            piece = board1[x][y]
            if piece in pieces[mover+"king"]:
                return x, y
                
def isCheck(board1, mover):
    kx, ky = findKing(board1, mover)
    for x in range(0,8):
        for y in range(0,8):
            piece = board1[x][y]
            if piece == 0 or mover in pieces[piece]:
                pass
            else:
                #print(piece, pieces[mover])
                if isValidMove(board1, (x, y), (kx, ky))[0]:
                    return True, (x, y)

def causesCheckmate(board1, mover):
    return False


# init
whosTurn = "w"

# gameloop
while True:
    os.system('cls' if os.name=='nt' else 'clear')
    printBoard()
    # xy-xy format, where the first xy is the initial pos
    # and the second xy is the position to move to
    # {1 <= x <= 8 | x e W} {1 <= y <= 8 | y e W}
    moveinput = input("> ").replace(" ", "")

    # interpret the move
    fromx, fromy, _, tox, toy, *extra = list(moveinput)

    if (not fromx.isnumeric()) and (not fromy.isnumeric()) and (
            not tox.isnumeric()) and (not toy.isnumeric()):
        continue

    fromx = int(fromx) - 1
    fromy = int(fromy) - 1
    tox = int(tox) - 1
    toy = int(toy) - 1

    print(f"DEBUG: {board[fromx][fromy]} to {board[tox][toy]}!")
    isValid = isValidMove(board, (fromx, fromy), (tox, toy))
    print(isValid)
    if isValid[0]:
        # TODO: delete after validations are over
        studyboard[tox][toy] = studyboard[fromx][fromy]
        studyboard[fromx][fromy] = 0
        if isCheck(studyboard, alphaToColor(whosTurn)):
            print(isCheck(studyboard, alphaToColor(whosTurn)))
            print("Causes checkmate, try again!")
            studyboard = copy.deepcopy(board)
        elif causesCheckmate(studyboard, alphaToColor(whosTurn)):
            print("You win! You checkmated the opponent!")
            break
        elif pieces[board[fromx][fromy]][0] != alphaToColor(whosTurn):
            print("not your turn")
            studyboard = copy.deepcopy(board)
        else:
            board = copy.deepcopy(studyboard)
            # switch turn
            whosTurn = "w" if whosTurn == "b" else "b"
    else:
        print(isValid[1])

    time.sleep(5)

# errorcodes
# 001: invalid move which is not a capture
# 002: invalid move that is a capture
# 003: piece in middle of pawn's 2 step move
# 004: piece in middle of path
# 005: piece in middle of path while capturing
# 006: illegal move