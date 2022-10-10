# https://edabit.com/challenge/rBNPRqYMApGLTgmBe

def factorial(x):
    answer = 1
    for i in range(0,x):
        answer *= x-i
    return answer

def combinations(k,n):
    return factorial(n) / (factorial(k)*(factorial(n-k)))


