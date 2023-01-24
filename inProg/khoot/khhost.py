#=#
# imports
import socket, threading, time, sys, select, json, os
# Import the library tkinter
from tkinter import *


#=#
# Constants
HEADER = 64
SERVER = "192.168.86.21"
try: PORT = int(sys.argv[1]) if sys.argv[1] else 14014
except: PORT = 14015
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "%DISCONNECT"

# Create a GUI app
app = Tk()
username = ""
ready = False
toQuestion = False
nextQuestion = False


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
    if type(input) != list:
        try: input.grid_remove()
        except: return False
    elif type(input) == list:
        for widget in input:
            remove(widget)
    return True

    
def login(loginPage:Page):
    global username, readyPage
    #login
    username = loginPage.widgets[1][0].get()
    
    print(username)
    
    loginPage.goNextPage(readyPage)

def startGame(readyPage:Page):
    global ready, questionPage
    ready = True
    
    readyPage.hide()

def skipQuestion(questionPage:Page):
    global nextQuestion
    nextQuestion = True
    
    
    
def toNextQuestion(leaderboardPage:Page):
    global toQuestion
    
    toQuestion = True
    
    leaderboardPage.hide()


def rawIn(prompt, timeout=30.0):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ready, _, _ = select.select([sys.stdin], [],[], timeout)
    if ready:
        return sys.stdin.readline().rstrip('\n') # expect stdin to be line-buffered
    else:
        print("\n")
    return "1"

def sendMsg(client, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)


def requestsManager(client):
    global nextQuestion, username, ready, toQuestion, leaderboardPage
    
    while True:
        request = client.recv(2048).decode(FORMAT)
        
        if request:
            if request == "%NAMEREQR": # loginPage wait for username
                # msg = input("Nickname for reference? \n> ")
                while username == "":  continue
                msg = username
                
            elif request == "%READYUP?": # readyPage wait for buttonClick
                #input("Enter to start game! \n> ")
                
                while ready == False: continue
                ready=False
                msg = "&STRTGAME"
                
            elif request[:9] == "%QUESTION": # questionPage write questions into label
                t0 = time.perf_counter()
                
                question = request[10:]
                question, *options = question.split("||")
                
                questionPage.widgets[0][0].config(text = f"QUESTION: {question}")
                questionPage.widgets[1][0].config(text = f"OPTIONS: 1) {options[0]} \n2) {options[1]} \n3) {options[2]} \n4) {options[3]}")
                
                questionPage.show()
                
                # os.system('clear' if os.name == 'posix' else 'cls')
                # print(f"QUESTION: {question}")
                # print(f"OPTIONS: \n1. {options[0]} \n2. {options[1]} \n3. {options[2]} \n4. {options[3]}")
                # print("\n")
                
                continue
            elif request == "%QSTNFNSH":# questionPage wait for 30 seconds or buttonclick
                # rawIn("Enter to next question \n> ")
                # print("\n")
                
                while (time.perf_counter()-t0 <= 30) and (nextQuestion == False): continue
                nextQuestion = False
                
                questionPage.hide()
                
                msg = "&NEXTQSTN"
                
            elif request[:9] == "%LDRBOARD": # leaderboardPage write leaderboard into labels, wait for buttonclick
                # os.system('clear' if os.name == 'posix' else 'cls')
                # print("\n")
                
                leaderboard = json.loads(request[10:]) # [[aarush, 100]]
                if len(leaderboard) > 5: leaderSpots = 4
                else: leaderSpots = len(leaderboard)
                
                leaderstr = ""
                
                for n in range(leaderSpots):
                    player, score = leaderboard[n]
                    leaderstr += (f"At #{n+1}, {player} scored {score} points!")
                    
                leaderboardPage.widgets[1][0].config(text= leaderstr)
                
                leaderboardPage.show()
                while toQuestion == False: continue
                toQuestion = False
                
                msg = "go"
            elif request == "%GAMEOVER": #leaderboard page again
                # os.system('clear' if os.name == 'posix' else 'cls')
                # print("\n")
                
                questionPage.hide()
                
                
                # leaderboard = json.loads(request[10:]) # [[aarush, 100]]
                if len(leaderboard) > 5: leaderSpots = 4
                else: leaderSpots = len(leaderboard)
                
                leaderstr = ""
                
                for n in range(leaderSpots):
                    player, score = leaderboard[n]
                    leaderstr += (f"At #{n+1}, {player} scored {score} points!")
                    
                leaderboardPage.widgets[1][0].config(text= leaderstr)
                leaderboardPage.show()
                remove(leaderboardPage.widgets[2][0])
                
                
                msg=""
                
                
                
            sendMsg(client, msg)
    
"""
LoginPage - :)
readyPage - 
questionPage - 
leaderboardPage - 

"""




leaderboardPage = Page([Label(app, text="LEADERBOARD"), 0, 0, 15, 20],
                       [Label(app, text="$1\n$2\n$3\n$4\n$5"), 0, 1, 10, 10],
                       [Button(app, text="Next Question!", command=lambda: toNextQuestion(leaderboardPage)), 0, 2, 10, 10])

questionPage = Page([Label(app, text="QUESTION: $"), 0, 0, 15, 20],
                    [Label(app, text="OPTIONS: \n$\n$\n$\n$"), 0, 1, 10, 10],
                    [Button(app, text="Skip Question", command= lambda: skipQuestion(questionPage)), 0, 2, 10, 10],
                    nextPage=leaderboardPage)

leaderboardPage.nextPage = questionPage

readyPage = Page([Label(app, text="0 players joined!"), 0, 0, 10, 15],
                 [Button(app, text="Start Game!", command=lambda :startGame(readyPage)), 0, 1, 10, 10], nextPage = questionPage)

# loginPage with a label, entry, and button, to submit username
loginPage = Page([Label(app, text="Username:"), 0, 0, 10, 10], 
                 [Entry(app, bd=2), 1, 0, 10, 10], 
                 [Button(app, text="Submit", 
                         command=lambda: login(loginPage)), 0, 1, 10, 10],
                 nextPage=readyPage)


#=#
# Init
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(("&HOSTJOIN").encode(FORMAT))

threading.Thread(target=lambda:requestsManager(client)).start()
loginPage.show()
app.mainloop()




# Make infinite loop for displaying app on screen
