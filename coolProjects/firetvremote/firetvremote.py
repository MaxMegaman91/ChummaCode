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




