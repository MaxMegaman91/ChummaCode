SAVE_PATH = "/home/aarush/ChummaCode/dappaProjects/getcloth/"
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os, sys, json

def getlink(url):
    soup = BeautifulSoup(urlopen(url).read().decode("utf-8"),"html.parser")
    return soup

webhtml = getlink("https://weather.com/en-CA/weather/hourbyhour/l/584018bec07ce9573837c14fa59da031fa6fcdeb1c3c9e3b2b27cb79ce254b5a")
for t in webhtml.find_all("script"):
    if str(t).find("window.__data=JSON.parse") != -1:
        with open(SAVE_PATH+"getcloth.txt", "w") as f:
            f.write(str(t.text).replace("\\\"", "\""))

#   view-source:https://weather.com/en-CA/weather/hourbyhour/l/584018bec07ce9573837c14fa59da031fa6fcdeb1c3c9e3b2b27cb79ce254b5a