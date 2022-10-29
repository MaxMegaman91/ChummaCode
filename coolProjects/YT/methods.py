import mytube
import tkinter as tk


window = tk.Tk()


def readInput():
    global link
    link = linkInput.get()
    for x in range(int(link)): tk.Label(text="window "+ str(x)).grid(row=x+2, column=0)
    mybutton.destroy()


linkInput = tk.Entry(window, width=43)
linkInput.grid(row=0,column=0)

mybutton = tk.Button(window, text="Submit", command=readInput, width=35)
mybutton.grid(row=1, column=0)

window.mainloop()

