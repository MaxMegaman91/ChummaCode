# https://edabit.com/challenge/Pa2rHJ6KeRBTF28Pg

person = {
  "name": "Mickey",
  "surname": "Mouse",
  "gender": "M",
  "dob": "16/1/1928"
}

theletterdict = {
    1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "H", 
    7: "L", 8: "M", 9: "P", 10: "R", 11: "S", 12: "T"
}

def is_vowel(x):
    vowel_list = ["a", "e", "i", "o", "u"]
    if x.lower() in vowel_list: return True
    elif x.lower() not in vowel_list: return False

def consonants(input1):
    returnlist = []
    for x in input1:
        if not is_vowel(x): returnlist.append(x)
    return returnlist

def vowels(input):
    returnlist = []
    for x in input:
        if is_vowel(x): returnlist.append(x)
    return returnlist

def surname(surname):
    if len(surname) <= 2: return str(consonants(surname)[0] + vowels(surname)[0] + "X").upper()
    elif len(consonants(surname)) < 3: return str("".join(consonants(surname)) + "".join(vowels(surname)))[0:3].upper()
    else: return "".join(consonants(surname)[0:3]).upper()

def name(name):
    if len(name) <= 2: return str(consonants(name)[0] + vowels(name)[0] + "X").upper()
    elif len(consonants(name)) < 3: return str("".join(consonants(name)) + "".join(vowels(name)))[0:3].upper()
    elif len(consonants(name)) == 3: return "".join(consonants(name)).upper()
    else: return ("".join(consonants(name)[0])+"".join(consonants(name)[2:4])).upper()


def dob(dob,gend):
    thedmy = dob.split('/')
    if len(thedmy[0]) == 1: thedmy[0] = "0"+thedmy[0]
    if gend == "M":
        return thedmy[2][2:4] + theletterdict[int(thedmy[1])] + thedmy[0]
    elif gend == "F":
        return thedmy[2][2:4] + theletterdict[int(thedmy[1])] + str(int(thedmy[0]) + 40)

def fiscalCode(identification):
    return surname(identification["surname"])+name(identification["name"])+dob(identification["dob"],identification["gender"])
