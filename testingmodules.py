import re
equationInput = input("What is the equation? ") # 2x + 6 = y

equationInput.replace(" ", "")   # 2x+6=y

try:
    ls, rs, *n= equationInput.split("=")
except ValueError:
    print("Invalid equation! ")

fullEquation = []

def combineLikeTerms(terms):
    # First we should sort each term to put higher exponents first
    # Then we should get the variable values for each term
    #
    #
    #
    return "Not Ready"



class Equation():
    def __init__(self, exp):
        exp = exp.replace(" ", "")
        ls, rs, *n = exp.split("=")
        self.inst = breakExp(exp)
        return

    def subs(self, xval=None, yval=None):
        if xval==None and yval==None: return "No value to substitute! "
        elif xval != None:
            return [xval, yval]
        elif yval != None:
            return [xval, yval]