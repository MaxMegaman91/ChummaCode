from mytube import *
import tkinter as tk
from urllib.request import urlopen
import io, base64


window = tk.Tk()

window.geometry("700x700")

def readInput():
    global link
    link = linkInput.get()
    video = ytVideo(link)

    i = 2
    for item in video.info():
        tk.Label(window, text=str(item)).grid(row=i,column=1, sticky="")
        i += 1
    
    Streams = []
    StreamResolutions = []
    AudioStreams = []

    for x in video.object.streams.filter(mime_type="video/mp4"):
        if x.resolution not in StreamResolutions:
            StreamResolutions.append(x.resolution)
    
    sortStreamsByKey(StreamResolutions)

    """for x in video.object.streams.filter(mime_type="video/mp4", progressive=False):
        if x.resolution not in StreamResolutions:
            StreamResolutions.append(x.resolution)

    AudioStreams = video.object.streams.filter(mime_type="audio/mp4").get_audio_only()

    StreamResolutions.append(AudioStreams.abr)"""

    variable = tk.StringVar(window)
    variable.set(StreamResolutions[0]) # default value

    w = tk.OptionMenu(window, variable, *StreamResolutions)
    w.grid(row=i,column=1, sticky="")
    i+=1

    print(variable.get())

    tk.Button(window, text="Download Video", command= lambda: video.download(quality=variable.get()), width=35).grid(row=i, column=1, sticky="")
    tk.Button(window, text="Download Audio", command= lambda: AudioDownload(link), width=35).grid(row=i+1, column=1, sticky="")

def AudioDownload(link):
    audio = ytAudio(link)
    audio.download()
    del audio


def sortStreamsByKey(streamsList):
    for x in range(len(streamsList)):
        streamsList[x] = streamsList[x][:-1]
    
    streamsList.sort(key=int, reverse=True)

    for x in range(len(streamsList)):
        streamsList[x] += "p"



linkInput = tk.Entry(window, width=60)
linkInput.grid(row=0, column=1, sticky="")

mybutton = tk.Button(window, text="Submit", command=readInput, width=50)
mybutton.grid(row=1, column=1, sticky="")

window.resizable(False, False)

window.mainloop()

