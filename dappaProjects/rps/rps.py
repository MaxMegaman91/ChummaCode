import random
options = ["r", "p", "s"]




# Declarations
class Computer():
    def __init__(self, difficultyLevel=1, importFile=True) -> None:
        self.difficulty = difficultyLevel
        self.playhist = []
        self.enemyhist = []
        self.winlist = []
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.cusoptions = ["r", "p", "s"]
        self._towin = {
            "r":"p",
            "p":"s",
            "s":"r"
        }
        self._tolose = {
            "r":"s",
            "s":"p",
            "p":"r"
        }
        self.fileImport()
    
    def rpspull(self) -> str:
        # pullalg
        pull = self._rpspull()

        # Add pull to history and return
        self.playhist.append(pull)
        return pull 

    def without(self, a, b):
        c = a
        return c.remove(b)

    def _rpspull(self):
        try:
            if self.winlist[-1] == "w":
                return random.choice(self.without(options, self._towin[self.enemyhist[-1]])) if self.winlist[-2] == "l" else self._towin[self.enemyhist[-1]]
            elif self.winlist[-1] == "l":
                return self._towin[self.enemyhist[-1]] if self.winlist[-2] == "w" else random.choice(self.without(options, self._towin[self.enemyhist[-1]]))
            elif self.winlist[-1] == "t":
                return self._tolose[self.enemyhist[-1]] if self.winlist.count("t") <2 else self._towin[self.enemyhist[-1]]
            return random.choice(options)
        except: return random.choice(options)
    
    def validateWin(self, pull1, pull2=0) -> str:
        if pull2 == 0: 
            pull2 = self.rpspull()
            pull1 = pull1.lower()[0]
            self.enemyhist.append(pull1)
        else:
            pull1, pull2 = pull1.lower()[0], pull2.lower()[0]
        if pull1 == pull2:
            self.winlist.append("t")
            self.ties += 1
            return "tie"
        elif pull1 == "r" and pull2 == "s":
            self.winlist.append("w")
            self.losses += 1
            return "real"
        elif pull1 == "p" and pull2 == "s":
            self.winlist.append("l")
            self.wins += 1
            return "comp"
        elif pull1 == "r" and pull2 == "p":
            self.winlist.append("l")
            self.wins += 1
            return "comp"
        elif pull1 == "s" and pull2 == "p":
            self.winlist.append("w")
            self.losses += 1
            return "real"
        elif pull1 == "s" and pull2 == "r":
            self.winlist.append("l")
            self.wins += 1
            return "comp"
        elif pull1 == "p" and pull2 == "r":
            self.winlist.append("w")
            self.losses += 1
            return "real"
        else: return 0
    
    def details(self, txt=False):
        yield "Player pull list: " + str(self.enemyhist)
        yield "Computer pull list: " + str(self.playhist)
        yield "Winloss list: " + str(self.winlist)
        yield "Number of computer wins: " + str(self.wins)
        yield "Number of computer losses: " + str(self.losses)
        yield "Number of computer ties: " + str(self.ties)
        yield "Difficulty level: " + str(self.difficulty)

    def export(self, all=False):
        with open("rpsdata.txt", "w") as file:
            file.write("".join(self.enemyhist))
            file.write("\n")
            file.write("".join(self.winlist))
        return

    def fileImport(self, all=False):
        with open("rpsdata.txt", "r") as file:
            try: 
                self.enemyhist = list(file.readlines()[0])
                self.winlist = list(file.readlines()[1])
            except IndexError: 
                self.enemyhist=[]
                self.winlist=[]
        return
    

myComputer = Computer()

for i in range(5):
    print(myComputer.validateWin(input("What would you like to pull? Rock, paper, or scissors? -> ")))
    i += 1

for x in myComputer.details():
    print(x)

myComputer.export()
del myComputer