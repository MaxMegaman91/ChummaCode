# https://edabit.com/challenge/cBzYRBbBA7gHwKpor


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

def secret_password(inputstring):
    if not inputstring.islower() or not inputstring.isalpha() or len(inputstring) != 9:
        return "BANG! BANG! BANG!"
    inputlist = [inputstring[0:3],inputstring[3:6],inputstring[6:9]]
    inputlist[0] = str(locateletter(inputlist[0][0])) + inputlist[0][1] + str(locateletter(inputlist[0][2]))
    inputlist[1] = inputlist[1][::-1]
    inputlist[2] = str(next_letter(inputlist[2][0])) + str(next_letter(inputlist[2][1])) + str(next_letter(inputlist[2][2]))
    inputlist[0], inputlist[1], inputlist[2] = inputlist[1], inputlist[2], inputlist[0]
    return "".join(inputlist)