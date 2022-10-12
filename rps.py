import random
options = ["r", "p", "s"]

def validateWin(pull1, pull2):
    if pull1 == pull2:
        return "tie"
    elif pull1 == "r" and pull2 == "s":
        return "p1 wins!"
    elif pull1 == "p" and pull2 == "s":
        return "p2 wins!"
    elif pull1 == "r" and pull2 == "p":
        return "p2 wins!"
    elif pull1 == "s" and pull2 == "p":
        return "p1 wins!"
    elif pull1 == "s" and pull2 == "r":
        return "p2 wins!"
    elif pull1 == "p" and pull2 == "r":
        return "p1 wins!"
    else: return 0

# Declarations
p1wins = p2wins = ties = 0
try:
    while True: 
        result = validateWin(input("r, p, or s? ")[0].lower(), random.choice(options))
        if result == "tie": ties += 1
        elif result == 0: pass
        elif int(result[1]) == 1: p1wins += 1
        elif int(result[1])==2: p2wins += 1
        print(result)
except KeyboardInterrupt: print("\n",p1wins, p2wins, ties, sep="\n")
