from tkinter import *
import os, random

app = Tk()

Label(app, text="Kahoot Question Maker", font=("Dejavu Sans", 20, "underline")).grid(columnspan=2, column=0, row=0, padx=15, pady=10)
Label(app, text="Question", font=("Droid Sans Fallback", 12)).grid(column=0, row=1, padx=10, pady=5)
Label(app, text="Answer", font=("Droid Sans Fallback", 12)).grid(column=0, row=2, padx=10, pady=5)
Label(app, text="Option", font=("Droid Sans Fallback", 12)).grid(column=0, row=3, padx=10, pady=5)
Label(app, text="Option", font=("Droid Sans Fallback", 12)).grid(column=0, row=4, padx=10, pady=5)
Label(app, text="Option", font=("Droid Sans Fallback", 12)).grid(column=0, row=5, padx=10, pady=5)

options = []
question = Entry(app, bd=5)
question.grid(column=1, row=1, padx=5, pady=8, ipadx=50, ipady=20)
answer = Entry(app, bd=5)
answer.grid(column=1, row=2, padx=5, pady=5, ipadx=50, ipady=12)
options.append(Entry(app, bd=5))
options[-1].grid(column=1, row=3, padx=5, pady=5, ipadx=50, ipady=12)
options.append(Entry(app, bd=5))
options[-1].grid(column=1, row=4, padx=5, pady=5, ipadx=50, ipady=12)
options.append(Entry(app, bd=5))
options[-1].grid(column=1, row=5, padx=5, pady=5, ipadx=50, ipady=12)

addQbutton = Button(app, bd=2, text="Submit", width=20, 
                    height=2, command=lambda:addQuestion()).grid(
                        columnspan=2, column=0, row=6, padx=5, pady=10)
listQbutton = Button(app, bd=2, text="Remove a Question", 
                     width=20, height=2, command=lambda:removeQuestion()).grid(
                         columnspan=2, column=0, row=7, padx=5, pady=20)
def addQuestion():
    with open(os.path.join(os.path.dirname(__file__), "questions.txt"), "a") as file: 
        questiontext= question.get()
        question.delete(0, END)
        if questiontext[-1] != "?":
            questiontext += "?"
        
        answertext = answer.get()
        answer.delete(0, END)
        
        optionstext=[]
        for entry in options:
            optionstext.append(entry.get())
            entry.delete(0, END)
        
        answerpos = random.randint(1,4)
        optionstext.insert(answerpos-1, answertext)
        
        file.write(f"{questiontext} ||{optionstext[0]}||{optionstext[1]}||{optionstext[2]}||{optionstext[3]}||{str(answerpos)}\n")

def removeQuestion():
    
    with open(os.path.join(os.path.dirname(__file__), "questions.txt"), "r") as file: 
        rawlines = file.readlines()
    
    with open(os.path.join(os.path.dirname(__file__), "questions.txt"), "w") as f:
        for line in rawlines:
            if line != rawlines[-1]:
                f.write(line)

app.mainloop()