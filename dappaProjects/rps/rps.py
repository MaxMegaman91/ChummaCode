import random
options = ["r", "p", "s"]



# Declarations
class Computer():
    def __init__(self, difficultyLevel=1) -> None:
        self.difficulty = difficultyLevel
        self.playhist = []
        self.enemyhist = []
        self.wins = 0
        self.losses = 0
        self.ties = 0
    
    def rpspull(self) -> str:
        # pullalg
        pull = self._rpspull()

        # Add pull to history and return
        self.playhist.append(pull)
        return pull 

    def _rpspull(self):
        # stuff to return choice
        return random.choice(options)
    
    def validateWin(self, pull1, pull2=0) -> str:
        if pull2 == 0: 
            pull2 = self.rpspull()
            pull1 = pull1.lower()[0]
            self.enemyhist.append(pull1)
        else:
            pull1, pull2 = pull1.lower()[0], pull2.lower()[0]
        if pull1 == pull2:
            self.ties += 1
            return "tie"
        elif pull1 == "r" and pull2 == "s":
            self.losses += 1
            return "real"
        elif pull1 == "p" and pull2 == "s":
            self.wins += 1
            return "comp"
        elif pull1 == "r" and pull2 == "p":
            self.wins += 1
            return "comp"
        elif pull1 == "s" and pull2 == "p":
            self.losses += 1
            return "real"
        elif pull1 == "s" and pull2 == "r":
            self.wins += 1
            return "comp"
        elif pull1 == "p" and pull2 == "r":
            self.losses += 1
            return "real"
        else: return 0
    
    def details(self, txt=False):
        yield "Player pull list: " + str(self.enemyhist)
        yield "Computer pull list: " + str(self.playhist)
        yield "Number of computer wins: " + str(self.wins)
        yield "Number of computer losses: " + str(self.losses)
        yield "Number of computer ties: " + str(self.ties)
        yield "Difficulty level: " + str(self.difficulty)

    def export(self, all=False):
        with open("rpsdata.txt", "w") as file:
            file.write("".join(self.enemyhist))
        return

    def fileImport(self, all=False):
        with open("rpsdata.txt", "r") as file:
            self.enemyhist = list(file.readlines()[0])
        return
    

i=0
myComputer = Computer()
myComputer.fileImport()
while i<5:
    myComputer.validateWin(input("What would you like to pull? Rock, paper, or scissors? -> "))
    i += 1

for x in myComputer.details():
    print(x)

myComputer.export()
del myComputer