# https://edabit.com/challenge/MGALfBAXhXqqdFyqo
def atbash(txt):
    txt = [*txt]
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(txt)):
        if txt[i] in alpha:
            txt[i] = alpha[25-alpha.index(txt[i])]
        elif txt[i].lower() in alpha:
            txt[i] = alpha[25-alpha.index(txt[i].lower())].upper()
    return "".join(txt)

def unatbash(txt):
    return atbash(txt)
