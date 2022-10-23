# Pls reprogram this
# Debug mode... requires more integration towards code
DEBUG = False
# Importing all Modules
from pytube import YouTube
from moviepy.editor import *
import time 
import os
import sys

##############################################################################################################################
# CPU Thread count depending on the os
availableThreads = 16 if os.name == "posix" else 32
theofficialqual = 0

# Resolutions
resolution = {
    "8k": "4320p",
    "4k": "2160p",
    "uhd": "1440p",
    "hd": "1080p",
    "sd": "720p",
    "mp3": "mp3",
    "aud": "aud",
    "usd": "360p"
}

# The place where videos are downloaded to
SAVE_PATH = "/home/aarush/Downloaded_Youtube" if os.name == "posix" else "C:/Users/aarus/Downloaded_Youtube"


################################################################################################################

def getFileCount(dir_path=r"C:/users/aarus/Downloaded_Youtube"):
    return int(len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))]))


# edits the mp3 info by title, artist, album, and lyrics API
def info_of_mp3(title, artist, album, wantlyrics, filenamefull):
    from mutagen.id3 import ID3, TIT2, TALB, TPE1, USLT
    audio = ID3(SAVE_PATH+"/"+filenamefull)
    
    audio.add(TIT2(encoding=3, text = title))    #TITLE
    audio.add(TPE1(encoding=3, text = artist))    #ARTIST
    audio.add(TALB(encoding=3, text = album))    #ALBUM

    if wantlyrics:
        lyrics = getLyrics(title + " by " + artist)
        audio.add(USLT(encoding=3, text = lyrics))

    audio.save(v2_version=3)

# lyrics API
def getLyrics(searchquery):
    from lyrics_extractor import SongLyrics
    extract_lyrics = SongLyrics("AIzaSyCAs1m8rklE3vYfyryY25u-gD7JuNhPlKs", "51f3092772c0347b5")
    lyricdict = extract_lyrics.get_lyrics(searchquery)
    return lyricdict["lyrics"]

# Converts mp4 to mp3 when requested final product is mp3 
def mp4_to_mp3(mp4, mp3):
    mp4_without_frames = AudioFileClip(SAVE_PATH+"/"+mp4)
    mp4_without_frames.set_duration(yt.length)
    mp4_without_frames.write_audiofile(SAVE_PATH+"/"+mp3)
    mp4_without_frames.close()
    os.remove(SAVE_PATH+"/"+mp4)

# root download function
def download_by_itag(itag, finalname):
    global yt, SAVE_PATH, name
    try:
        # downloading the video
        yt.streams.get_by_itag(itag).download(output_path=SAVE_PATH, filename=finalname)
    except:
        print("An error occured while trying to download the video/audio!")
        sys.exit("Download error")

# combines a video and audio file for higher quality video files
def combine_audio_video(audiofile, videofile, output_file_name_with_extension):
    videoclip = VideoFileClip(SAVE_PATH+"/"+videofile)
    audioclip = AudioFileClip(SAVE_PATH+"/"+audiofile)
    video = videoclip.set_audio(audioclip)
    video.write_videofile(str(SAVE_PATH+"/"+output_file_name_with_extension), fps=60, threads=availableThreads, codec = "libfdk_aac")
    while True: ### check if audio and video files are closed to delete them
        try:
            myfile = open(f'{SAVE_PATH}/{videofile}', "r+")
            myfile.close()
            os.remove("C:/Users/aarus/Downloaded_Youtube/tempaud.mp4")
            os.remove("C:/Users/aarus/Downloaded_Youtube/tempvid.mp4")
            break                             
        except IOError:
            pass

# locate link and set yt to a class with the link
def findlink(link):
    global yt, name
    # Find video and attach object as variable yt
    print("Finding link: " + link)
    try:
        yt = YouTube(link)
    except:
        print("Not able to find link!")
        sys.exit("LINK NOT FOUND!")
    if name == "":
        name = validFilename(yt.title)
    info()

# replace string invalid characters to make a valid filename
def validFilename(x):
    thelist=[]
    for letter in x:
        if letter in "abcdefghijklmnopqrstuvwxyz_ ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-":
            thelist.append(letter)
    return "".join(thelist).strip()

# download a file with quality input accessing yt object
def download_with_qual(qual, finalname):
    global theofficialqual
    theofficialqual = qual
    try:
        if qual != "sd" and qual != "mp3" and qual != "aud" and qual != "usd":
            viditag = yt.streams.filter(res=resolution[qual], mime_type="video/mp4", progressive=False).first().itag
            auditag = yt.streams.filter(mime_type="audio/mp4").get_audio_only().itag
            print("Downloading video!\n")
            download_by_itag(viditag, "tempvid.mp4")
            print("Downloaded video!\n")
            print("Downloading audio!\n")
            download_by_itag(auditag, "tempaud.mp4")
            print("Downloaded audio!\n")
            print("Starting combine!\n")
            combine_audio_video("tempaud.mp4", "tempvid.mp4",finalname+".mp4")
        elif qual == "sd":
            itagofthehighestres = yt.streams.filter(progressive=True).get_highest_resolution().itag
            print("Downloading " + qual + " quality of " + ytTitle)
            download_by_itag(itagofthehighestres, finalname+".mp4")
        elif qual == "usd":
            itagofthehighestres = yt.streams.filter(res="360p",progressive=True).get_highest_resolution().itag
            print("Downloading " + qual + " quality of " + ytTitle)
            download_by_itag(itagofthehighestres, finalname+".mp4")
        elif qual == "aud" or qual == "mp3":
            auditag = yt.streams.filter(mime_type="audio/mp4").get_audio_only().itag
            print("Downloading " + qual + " quality of " + ytTitle)
            download_by_itag(auditag, "tempaud.mp4")
            mp4_to_mp3("tempaud.mp4", finalname+".mp3")    
        print("Product installed!\n")
    
    except AttributeError: print("Attribute Error raised: I think you chose a quality not available!")
            
