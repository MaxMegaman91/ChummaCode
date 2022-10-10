import math, random, sys, time, os
debug = False


class Triangle():
    def __init__(self, is90=False, decpoint=1,rmax=30):

        if is90:
            sys.exit("In development... ")
        

        # where a, b, c are lengths
        self.a, self.b = random.sample(range(1,rmax),2)
        if self.b > self.a: self.a, self.b = self.b, self.a
        self.c = random.randint(self.a-self.b+1, self.a+self.b-1)

        while self.c == self.a:
            self.a, self.b = random.sample(range(1,rmax),2)
            if self.b > self.a: self.a, self.b = self.b, self.a
            self.c = random.randint(self.a-self.b+1, self.a+self.b-1)

        # and A, B, C are angles opposite its lower
        self.dega = ((self.b**2 + self.c**2) - self.a**2) / (2*self.b*self.c)
        self.degb = ((self.c**2 + self.a**2) - self.b**2) / (2*self.c*self.a)
        self.A_real = math.degrees(math.acos(self.dega))
        self.B_real = math.degrees(math.acos(self.degb))
        self.C_real = 180 - self.A_real - self.B_real

        # rounding absurd decimal values to 1 pt
        self.A = round(self.A_real, decpoint)
        self.B = round(self.B_real, decpoint)
        self.C = round(self.C_real, decpoint)

        if debug:
            print("Side a: ", self.a)
            print("Side b: ", self.b)
            print("Side c: ", self.c)
            print("Angle A: ", self.A)
            print("Angle B: ", self.B)
            print("Angle C: ", self.C)
            print("Angles match: ", self.A_real+self.B_real+self.C_real == 180)
        
        self.info = {
            "len a": self.a,
            "len b": self.b,
            "len c": self.c,
            "ang a": self.A,
            "ang b": self.B,
            "ang c": self.C,
            "ran a": self.A_real,
            "ran b": self.B_real,
            "ran c": self.C_real
        }

        return
    
    def trigPractice(self, *args):

        availTypes = ["sss", "ssa", "saa", "sssa", "sssaa", "ssaa", "saaa"]

        if args:
            type = args[0]
            type = type.lower()
            if type not in availTypes:
                type = random.choice(availTypes)
        else:
            type = random.choice(availTypes)
        
        availl = [1,2,3]
        availa = [1,2,3]
        letters = {
            1:"a",
            2:"b",
            3:"c"
        }

        for x in type:
            if x == "s":
                pull = availl[0]
                availl.remove(pull)
                pull = letters[pull]
                print("Side", pull, "has a length of", self.info["len "+pull])
            elif x == "a":
                pull = availa[0]
                availa.remove(pull)
                pull = letters[pull]
                print("Angle", pull, "is equal to", self.info["ang "+pull], "degrees")
        wait = input("Press enter with solution! ")


        print("Side a has a length of: ", self.info["len a"])
        print("Side b has a length of: ", self.info["len b"])
        print("Side c has a length of: ", self.info["len c"])
        print("Angle a has a length of: ", self.info["ang a"])
        print("Angle b has a length of: ", self.info["ang b"])
        print("Angle c has a length of: ", self.info["ang c"])

def mainTrig():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        myTriangle = Triangle()
        myTriangle.trigPractice()
        time.sleep(10)