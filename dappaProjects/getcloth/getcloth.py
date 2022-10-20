SAVE_PATH = "/home/aarush/ChummaCode/dappaProjects/getcloth/"
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json, datetime

now = datetime.datetime.now()

def get_weather(hourrange=7, location=False):

    # format = [temp {Value, Unit, UnitType}, feeltemp {Value, Unit, UnitType, Phrase}, boolPrecip, 
    # preciptype (str), precipIntense (str), [rainprob, snowprob, iceprob] (int)], 
    # [snow {value, Unit, UnitType}, ice{value, Unit, UnitType}], CloudCover (int)
    # (prob=probability)

    tempList = []

    weather = json.loads(BeautifulSoup(urlopen("http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/55487?apikey=%09Kt8Yf7YHg1RhjCGCBaVuRlf2kvQFPJzA&language=en-us&details=true&metric=true").read().decode("utf-8"), "html.parser").text)
    neededWeather = weather[:hourrange]

    with open(SAVE_PATH + "getcloth.json", "w") as f: f.write(str(weather))

    for weatherByHour in neededWeather:
        toAppend = [weatherByHour["Temperature"], weatherByHour["RealFeelTemperature"], weatherByHour["HasPrecipitation"]]
        if weatherByHour["HasPrecipitation"]: toAppend += [weatherByHour["PrecipitationType"], weatherByHour["PrecipitationIntensity"]]
        toAppend +=  [[weatherByHour["RainProbability"], weatherByHour["SnowProbability"], weatherByHour["IceProbability"]], [weatherByHour["Snow"], weatherByHour["Ice"]], weatherByHour["CloudCover"]]
        tempList.append(toAppend)
    return tempList

class Laundry():
    def __init__(self, belongsToName="Aarush", selfImport=True):
        self.name = belongsToName
        if selfImport:
            with open(SAVE_PATH+"extract.txt", "w") as extractfile:
                pass

class cloth():
    def __nit__(self):
        pass


print(get_weather())
#   view-source:https://weather.com/en-CA/weather/hourbyhour/l/584018bec07ce9573837c14fa59da031fa6fcdeb1c3c9e3b2b27cb79ce254b5a