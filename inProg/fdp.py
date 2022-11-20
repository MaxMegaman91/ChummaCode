import math, random

class fraction():
    def __init__(self, num=0, den=1):
        self.numerator, self.denominator = num, den
        self.raw = str(num) + "/" + str(den)
    
    def decimate(self, roundPlaces=3):
        realval = str(self.numerator/self.denominator)
        return round(realval, roundPlaces)
    
    def percentify(self, wantsign=True):
        return str(self.decimate/100) + "%" if wantsign else str(self.decimate/100)
    
    def __repr__(self): # for value reading
        return str(self.raw)
        
    def __str__(self): # For stringify and print
        return str(self.raw)

for qnum in range(qcount):
    fromval = random.choice(["fraction", "decimal", "percent"])
    toval = random.choice(["fraction", "decimal", "percent"])