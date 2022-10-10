from gtts import gTTS
import os
from mutagen.mp3 import MP3

mytext = input("What is the text you need as speech? ")

if mytext == "clip":
    import pyperclip
    mytext = pyperclip.paste()

file1 = gTTS(text=mytext, lang="en", slow=False)

file1.save("thetext.mp3")

audio = MP3("thetext.mp3")
len = audio.info.length

os.system("vlc thetext.mp3")



