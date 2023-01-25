# ------------------------       khplayer.py       ------------------------
# ----- imports -----
import socket, threading, sys
from tkinter import *

# ----- constants -----
if len(sys.argv) <= 1:
    SERVER = "192.168.2.120"
    PORT = 14014
elif len(sys.argv) > 1:
    SERVER, PORT = sys.argv

del sys

HEADER = 64
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "%DISCONNECT"
FONTS = {"title":("DejaVu Sans", 24, "bold"), 
         "heading":("Droid Sans Fallback", 16), 
         "text":("Droid Sans Fallback", 12),
         "button":("Loma", 12)}

# Game data
name = ""
ranking = 2^63
answerstr = ""
points = 0

# Create a GUI app
app = Tk()

# Class for collection of widgets
class Page():
    def __init__(self, *args, nextPage=None):
        """With arrays of [widget, col, row, padx, pady], a Page instance is created.
        A collection of widgets that make a view page.
        
        .state is either isHiding or isShowing to know if its showing or not
        .show() shows the page
        .hide() hides the page 
        .goNextPage() switches page
        .toggle() switches between hide/show
        
        Returns None
        """
        
        self.widgets = list(args) # list of multiple [widget, col, row, padx, pady]
        self.state="isHiding" 
        self.nextPage=nextPage 
        return

    def show(self, *_):
        """Shows the app page by gridding the widgets."""
        
        for widget, col, row, padx, pady in self.widgets: # unpack lists to widget col row padx pady
            widget.grid(column=col, row=row, padx=padx, pady=pady)
            
        self.state="isShowing"
    
    def hide(self, *_):
        """Hides the page by widget.grid_remove()"""
        
        for widget, *xtras in self.widgets:
            remove(widget)
            
        self.state="isHiding"
        
    
    def goNextPage(self, nextPage=None, *_):
        """Faster function to switch between pages

        Args:
            nextPage (Page, optional): The page to switch to. Defaults to self.nextPage
        """
        self.hide() #hide current
        
        if nextPage: # if input given
            nextPage.show()
            
        elif self.nextPage: #if nextpage 
            self.nextPage.show()
            
        return
        
    def toggle(self, *_):
        """Toggle the page on/off."""
        
        if self.state == "isHiding":
            self.show()
            
        elif self.state == "isShowing":
            self.hide()

# Creating a function for removing widgets from grid
def remove(input):
    """Removes a widget or a list of widgets from the grid

    Args:
        input (list or Widget): Gridded widget or list of widgets to un-grid

    Returns:
        bool: Successfulness
    """
    if type(input) != list: # Hopefully widget
        try: input.grid_remove()
        except: return False
        
    elif type(input) == list: # Go through and delete in list
        for widget in input:
            remove(widget)
            
    return True


def login(loginPage:Page):
    """Transition between loginpage and waitpage

    Args:
        loginPage (Page): loginPage
    """
    global name
    name = loginPage.widgets[1][0].get()
    
    loginPage.goNextPage()

def answer(answer:str):
    """Transition between answerPage and waitPage

    Args:
        answer (str): uses answer input -> send to globals -> sends to server"""
    
    global answerstr
    
    answerstr = answer
    print(f"Answer submitted: {answer}")

def sendMsg(client, msg):
    """Sends a string message from the player to the server

    Args:
        client (socket): socket object representing connection between server and player
        msg (string): message to send"""
    
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)

def requestsManager(client):
    """Manages requests from the server to the player

    Args:
        client (socket): socket object representing connection between server and player"""
        
    global answerstr, name, ranking, points # player data
    while True:
        request = client.recv(2048).decode(FORMAT)
        
        if request: # if there is a valid request
            
            if request == "%NAMEREQR": # require nickname from the player
                
                loginPage.show()
                while name == "": continue # wait for login page submission
                msg = name
                
                sendMsg(client, msg)
                
                loginPage.goNextPage() # go to waiting page
                
            elif request == "%ANSWRQST": # require an answer from the player
                
                waitPage.goNextPage() # go to question page
                
                """os.system('clear' if os.name == 'posix' else 'cls')
                msg = input("Which is the answer 1-4? \n> ")""" # code for cmd khoot
                
                while answerstr == "": continue # wait for questionPage submission
                msg = answerstr
                
                sendMsg(client, msg)
                
                answerstr = ""
                
                askingPage.goNextPage() # go to waiting page
                waitPage.widgets[0][0].config(text = f"Think you got it? ") # change waiting page text
                
            elif request[:9] == "%POINTCHK": # display player score and result of question
                
                if points < int(request[10:]): # if there is a change in score
                    waitPage.widgets[0][0].config(
                        text = f"CORRECT!", font=('Times New Roman',20,'bold')) # say correct
                    
                else: # if there is no score
                    waitPage.widgets[0][0].config(
                        text = f"WRONG!", font=('Times New Roman',20,'bold')) # say wrong
                
                points = int(request[10:]) # update points
                waitPage.widgets[1][0].config(text = f"You have {points} points!") # update waitPage text
            
            elif request[:9] == "%RANKINGL": # ranking leaderboard for player
                
                ranking = int(request[10:]) # get ranking
                
                # update waitPage text
                waitPage.widgets[0][0].config(text = "CONGRADULATIONS!", font=FONTS["heading"])
                waitPage.widgets[1][0].config(text = f"You placed #{ranking} with {points} points!")
                
            else: continue # for unknown requests
            
# waitPage with 2 labels, one for correct, and one for points
waitPage = Page([Label(app, text="Waiting for host to start the game! ", 
                       font=FONTS["heading"]), 0, 0, 25, 25], 
                [Label(app, text="", font=FONTS["text"]), 0, 1, 25, 25])

# askingPage with 4 buttons like khoot
askingPage = Page([Button(app, text="1", bg="blue", fg="black", height=7, width=10, 
                          command=lambda: answer("1"), font=FONTS["button"]), 0, 0, 10, 10], 
                  [Button(app, text="2", bg="red", fg="black", height=7, width=10, 
                          command=lambda: answer("2"), font=FONTS["button"]), 1, 0, 10, 10], 
                  [Button(app, text="3", bg="yellow", fg="black", height=7, width=10, 
                          command=lambda: answer("3"), font=FONTS["button"]), 0, 1, 10, 10], 
                  [Button(app, text="4", bg="green", fg="black", height=7, width=10, 
                          command=lambda: answer("4"), font=FONTS["button"]), 1, 1, 10, 10], 
                  nextPage=waitPage)

# setting the page after wait page to askingPage
waitPage.nextPage = askingPage

# loginPage with a label, entry, and button, to submit username
loginPage = Page([Label(app, text="Username:", font=FONTS["heading"]), 0, 0, 10, 10], 
                 [Entry(app, bd=2), 1, 0, 10, 10], 
                 [Button(app, text="Submit", font=FONTS["button"], 
                         command=lambda: login(loginPage)), 0, 1, 10, 10],
                 nextPage=waitPage)

# List of all pages (no use for now)
ALLPAGES = [waitPage, askingPage, loginPage]

# ======================================================================== #
# Initiation
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # connnection socket
client.connect(ADDR) # connect to server

client.send(("&PLAYJOIN").encode(FORMAT)) # alert server that you are a player

t = threading.Thread(target=lambda:requestsManager(client)).start() # start request manager thread
app.mainloop() # start 

del t # delete thread

exit() # kill

