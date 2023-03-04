import random, time
import pyautogui as gui
import requests
from bs4 import BeautifulSoup

def searchRandom():
    topicList = []

    get = requests.get("https://twitter-trends.iamrohit.in/canada")
    # print(get.text)
    soup = BeautifulSoup(get.text, 'html.parser')
    for topic in soup.find_all('a', class_='tweet', target='_blank'):
        topicList.append(topic.get_text())
        
    gui.keyDown('ctrl')
    gui.press('t')
    gui.keyUp('ctrl')

    time.sleep(1)
    gui.typewrite("message")
    gui.press('enter')
    
    time.sleep(2)
    gui.FAILSAFE = True
    x = 0
    while x < 31:
        topic = random.choice(topicList)
        topicList.remove(topic)
        gui.click(277, 174, clicks=3, interval=0.1)
        time.sleep(0.5)
        gui.typewrite(topic)
        gui.press('enter')
        time.sleep(2)
        x+= 1



def dailySet():
    gui.press('win')
    gui.typewrite("edge")
    gui.press('enter')
    
    time.sleep(2)
    gui.typewrite("https://rewards.bing.com/     ")
    gui.press('enter')
    
    time.sleep(2)
    
    gui.keyDown('ctrl')
    gui.click(492, 900)
    time.sleep(0.5)
    gui.click(1118, 900)
    time.sleep(0.5)
    gui.click(1533, 900)
    
    gui.keyUp('ctrl')
    
    gui.keyDown('ctrl')
    gui.press("4")
    time.sleep(0.5)
    gui.click(1142, 865)
    time.sleep(2)
    gui.press('w', 3, 0.5)
    gui.keyUp('ctrl')
    time.sleep(2)
    
    gui.keyDown('ctrl')
    gui.press('r')
    gui.keyUp("ctrl")

def searchNewsMobile():
    time.sleep(2)
    
    gui.keyDown('ctrl')
    gui.press('w')
    time.sleep(1)
    gui.press('t')
    gui.keyUp('ctrl')
    
    time.sleep(1)

    gui.typewrite("https://www.bing.com/search?q=popular%20now%20on%20bing&filters=segment:%22popularnow.carousel%22&form=ml10ns&crea=ml10ns")
    gui.press('enter')
    time.sleep(1)
    
    gui.press('f12')
    
    time.sleep(2)
    gui.keyDown('ctrl')
    time.sleep(0.5)
    gui.press('r')
    gui.keyUp('ctrl')
    time.sleep(2)
    
    for x in range(22):
        gui.click(632, 537)
        time.sleep(2)
        

dailySet()
input("Do the other extra point bonuses and press enter -> ")
searchRandom()
searchNewsMobile()
"""
[
        "how to play subway surfers", 
        "how to do microsoft rewards",
        "how to search on bing",
        "how to use jet dry on dishwasher",
        "skateboarding tutorial",
        "arts and crafts new",
        "xbox game pass news",
        "telescopes cheap",
        "wimpy kid movie 2022",
        "hot wheels sets new 10 old",
        "what plants best for indoor",
        "is amazon stock a good first stock",
        "minions game on ipad",
        "how to sing acapella",
        "hamilton beach not working",
        "cricket world cup 2023",
        "world cup winners 2022",
        "wordle today",
        "wordle answer hacker",
        "wordle helper",
        "what modifications to wordle",
        "is chess.com trustable",
        "battle cats download",
        "office e01",
        "spiderman new movie 2023",
        "covid19 rates",
        "covid19 vaccine rates in Sascatchewan",
        "Tommy Hilfiger stock",
        "ac4 legendary ships",
        "minecraft how to mine bedrock",
        "crafts and arts today",
        "what should i make for food",
        "where is google ceo now",
        "why is everyone being laid"
    ]"""   