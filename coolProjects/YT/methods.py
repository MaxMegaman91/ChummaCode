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
    tk.Button(window, text="Download Now", command=video.download(), width=35).pack(side=tk.TOP)


linkInput = tk.Entry(window, width=43)
linkInput.pack(side=tk.TOP)

mybutton = tk.Button(window, text="Submit", command=readInput, width=35)
mybutton.pack(side=tk.TOP)

window.resizable(True, True)

window.mainloop()

