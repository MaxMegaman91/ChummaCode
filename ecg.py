#https://edabit.com/challenge/9Px2rkc9TPhK54wDb
# All done
ecgsequence = [1,2]
input = 5

def ecg_seq_index(input):
    while not existsin(input):
        main()
    return (ecgsequence.index(input))

def hcf(a, b):
    if (b == 0) and abs(a) != 1: return True, abs(a)
    elif b==0 and abs(a) == 1: return False, 0
    else: return hcf(b, a % b)

def existsin(x):
    if x in ecgsequence: return True
    else: return False

def main():
    for index in range(3,2^64):
        if existsin(index): continue
        elif not existsin(index) and hcf(ecgsequence[-1],index)[1]:
            ecgsequence.append(index)
            return
