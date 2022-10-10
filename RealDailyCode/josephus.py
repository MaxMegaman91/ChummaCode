#https://edabit.com/challenge/L9Zh7dWsENnE9P6qc
# All done
from math import log, floor, pow
def josephus(headcount):
    thelist = list(range(1,headcount+1))
    if headcount >3:
        theahead = headcount - 2**(floor(log(headcount,2)))
        if theahead == 0: return 1
        else: return (theahead)*2 + 1
    elif headcount == 1: return 1
    elif headcount == 2: return 1
    elif headcount == 3: return 3
