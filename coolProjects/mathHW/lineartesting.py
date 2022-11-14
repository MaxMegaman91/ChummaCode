# this lnreq, not qrep 
class Equation():
    
    def __init__(self, Equation):
        self.equation = Equation
        return

    def _0ToTerms_(self):
        self.terms = []
        return
    
    def __add__(self, new): # to add to another equation
        return Equation(self.equation + new.equation)

    def __sub__(self, new): # to subtract to another equation
        return Equation(self.equation - new.equation)
    
    def __repr__(self): # for value reading
        return str(self.equation)
        
    def __str__(self): # For stringify and print
        return str(self.equation)

class Terms():
    def __init__(self, term):
        import re
        self.rawTerm = term

        subbed = re.sub("[A-Za-z]", lambda ele: " " + ele[0], term) # ? qrep here replace (ele[0] + " ",) with just (ele[0],)
        subbed = subbed.replace("*","")
        self.term = subbed.replace(" ", "*")
        self.tlist = self.term.split("*")

        self.coeff = int(self.tlist[0])
        self.varsAvail = self.tlist[1:]
    
    def __mul__(self, newT):
        ansCoeff = str(self.coeff * newT.coeff)
        # variable multiplication) ansVars = something.something.something
        ansT = Terms(ansCoeff + ansVars)
        return ansT
    
    def _Subs_(self, **kwargs):
        for var, val in kwargs.items():
            if var in self.varsAvail:
                toEval = self.term.replace(var, str(val))
        return eval(toEval)
    
    def __repr__(self): # for value reading
        return str(self.term)
        
    def __str__(self): # For stringify and print
        return str(self.term)

term = Terms("2x")
print(term)
print(term._Subs_(x=5))