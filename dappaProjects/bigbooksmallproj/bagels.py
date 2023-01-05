import random, os
MAX_DIGITS = 4
MAX_TRIES = 20

def wordle(word, needtobe, b=True):
    for x in needtobe:
        if x in word:
            if needtobe.index(x) == word.index(x):
                b=False
                print("Fermi", end=" ")
            else:
                b=False
                print("Pico", end=" ")
    if b: print("Bagels", end=" ")
    print("\n")

while True:
    
    os.system("cls")
    print("""
I am thinking of a {}-digit number. Try to guess what it is.
Here are some clues:
    When I say:     That means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No digit is correct.

I have thought up a number.
You have {} guesses to get it.""".format(MAX_DIGITS, MAX_TRIES))


    mainNum = list("123457890")
    random.shuffle(mainNum)
    mainNum = "".join(mainNum[:MAX_DIGITS])

    for x in range(MAX_TRIES):
        print("GUESS #{}:".format(x+1))
        guessnum = input("> ")
        if guessnum == mainNum:
            print("You got it!")
            break
        wordle(guessnum, mainNum)
    if guessnum != mainNum:
        print("You lost, the number was {}.".format(mainNum))
    

    if input("Wanna play again? \n> ")[0].lower() != "y":
        break

print("\nThanks for playing! ")
