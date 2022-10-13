from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def retrieveInfo(playerID):
    with open("coolProjects/cricoreAPI/"+str(playerID)+".json", "a") as f:
        f.write("{")

        activityList = ["BATTING", "BOWLING", "FIELDING"]
        for activity in activityList:
            url = "https://hs-consumer-api.espncricinfo.com/v1/pages/player/stats/summary?recordClassId=1&playerId="+str(playerID)+"&type="+str(activity.upper())
            soup = BeautifulSoup(urlopen(url).read().decode("utf-8"),"html.parser")
            jsontext = json.loads(soup.text)["summary"]["groups"][0]["stats"][0]
            f.write("\""+activity + "\":")
            json.dump(jsontext, f)
            if activityList.index(activity) < 2: f.write(",")
            f.write("\n")

        f.write("}")
        return
    

for x in range(99999):
    retrieveInfo(x)
