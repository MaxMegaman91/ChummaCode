# https://edabit.com/challenge/8vJaRDKxoGQ5JnCCz
# Message to appa: This is an expert problem but its easy to me :)

def is_exactly_three(inputnumber):
    thelist = []
    for factor in range(1,inputnumber+1):
        if inputnumber % factor == 0: thelist.append(factor)
    if len(thelist) == 3: return True
    else: return False
