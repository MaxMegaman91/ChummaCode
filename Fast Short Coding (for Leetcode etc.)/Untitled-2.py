import random

winrate = 0
history = []
guesspwr = 1

while True:
    rpsinput = input("Rock, Paper, or Scissors? ").lower()
    pull = random.choice(["r","p","s"])
    print()