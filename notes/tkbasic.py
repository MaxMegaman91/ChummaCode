# Import the library tkinter
from tkinter import *
import time

# Create a GUI app
app = Tk()

class Page():
    def __init__(self, *args, nextPage=None):
        """Give arrays of [widget, col, row], and a Page instance is created.
        .show() shows the webpage
        .hide() hides the webpage 
        
        Returns None
        """
        
        self.widgets = list(args)
        self.state="isHiding"
        self.nextPage=nextPage
        return

    def show(self, *_):
        for widget, col, row in self.widgets:
            display(widget, col, row)
        self.state="isShowing"
    
    def hide(self, *_):
        for widget, *xtras in self.widgets:
            remove(widget)
        self.state="isHiding"
        
    
    def goNextPage(self, nextPage=None, *_):
        if nextPage:  
            self.hide()
            nextPage.show()
        elif self.nextPage:
            self.hide()
            self.nextPage.show()
        return
        
    def toggle(self, *_):
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
  
# Creating a function for making widget visible again
def display(widget, col, row, padx=10, pady=10):
    widget.grid(column=col, row=row, padx=padx, pady=pady)
    
def login(loginPage:Page):
    #login
    name = loginPage.widgets[1][0].get()
    
    print(name)
    
    loginPage.goNextPage()

def answer(askingPage:Page, answer:str):
    global score
    score += 100
    askingPage.goNextPage()
    print(f"Answer submitted: {answer}")
    waitPage.widgets[0][0].config(text=f"You scored {score} points! ")


score = 0
waitPage = Page([Label(app, text="Waiting for host to start the game! "), 0, 0])

askingPage = Page([Button(app, text="1", bg="blue", fg="white", height=8, width=10, command=lambda: answer(askingPage, "1")), 0, 0], 
                  [Button(app, text="2", bg="red", fg="white", height=8, width=10, command=lambda: answer(askingPage, "2")), 1, 0], 
                  [Button(app, text="3", bg="yellow", fg="white", height=8, width=10, command=lambda: answer(askingPage, "3")), 0, 1], 
                  [Button(app, text="4", bg="green", fg="white", height=8, width=10, command=lambda: answer(askingPage, "4")), 1, 1], 
                  nextPage=waitPage)

waitPage.nextPage = askingPage

loginPage = Page([Label(app, text="Username:"), 0, 0], 
                 [Entry(app, bd=2), 1, 0], 
                 [Button(app, text="Submit", 
                         command=lambda: login(loginPage)), 0, 1],
                 nextPage=askingPage)


if input("> "):
    loginPage.show()


app.mainloop()


# Make infinite loop for displaying app on screen
