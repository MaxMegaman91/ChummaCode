# https://edabit.com/challenge/EWZqYT4QGMYotfQTu


def tap_code(text):
    countlist = []
    anslist = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x in text.split(" "):
        countlist.append(x.count("."))
    print(countlist)
    for x in range(0,len(countlist), 2):
        alphaindex = ((countlist[x]-1)*5 + countlist[x+1])-1
        if alphaindex >= 11: alphaindex-=1
        anslist.append(alphabet[alphaindex])
    print("".join(anslist))

tap_code(". ... .... .. ..... . ... ..... . .")