import requests
import json
import coolProjects.firetvremote.firetvremote as ftv

def retrieve_messages(channelid):
    headers = {
        'authorization':'NzMwMDUxMzk5OTQ5NDg0MTAy.GHpmhr.skovc13qtvVAn-EH5A1DJNQxB_cn3e9kQJxg7k'
    }
    
    r = requests.get(f"https://discord.com/api/v9/channels/{channelid}/messages",headers=headers)
    messages = json.loads(r.text)
    
    texts = []
    for x in messages:
        texts.append(x['content'])
        
    return texts

startmsgs = retrieve_messages(1091156440875536387)
apicopy = ftv.fireStickController()
apicopy.addDevice("192.168.2.18")
print("waiting...")
while True:
    trial = retrieve_messages(1091156440875536387)
    
    if len(trial) > len(startmsgs) and trial[0] == "/firetv down":
        print("called.")
        apicopy.pressbutton('down')
        
        startmsgs = trial