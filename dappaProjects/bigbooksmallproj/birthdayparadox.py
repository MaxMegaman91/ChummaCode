import datetime, random

def findDuplicates(list1):
    if len(list1) == len(set(list1)):
        return None
    else:
        for a, birthdayA in enumerate(birthdays):
            for b, birthdayB in enumerate(birthdays[a + 1 :]):
                if birthdayA == birthdayB:
                    return birthdayA # Return the matching birthday.

def main():
    ny = datetime.datetime(2001, 1, 1)
    birthdays = []
    for _ in range(int(birthdaysToGenerate)):
        daystoadd = datetime.timedelta(random.randint(0, 364))
        newbd = ny+daystoadd
        birthdays.append(newbd)

    rv = findDuplicates(birthdays)
    return 0 if rv == None else 1

birthdaysToGenerate = 101
while int(birthdaysToGenerate) >= 100 or int(birthdaysToGenerate) < 0:

    birthdaysToGenerate = input("How many birthdays should I generate? (max 100) \n> ")

    if int(birthdaysToGenerate) <= 100 and int(birthdaysToGenerate) > 0:
        break

    print("Retry! \n")

birthdays = []

MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

print("Here are {} birthdays: ".format(birthdaysToGenerate))

ny = datetime.datetime(2001, 1, 1)
for _ in range(int(birthdaysToGenerate)):
    daystoadd = datetime.timedelta(random.randint(0, 364))
    newbd = ny+daystoadd
    birthdays.append(newbd)

    print(MONTHS[int(newbd.strftime("%m"))-1],int(newbd.strftime("%d")), end="")
    if _ != int(birthdaysToGenerate)-1: print(", ", end="")
    else: print()

rv = findDuplicates(birthdays)
if rv != None:
    print("In this simulation, multiple people have a birthday on {} {}".format(MONTHS[int(rv.strftime("%m"))-1], int(rv.strftime("%d"))), end=".\n\n")

print("Generating {} random birthdays 100,000 times...".format(birthdaysToGenerate))
input("Press Enter to begin! ")
print("Lets run another 100,000 simulations... ")
score = 0
for _ in range(100000):
    if _ % 10000 == 0:
        print(_,"simulations run...")
    score += main()


print("100000 simulations run.")
print("""
Out of 100,000 simulations of {} people, there was a
matching birthday in that group {} times. This means
that {} people have a {} % chance of
having a matching birthday in their group.
That's probably more than you would think!
""".format(birthdaysToGenerate, score, birthdaysToGenerate, score/1000))







