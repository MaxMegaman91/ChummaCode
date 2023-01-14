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
    x=0
    N = D = n = d = P = 1
    # """"""
    while (N/D) != round(n/d,2) or x==0:
        x=1

        n = N = P = random.randint(0,100)
        D = d = 100

        temp = 0.0
        while temp == 0.0: temp = round(random.random(), 1)

        n *= temp
        d *= temp
        n = round(n,2)
        d = round(d)

    # """"""

    # print(f"N = {N}, D = {D}, n = {n}, d = {d}, P = {P}")
    # UP

    C = names.get_first_name()
    
    problem = problem.replace("^P", str(P))
    problem = problem.replace("^D", str(d))
    problem = problem.replace("^N", str(n))
    problem = problem.replace("^C", str(C))

    want = problem[-2]
    problem = problem[:-3]

    if want == "P":
        return problem, P
    elif want == "D":
        return problem, d
    elif want == "N":
        return problem, n
    else:
        return "", ""
    
    
    

"""print(getProblem())

problemW = tk.Text(window)
window.mainloop()"""

print(getProblem())

