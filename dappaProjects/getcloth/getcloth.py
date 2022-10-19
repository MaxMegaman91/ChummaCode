from urllib.request import urlopen
from bs4 import BeautifulSoup
import os, sys, json

def getlink(url):
    soup = BeautifulSoup(urlopen(url).read().decode("utf-8"),"html.parser")
    jsontext = json.loads(soup.text)