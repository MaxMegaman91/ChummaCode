SAVE_PATH = "C:/Users/aarus/ChummaCode/inProg/thengAcademy/"
import tkinter as tk
import names, random

window = tk.Tk()

window.columnconfigure(list(range(1)), minsize=50)
window.rowconfigure(list(range(2)), minsize=50)
window.title("ThengAcademy")
window.resizable(width=False, height=False)


def randomFactor(n):
    returnList = []
    for x in range(1,(n//2)+1):
        if n/x == n//x:
            returnList.append(x)
    
    return random.choice(returnList) if returnList else 0

def randomComposite(a, b):
    returnList = []
    for x in range(a, b+1):
        if isComposite(x): 
            returnList.append(x)
    
    return random.choice(returnList) if returnList else 0

def isComposite(n):
    for x in range(2,n):
        if n/x == n//x:
            return True
    return False

def getProblem():
    with open(SAVE_PATH+'wordProblems.txt', 'r') as file:
        problemTypes = file.readlines()
    print(problemTypes)
    RAWproblem = random.choice(problemTypes)

    problem = RAWproblem

    # DOWN
    P = randomComposite(0,100)/100
    D = int(P*random.randint(0,20)*100)
    N = (P)*D
    # UP

    C = names.get_first_name()
    
    problem = problem.replace("^P", str(P))
    problem = problem.replace("^D", str(D))
    problem = problem.replace("^N", str(N))
    problem = problem.replace("^C", str(C))

    want = problem[-1]
    problem = problem[:-3]

    if want == "P":
        return problem, P
    elif want == "D":
        return problem, D
    elif want == "N":
        return problem, N
    else:
        return "", ""
    
    
    

"""print(getProblem())

problemW = tk.Text(window)
window.mainloop()"""

print(getProblem())

