import pyautogui as pg
import time
 
def openapp(theappname):
    pg.press(["win"])
    pg.typewrite(theappname)
    time.sleep(3)
    pg.press(["enter"])
    time.sleep(3)

def opensongs():
    pg.click(963,307,duration=0.5)
    pg.keyDown("ctrl")
    pg.press("o")
    pg.keyUp("ctrl")
    pg.click(963,307,duration=0.5)
    pg.keyDown("ctrl")
    pg.press("a")
    pg.keyUp("ctrl")
    pg.press(["enter"])

def convert_to_aac(length):
    length = int(length)
    length *= 5
    pg.keyDown("ctrl")
    pg.press("a")
    pg.keyUp("ctrl")
    pg.moveTo(25,67,duration=1)
    pg.click()
    pg.moveTo(118,443,duration=1)
    pg.moveTo(419,443,duration=0.5)
    pg.moveTo(462,522,duration=0.5)
    pg.click()
    time.sleep(length)
    pg.keyDown("shift")
    pg.press("delete")
    pg.keyUp("shift")

def addtophone(): 
    #not done yet, song length changes location of the three dots, so must use ctrl-a and double click
    pg.click()
    pg.keyDown("ctrl")
    pg.press("a")
    pg.keyUp("ctrl")
    pg.moveTo(568,165,duration=0.5)
    pg.click(button='right')
    pg.moveTo(616,207,duration=0.5)
    pg.moveTo(915,202,duration=0.5)
    pg.click()




def exporttophone(songs):
    time.sleep(5)
    openapp("itunes")
    opensongs()
    convert_to_aac(songs)
    addtophone()

exporttophone(0)