# print info to make sure the right link was obtained
def info():
    global ytTitle
    # Print info
    enter = "\n"
    print("Video Title: " + yt.title, enter)
    print("Video Author: "+ yt.author, enter)
    print("Video total views: "+ str(yt.views), enter)
    print("Video length: " + str(yt.length//60) + ":" + str(yt.length%60), enter)
    print("Age Restriction: " + str(yt.age_restricted))
    print("Description Below\n\n\n", yt.description)
    ytTitle = yt.title
    # Print all streams
    for x in yt.streams.filter():
        print(x) # must decode all itags and attributes to neater space

################################################################################################################
# Login and password information

"""import getpass
os.system('cls' if os.name == 'nt' else 'clear')
login = getpass.getpass(prompt='Login: ', stream=None)
pasw = getpass.getpass(prompt='Password: ', stream=None)
if login != "greatestloser" or pasw != "!g0t$2":
    os.exit("Bad info! ")"""

################################################################################################################
# Main loop
while True:
    name = ""

    os.system('cls' if os.name == 'nt' else 'clear')

    print("==========================================================================================")
    textinput = input("What mode of installing (txt, mp3, emp3, or <Enter> for link input): -->  ") # link of the video

    # If we are reading the txt file
    if textinput == "txt":
        print("==========================================================================================")
        print("Reading file!" + "\n\n")

        # Read the text file
        with open("/home/aarush/ChummaCode/coolProjects/YT/the.txt", "r") as f:
            mylist = [line.rstrip('\n') for line in f]
            mylist = mylist[2:]
        
        # and read line by line
        for line in mylist:
            link, quality, *extraStuff = line.split("|")

            # if the quality is not mp3, download with quality
            if quality != "mp3" or quality != "aud":
                findlink(link) # Split each line by the | sign, then find the link associated
                download_with_qual(quality, name) # download with the quality on the other side of the |

            # if the quality is mp3, then download and edit metadata
            else:
                link, quality, name, arti, albm, wlry, *extraStuff= extraStuff
                findlink(link)
                download_with_qual(quality, name)
                info_of_mp3(name, arti, albm, wlry, name+".mp3")

    # install mp3 and edit metadata     
    elif textinput == "mp3":
        textinput = input("Give your inputs (link|qual|name|artist|albm|wlry)! ")
        link, quality, name, arti, albm, wlry, *extraStuff= textinput.split("|")
        findlink(link)
        download_with_qual(quality, name)
        info_of_mp3(name, arti, albm, wlry, name+".mp3")
    
    # install mp3 and edit metadata (gathering inputs separately)
    elif textinput == "emp3":
        link = input("What is the link: ")
        quality = input("What is the quality: ")
        name = input("What is the name: ")
        arti = input("What is the artist: ")
        albm = input("What is the album: ")
        wlry = input("Would you like lyrics (1 for true, 0 for false): ")
        findlink(link)
        download_with_qual(quality, name)
        info_of_mp3(name, arti, albm, wlry, name+".mp3")
    
    elif textinput == "cleanup->":
        if os.name == "posix": os.exit()
        import pyautogui, time
        pyautogui.press("win")
        time.sleep(1)
        pyautogui.write("Itunes")
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(10)
        with pyautogui.hold("ctrl"): pyautogui.press("o")
        time.sleep(1)
        pyautogui.click(x=1748, y=474)
        with pyautogui.hold("ctrl"): pyautogui.press("a")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.moveTo(1910, 180)
        pyautogui.mouseDown(button="left")
        pyautogui.moveTo(1910, 970)
        pyautogui.mouseUp(button='left')
        time.sleep(1)
        pyautogui.click(1180, 980)
        for x in range(getFileCount()-1):pyautogui.hotkey('shift', 'up')
        time.sleep(1)
        pyautogui.click(30,67)
        pyautogui.moveTo(68,441,1)
        time.sleep(0.25)
        pyautogui.moveTo(489,448,0.25)
        pyautogui.moveTo(495,519,0.25)
        pyautogui.click()
        time.sleep(getFileCount()*7)
        pyautogui.press("del")
        pyautogui.click(276,102)
        pyautogui.click(1683,981)
        time.sleep(10)


                
    # else if we are downloading only one
    elif textinput == "":
        textinput = input("Give me a youtube link: ")

        findlink(textinput) # Find the link associated yt vid
        itagtouse = input("What quality or itag would you like? -->  ") # Gathering the itag we require

        if itagtouse == "": # Auto download highest progressive source
            itagtouse = yt.streams.filter(progressive=True).get_highest_resolution().itag
            download_by_itag(itagtouse, name)

        elif (itagtouse in resolution.keys()): # Download with quality input (eg. 4k, hd, uhd, sd, mp3, aud)
            download_with_qual(itagtouse,name)

        elif len(itagtouse.split("&")) == 2: # Download 2 custom itags and combine
            viditag, auditag = itagtouse.split("&")
            print(viditag)
            print(auditag)
            print("Downloading video...")
            download_by_itag(viditag, "tempvid.mp4")
            print("Downloading audio...")
            download_by_itag(auditag, "tempaud.mp4")
            print("Combining...")
            combine_audio_video("tempaud.mp4", "tempvid.mp4",name+".mp4")
            print("Product installed and file ready!\n")

        elif itagtouse[0:5] == "itag:": # specify certain itag
            itagtouse == itagtouse[6:]
            download_by_itag(itagtouse, name)
    
    # cleanup
    print("All done and finished! \n")
    time.sleep(5)
################################################################################################################