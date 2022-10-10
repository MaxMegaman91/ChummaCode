"""nums = [3,2,11,1]
removeQueries = [3,2,1,0]
availablenums = [0,1,2,3]

for remove in removeQueries:
    nums[remove] = "0"
    availablenums.remove(availablenums[remove])
"""
"""import os, time

class Car():
    def __init__(self,model,color,maxspeed):
        self.model, self.color, self.maxspeed = model, color, maxspeed
        self.curspeed = 0
        self.distance = 0
    
    def accelerate(self,speed):
        self.curspeed += speed
        if self.curspeed >= self.maxspeed:
            self.curspeed = self.maxspeed
            print("Car at max speed of {}.".format(self.curspeed))
            return
        print("Car traveling at {}kmph. ".format(self.curspeed))
        self.distance += self.curspeed
    
    def decelerate(self,speed):
        self.curspeed -= speed
        if self.curspeed <= 0:
            self.curspeed = 0
            print("Car stopped!")
            return
        print("Car traveling at {}kmph. ".format(self.curspeed))
        self.distance += self.curspeed

os.system('cls' if os.name == 'nt' else 'clear')
mycar = Car(input("What car model would you like? --> "), input("What car color would you like? --> "), int(input("What is the max speed of the car? --> ")))
carlist = [mycar]
carnum = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("================================================================")
    action = input("What to do? accel/brake --> ")
    if action == "accel":
        by = int(input("by what amount? --> "))
        carlist[carnum].accelerate(by)
    elif action == "brake":
        by = int(input("by what amount? --> "))
        carlist[carnum].decelerate(by)
    elif action == "info":
        print("Your {} {} car is travelling at {}kmph. It has traveled {} kms.".format(carlist[carnum].color, carlist[carnum].model, carlist[carnum].curspeed, carlist[carnum].distance))
        time.sleep(5)
    elif action == "newcar":
        carlist.append(Car(input("What car model would you like? --> "), input("What car color would you like? --> "), int(input("What is the max speed of the car? --> "))))
        carnum = int(input("Which number car? {} cars are available. -->".format(len(carlist))))-1
    elif action == "changecar":
        carnum = int(input("Which number car? {} cars are available. --> ".format(len(carlist))))-1
    time.sleep(5)"""

"""import clipboard, time
while True:
    time.sleep(5)
    print("GOING!")
    time.sleep(1)
    text = clipboard.paste()
    clipboard.copy(text[0:-3])  # now the clipboard content will be string "abc"
    print("Done")

import sys, pygame
from pygame.locals import *

pygame.init()

size = width, height = 1585, 865
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("C:/Users/aarus/Downloads/ball.png")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    if ballrect.x == 500:speed[0] = 0

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()"""
