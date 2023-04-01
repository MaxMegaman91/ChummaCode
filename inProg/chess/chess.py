import os
import time

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


def isValidMove(fromxy, toxy):
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
    elif fpieceColor[0] != whosTurn:
        return False, "not ur turn"

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

                return True, ""

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
        return False, "invalid knight move (006)"            
    
    elif fpiece in pieces['king']:
        if fy-ty <= 1 and fx-tx <= 1:
            return True, ""
        return False, "invalid king move (006)"
            
    elif fpiece in pieces['pawn']:
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

    return True, "unmapped"


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
    isValid = isValidMove((fromx, fromy), (tox, toy))
    print(isValid)
    if isValid[0]:
        # TODO: delete after validations are over
        board[tox][toy] = board[fromx][fromy]
        board[fromx][fromy] = 0

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