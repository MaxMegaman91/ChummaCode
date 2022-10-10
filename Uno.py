import random, os
# RB = Red Block, YR = Yellow Reverse, B+2 = Blue Plus 2 
deck = ["R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "RB", "RR", "R+2",
"Y0", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "YB", "YR", "Y+2",
"B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "BB", "BR", "B+2",
"G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "GB", "GR", "G+2",
"L+4", "L+4", "L+4", "L+4", "LW", "LW", "LW", "LW", "LW", "LW", "LW", "LW"]

downcard = random.choice(deck)
totalplayers= int(input("How many players? "))
turnp = 0

def getmeaning(k):
    global players, i
    if k.lower() == "pick":
        players[i].takecard(1)[0]

class Hand():
    def __init__(self, number):
        self.cardhand = []
        self.number = int(number)
        for i in range(7):
            cardtaken = random.choice(deck)
            self.cardhand.append(cardtaken)
            i+=1

    def gethand(self):
        for i in self.cardhand:
            print(i, end=", ")
    
    def dropcard(self, card):
        global downcard, totalplayers, turnp
        if card in self.cardhand and (card[0] == downcard[0] or card[1] == downcard[1]):
            downcard = card
            self.cardhand.remove(card)
            if self.number + 1 <= totalplayers: turnp +=1 
            elif self.number + 1 > totalplayers: turnp = 0
            else: raise KeyboardInterrupt
            if card[1] == "B":
                return "skip"
            elif card[1] == "+":
                return "plus"
            elif card[1] == "R":
                return "reverse"
            elif card[1] == "W":
                return "wild"
            else: return "reg"
    
    def takecard(self, times):
        global totalplayers
        if times == 1:
            self.cardhand.append(random.choice(deck))
            return self.cardhand[-1]
        elif times > 1:
            i=0
            while i <= times:
                self.cardhand.append(random.choice(deck))
                i+=1
            return self.cardhand[-1]

p1 = Hand(1)
p2 = Hand(2)
players = [p1, p2]
revplayers = players.reverse()
i=0
while i <4:
    players[turnp].gethand()
    print("\n\n\n")
    print(downcard)
    inputtemp = input("What card to drop?")
    players[turnp].dropcard(inputtemp) if inputtemp in deck else getmeaning()
    print("\n\n\n\n" + downcard)  
