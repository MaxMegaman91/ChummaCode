import tkinter as tk
import firetvremote as ftvcontrol

debug = False

window = tk.Tk()

window.columnconfigure(list(range(3)), minsize=50)
window.rowconfigure(list(range(8)), minsize=50)
window.title("Fire TV")
window.resizable(width=False, height=False)

apicopy = ftvcontrol.fireStickController()
apicopy.addDevice("192.168.2.18")

tk.Button(window,text="👂",command = lambda: apicopy.pressbutton("wake"),font=("Arial",20)).grid(row=0,column=1)
tk.Button(window,text="↑",command = lambda: apicopy.pressbutton("up"),font=("Arial",20)).grid(row=1,column=1)
tk.Button(window,text="←",command = lambda: apicopy.pressbutton("left"),font=("Arial",20)).grid(row=2,column=0)
tk.Button(window,text="🔘",command = lambda: apicopy.pressbutton("select"),font=("Arial",20)).grid(row=2,column=1)
tk.Button(window,text="→",command = lambda: apicopy.pressbutton("right"),font=("Arial",20)).grid(row=2,column=2)
tk.Button(window,text="↓",command = lambda: apicopy.pressbutton("down"),font=("Arial",20)).grid(row=3,column=1)
#row gap
tk.Button(window,text="⎌",command = lambda: apicopy.pressbutton("back"),font=("Arial",20)).grid(row=5,column=0)
tk.Button(window,text="⌂",command = lambda: apicopy.pressbutton("home"),font=("Arial",20)).grid(row=5,column=1)
tk.Button(window,text="𝪊",command = lambda: apicopy.pressbutton("menu"),font=("Arial",20)).grid(row=5,column=2)
tk.Button(window,text="⮄",command = lambda: apicopy.pressbutton("rewind"),font=("Arial",20)).grid(row=6,column=0)
tk.Button(window,text="‣",command = lambda: apicopy.pressbutton("pause"),font=("Arial",20)).grid(row=6,column=1)
tk.Button(window,text="⇉",command = lambda: apicopy.pressbutton("forward"),font=("Arial",20)).grid(row=6,column=2)


try:
    window.mainloop()
except: print("")
