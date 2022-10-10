# https://edabit.com/challenge/HXAWjd2Nkj8eAJ2xY
# later :)

def replace(inputstring, changex, changey):
    try: 
        thelist = []
        for x in inputstring:
            thelist.append(x)
        while changex in thelist:
            thelist[thelist.index(changex)] = changey
        return "".join(thelist)
    except: return False


def timeToEat(inputstring):
    time = (replace(replace(inputstring, ".", " "), ":", " ")).split(sep=" ")
    if time[2] == 'p':
        time[0] = str(int(time[0]) + 12)
    returnlist = [0,0]
    mealtimes = [["7","00"],[]]
    return time

print(timeToEat("5:00 p.m."))