import random, time
import pyautogui as gui

gui.FAILSAFE = True
x = 0
while x < 100:
    topic = random.choice([
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
    ])
    
    gui.click(277, 174, clicks=3, interval=0.1)
    """time.sleep(0.5)
    gui.keyDown('ctrl')
    gui.keyDown('a')
    gui.keyUp('a')
    gui.keyUp('ctrl')"""
    time.sleep(0.5)
    gui.typewrite(topic)
    gui.press('enter')
    time.sleep(5)
    x+= 1
    