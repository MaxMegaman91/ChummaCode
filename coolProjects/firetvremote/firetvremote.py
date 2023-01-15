import os
from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.auth.keygen import keygen

class fireStickController():
    def __init__(self):
        if not os.path.isfile('adbkey'):
            print("Generating ADB keys...")
            keygen('adbkey')
        else: print("ADB keys found!")

        with open('adbkey') as f:
            print("Reading ADB keys!")
            priv = f.read()
        with open('adbkey'+'.pub') as f:
            pub = f.read()
        self.creds = PythonRSASigner(pub,priv)
        print("Credentials set! ")
        self.buttonDict = {
            "home":b' 111',
            "wake":b' 177',
            "back":b' 4',
            "undo":b' 4',
            "microphone":b' 130',
            "up":b' 19',
            "down":b' 20',
            "left":b' 21',
            "right":b' 22',
            "select":b' 23',
            "menu":b' 82',
            "play":b' 85',
            "pause":b' 85',
            "rewind":b' 89',
            "forward":b' 90'}

    def addDevice(self, deviceIP):
        print("Connecting...")
        self.device = AdbDeviceTcp(deviceIP,5555,default_transport_timeout_s=9.)
        try:
            self.device.close()
        except:
            print("No device connected...")
        else:
            self.device.connect(rsa_keys=[self.creds],auth_timeout_s=10.)
        
        print("Connected! ")
        return self.device

    def select(self):
        self.device._service(b'shell',b'input keyevent ()')
        print("Select command sent! ")

    def pressbutton(self,button):
        import threading
        try:
            threading.Thread(target=lambda:self.device._service(b'shell',b'input keyevent' + self.buttonDict[button])).start()
            
        except KeyError:
            print("Invalid key! ")


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


