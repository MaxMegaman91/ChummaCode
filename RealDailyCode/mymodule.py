# No problem, just to help with future codes

def locateletter(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if x in alphabet:
        return alphabet.index(x) + 1
    else: return False

def next_letter(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if x in alphabet:
        return alphabet[locateletter(x)]
    else: return False

def factors_of(x):
    mylist = []
    for index in range(1,x/2+1):
        if x % index == 0: mylist.append(index)
    mylist.append(x)
    return mylist

def replace(inputstring, changex, changey):
    try: 
        thelist = []
        for x in inputstring: thelist.append(x)
        while changex in thelist: thelist[thelist.index(changex)] = changey
        return "".join(thelist)
    except: return False


