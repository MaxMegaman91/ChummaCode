import main as mytube
import tkinter as tk


window = tk.Tk()


def readInput():
    global link
    link = linkInput.get()

linkInput = tk.Entry(window, width=43)
linkInput.grid(row=0,column=0)

mybutton = tk.Button(window, text="Submit", command=readInput, width=35)
mybutton.grid(row=1, column=0)

window.mainloop()

