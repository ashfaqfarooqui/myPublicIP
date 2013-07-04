#!/usr/bin/python
import xmpp 
import os
import subprocess
from datetime import datetime

def messageCB(sess,mess):
    
    sender=mess.getFrom()
    message=mess.getBody()
    messageRecieved(message,sender)


def execCommand(cmd):
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out

def messageRecieved(msg,sender):
    
    stringMessage = str(msg)
    print stringMessage
    case = stringMessage.startswith('command')
    print case
    if case:
        command = stringMessage[3:]
        print command
        if cmp(str(command.lstrip()), str("giveMeMyIp"))==0:
            out = execCommand("wget http://ipecho.net/plain -O - -q ; echo")
        else:
            out = execCommand("echo invalidPassword")
        sendOutput(str(out),sender)
        
def sendMessage():
    out=execCommand("wget http://ipecho.net/plain -O - -q ; echo")
    sendOutput(out, aravind)
    sendOutput(out, omar)
   
    
def sendOutput(outputData,nick):
    message = xmpp.Message(nick, outputData)
    message.setAttr('type', 'chat')
    client.send(message)
 
aravind='aravindma1990@gmail.com'
# aravind='ashfaq.farooqui@swissjabber.ch'
omar='moihussain@gmail.com'   
username = 'ashfaq.farooqui'
passwd = ''

t1= datetime.now()
client = xmpp.Client('gmail.com')
client.connect(server=('talk.google.com',5223))
client.auth(username, passwd, 'botty')
client.sendInitPresence()
client.RegisterHandler('message',messageCB)


while 1:
    client.Process(1)
    t2=datetime.now()
    tdelta=(t2-t1).total_seconds()
    if(tdelta>=7600):
        t1=datetime.now()
        sendMessage()
        
