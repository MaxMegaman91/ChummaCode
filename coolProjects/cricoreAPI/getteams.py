from urllib.request import urlopen
from bs4 import BeautifulSoup
import json, os, dicttoxml

def getTeamInfo(teamName):
    players = []
    
    teamName = teamName.lower()
    hyphenedTeam = "-".join(teamName.split())
    URL = f"https://www.iplt20.com/teams/{hyphenedTeam}"
    soup = BeautifulSoup(urlopen(URL).read().decode("utf-8"),"html.parser")

    mydivs = soup.find_all("div", {"class":"ih-p-img"})

    for pimg in mydivs:
        name = pimg.h2.text
        role = pimg.span.text
        imgsrc = pimg.img['src']
        
        playerData = {"name":name,
                      "role":role,
                      "imgsrc":imgsrc}
        
        players.append(playerData)
        
        
    jsond = json.dumps({'teamname':teamName, 'players':players})
    
    with open('data.json', "w") as file:
        file.write(jsond)
    
getTeamInfo("chennai super kings")




