from sympy import var
from sympy import sympify

"""for ab in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    exec(str(ab+" = var(\""+ab+"\")"))
user_input = '5*x+2'
expr = sympify(user_input)
res = expr.subs(x, 3.14)
print(res)"""


inputEquation = input("What is the equation? -> ")
varlist=[]

for abc in inputEquation:
    if abc.isalpha():
        exec(str(abc+" = var(\""+abc+"\")"))
        varlist.append(abc)
        if inputEquation[inputEquation.index(abc)-1].isdigit() and inputEquation.index(abc)-1>=0:
            inputEquation = inputEquation[:inputEquation.index(abc)] + '*' + inputEquation[inputEquation.index(abc):]

inputEquation.replace("^", "**")
expr = sympify(inputEquation)
exec("ans = expr.subs(varlist[0], input())")
print(ans)