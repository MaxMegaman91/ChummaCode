import random
x=0
# """"""
while (N/D) != round(n/d,2) or x==0:
    x=1

    n = N = P = random.randint(0,100)
    D = d = 100
    print(N/D)

    temp = 0.0
    while temp == 0.0: temp = round(random.random(), 1)

    n *= temp
    d *= temp
    n = round(n,2)
    d = round(d)
    print(n/d)

# """"""

print(f"N = {N}, D = {D}, n = {n}, d = {d}, P = {P}")