from urllib.request import urlopen
from bs4 import BeautifulSoup
import json, os, dicttoxml

def gettext(url):
    soup = BeautifulSoup(urlopen(url).read().decode("utf-8"),"html.parser")
    jsontext = json.loads(soup.text)
    return jsontext

def playerInfo(playerID, savePath="C:/Users/aarus/fetch/", saveFile=True):
    try:
        with open(savePath+str(playerID)+".json" if saveFile==True else str(saveFile), "a") as f:
            f.write("{")
            
            for activity in ["BATTING", "BOWLING", "FIELDING"]:
                f.write("\""+activity + "\":")
                json.dump(gettext("https://hs-consumer-api.espncricinfo.com/v1/pages/player/stats/summary?recordClassId=1&playerId="+str("{number:06}".format(number=playerID))+"&type="+str(activity.upper())), f)
                if activity != "FIELDING": f.write(",")
                f.write("\n")

            f.write("}")
            return
    except:
        return
    
def matchInfo(matchID, savePath="C:/Users/aarus/fetch/", saveFile=True):
    try:
        with open(savePath+str(matchID)+".json" if saveFile==True else str(saveFile)+".json", "a") as file:
            file.write("{")

            jsontext = gettext("https://hs-consumer-api.espncricinfo.com/v1/pages/match/overs/details?lang=en&seriesId=1298134&mode=ALL&matchId="+str(matchID))
            for inning in jsontext["inningOvers"]:
                file.write("\"inning" + str(inning["inningNumber"]) + "\" : {")
                for over in inning["stats"]:
                    for ball in over["balls"]:
                        file.write("\"ball" + str(ball["oversUnique"]) + "\": ")
                        json.dump(ball, file)
                        file.write("" if over["balls"][-1]==ball and inning["stats"][-1] == over else ",")
                
                file.write("}," if inning["inningNumber"]==1 else "}")
            file.write("}")
    except KeyError:
        print("Something wrong with matchID json data! ")
    except: print("Match ID error!")

def teamInfo(teamID, getIndividualPlayerData=False, saveFile=True):
    jsontext = gettext("https://hs-consumer-api.espncricinfo.com/v1/pages/player?teamId="+str(teamID))
    teamname = str(jsontext["content"]["team"]["name"])

    try: os.mkdir(os.path.join("/home/aarush/cricorehard/teamData/", teamname)) 
    except OSError: pass

    with open("/home/aarush/cricorehard/teamData/"+teamname+"/"+teamname+".json" if saveFile==True else str(saveFile), "a") as file:
        json.dump(jsontext["content"]["players"]["results"], file)
        
    if getIndividualPlayerData:
        for player in jsontext["content"]["players"]["results"]:
            playerInfo(player["id"], saveFile="/home/aarush/cricorehard/teamData/"+teamname+"/"+player["longName"]+".json")

def jsonToXML(jsonFilePath, onDebug=False, deleteJSON=False):

    with open(jsonFilePath, "r") as file: 
        data = json.load(file)

    if onDebug: print(data)

    xml = dicttoxml.dicttoxml(data)
    
    if onDebug: print(xml)
    
    with open(jsonFilePath[:-4]+"xml", "w") as file:
        file.write(xml.decode("utf-8"))
    
    if deleteJSON:
        os.remove(jsonFilePath)
    

# jsonToXML("/home/aarush/ChummaCode/getcloth.json")