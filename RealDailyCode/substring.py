# https://edabit.com/challenge/RB6iWFrCd6rXWH3vi
# No Edits Allowed

def longest_substring(substring):
    isprevodd = "None"
    numberlist = []
    finallist = []

    def isodd(testingnumber):
        if testingnumber % 2 == 1:
            return True
        elif testingnumber % 2 == 0:
            return False

    def listtoint(lst):
        s = [str(i) for i in lst]
        return "".join(s)

    for substringindex in substring:
        if isodd(int(substringindex)) == isprevodd:
            finallist.append(listtoint(numberlist))
            numberlist.clear()
        isprevodd = isodd(int(substringindex))
        numberlist.append(int(substringindex))

    if len(numberlist) != 0:
        finallist.append(listtoint(numberlist))
        numberlist.clear()
            
    #print("The number given was:", substring)
    #print("These are the substrings:", finallist)
    largestsub = max(finallist, key = len)
    #print("The first largest substring is:", str(largestsub))
    return largestsub