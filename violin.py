import random
class Gitam():
    def __init__(self):
        return
    
    def initiate(self, name, jati, talam, ragam, prefspeed, prefnpb):
        self.name = name
        self.jati = jati
        self.talam = talam
        self.ragam = ragam
        self.prefspeed = prefspeed
        self.prefnpb = prefnpb
        
    def getinfo(self):
        infoarray = [self.name, self.talam, self.ragam, self.prefspeed, self.prefnpb]
        return infoarray
    
    def store(self,x):
        with open(x+'.txt', 'w') as filehandle:
            for listitem in self.getinfo():
                filehandle.write('%s\n' % listitem)
        filehandle.close()
    
    def refresh(self, x):
        returnlist = []
        # open file and read the content in a list
        with open(x+'.txt', 'r') as filehandle:
            for line in filehandle:
            # remove linebreak which is the last character of the string
                currentPlace = line[:-1]

                # add item to the list
                returnlist.append(currentPlace)
        filehandle.close()
        self.name, self.talam, self.ragam, self.prefspeed, self.prefnpb = returnlist
    
    def refreshandreturn(self,x):
        self.refresh(x)
        return self.getinfo()


ragams= {
    "Mayamalavagaula": "S R1 G2 M1 P D1 N2 S. \nS. N2 D1 P M1 G2 R1 S",
    "Shankarabaranam": "S R2 G2 M1 P D2 N2 S. \nS. N2 D2 P M1 G2 R2 S",
    "Malahari": "S R1 M1 P D1 S. \nS. D1 P M1 G2 R1 S",
    "Suddha Saveri": "S R2 M1 P D2 S. \nS. D2 P M1 R2 S",
    "Mohanam": "S R2 G2 P D2 S. \nS. D2 P G2 R2 S",
    "Kalyani": "S R2 G2 M2 P D2 N2 S. \nS. N2 D2 P M2 G2 R2 S",
    "Saveri": "S R1 M1 P D1 S. \nS. N2 D1 P M1 G2 R1 S",
    "Bilahari": "S R2 G2 P D2 S. \nS N2 D2 P M1 G2 R2 S",
    "Khamas": "S M1 G2 M1 P D2 N1 S. \nS. N1 D2 P M1 G2 R2 S" 
}


gitam1 = Gitam()
gitam1.refresh("gitam1")

gitam2 = Gitam()
gitam2.refresh("gitam2")

gitam5 = Gitam()
gitam5.refresh("gitam5")

gitam6 = Gitam()
gitam6.refresh("gitam6")

gitam7 = Gitam()
gitam7.refresh("gitam7")

gitam8 = Gitam()
gitam8.refresh("gitam8")

swarajati1 = Gitam()
swarajati1.refresh("swarajati1")

swarajati2 = Gitam()
swarajati2.refresh("swarajati2")

learnedlist=[gitam1, gitam2, gitam5, gitam6, gitam7, gitam8, swarajati1, swarajati2]
choice = random.choice(learnedlist).getinfo()[1:-1]
print(choice)
while input(">>>") == "+":
    print(ragams[choice.getinfo()[2]])
