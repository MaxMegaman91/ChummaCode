SAVE_PATH = "C:/Users/aarus/ChummaCode/coolProjects/notifier/"
from plyer import notification
import datetime, time
from simplegmail import Gmail
from win10toast_click import ToastNotifier

def mail_open():
    import webbrowser
    webbrowser.open("https://mail.google.com/mail/u/0")
    
def timeread():
    with open(SAVE_PATH + "time.txt", "r") as file1:
        lines = file1.readline()
    return datetime.datetime.strptime(lines, '%Y-%m-%d %H:%M:%S')

def timewrite(timein):
    with open(SAVE_PATH + "time.txt","w") as file1:
        file1.write(timein.strftime("%Y-%m-%d %H:%M:%S"))
    return True

gmail = Gmail(client_secret_file=SAVE_PATH + "client_secret.json")
lastCheckedDate = timeread()

messages = gmail.get_unread_inbox()

for message in messages:
    
    if datetime.datetime.strptime(message.date[0:-6], '%Y-%m-%d %H:%M:%S') > lastCheckedDate:
        ToastNotifier().show_toast(
            title='Mail from {}'.format(message.sender[:message.sender.index("<")]),
            msg=message.subject,
            icon_path= SAVE_PATH + "mailxilter.ico",
            duration=3,
            threaded=True, 
            callback_on_click=mail_open) 

timewrite(datetime.datetime.now())



