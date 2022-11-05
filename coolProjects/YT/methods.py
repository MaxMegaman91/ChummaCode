from mytube import *
import tkinter as tk
from urllib.request import urlopen
import io, base64


window = tk.Tk()

window.geometry("500x200")

def readInput():
    global link
    link = linkInput.get()
    video = ytVideo(link)

    i = 2
    for item in video.info():
        tk.Label(window, text=str(item)).pack(side=tk.TOP)
        i += 1
    
    Streams = []
    StreamResolutions = []
    AudioStreams = []

    for x in video.object.streams.filter(mime_type="video/mp4"):
        if x.resolution not in StreamResolutions:
            Streams.append(x)
            StreamResolutions.append(x.resolution)

    for x in video.object.streams.filter(mime_type="video/mp4", progressive=False):
        if x.resolution not in StreamResolutions:
            Streams.append(x)
            StreamResolutions.append(x.resolution)

    for x in video.object.streams.filter(only_audio=True):
        AudioStreams.append(x)
    
    del StreamResolutions

    Streams = sortStreamsByKey(Streams,"resolution")
    print(Streams)

    AudioStreams = sortStreamsByKey(AudioStreams, "abr")
    print(AudioStreams)

    RealOptions = [x.resolution for x in Streams]+[x.abr for x in AudioStreams]

    variable = tk.StringVar(window)
    variable.set(RealOptions[0]) # default value

    w = tk.OptionMenu(window, variable, *RealOptions)
    w.pack(side=tk.TOP, padx=5, pady=10)

    print(variable.get())

    tk.Button(window, text="Download Now", command= lambda: video.download(variable.get()), width=35).pack(side=tk.TOP, padx=5, pady=10)


def sortStreamsByKey(streamsList, key):
    import operator
    streamsList.sort(key=operator.attrgetter(key))
    return streamsList


linkInput = tk.Entry(window, width=60)
linkInput.pack(side=tk.TOP)

mybutton = tk.Button(window, text="Submit", command=readInput, width=50)
mybutton.pack(side=tk.TOP)

window.resizable(True, True)

window.mainloop()

