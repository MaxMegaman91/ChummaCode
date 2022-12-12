from mytube import *
from ytmusicapi import YTMusic

yt = YTMusic()


def song_filter(list1, returnlist=[]):
    for x in list1:
        returnlist.append(x["title"]+ ", Explicity: " + str(x["isExplicit"]))
    return returnlist

def artistformat(list1):
    for artist in list1[:-3]:
        string += artist
        string += ", "



while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    search_query= input("Query? ")
    search_results = yt.search(search_query, filter="songs", limit=5)
    # print(search_results)

    titlelist = song_filter(search_results)
    
    for x in range(0, 8):
        print(str(x+1) + ") " + titlelist[x])

    selection = int(input("Which number do you want? "))-1

    selectedDictionary = search_results[selection]
    songname = selectedDictionary["title"]

    artistlist = []
    for artist in selectedDictionary["artists"]:
        artistlist.append(artist["name"])
    songartist = ", ".join(artistlist)

    songalbum = selectedDictionary["album"]["name"]
    songlink = "https://www.youtube.com/watch?v="+selectedDictionary["videoId"]

    print(songname, songartist, songalbum, songlink, sep="\n")


    audioObject = ytAudio(songlink)
    audioObject.download()
    audioObject.metadata(songname, songartist, songalbum, True)
