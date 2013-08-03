#!/usr/bin/python
import xmpp 
import os
import subprocess
from datetime import datetime
import logging

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
        if cmp(str(command.lstrip()), str("uniquekey"))==0:
            out = execCommand("wget http://ipecho.net/plain -O - -q ; echo")
        else:
            out = execCommand("echo invalidPassword")
        sendOutput(str(out),sender)
    logging.info('messageRecieved at'+str(datetime.now().hour)+'from'+str(sender)+'message:'+stringMessage)
        
def sendMessage():
    out=execCommand("wget http://ipecho.net/plain -O - -q ; echo")
    sendOutput(out, aravind)
    sendOutput(out, omar)
    logging.info('message sent to both'+str(datetime.now().hour)+':'+str(datetime.now().minute))
   
    

def createMessage(outputData, nick):
    if str(message.getBody())!=outputData :
        message.setBody(outputData)
    if str(message.getTo())!=nick :
        message.setTo(nick)
    message.setAttr('type', 'chat')
    return message

def sendOutput(outputData,nick):
    message = createMessage(outputData, nick)
    client.send(message)
    logging.info('messageSent on request at'+str(datetime.now().hour)+'to'+str(nick)+'message:'+str(outputData))
 
aravind='user@mail.com'
omar='user@mail.com'   
username = 'myself'
passwd = 'pass'

message =xmpp.Message('welcome',aravind)
t1= datetime.now()
client = xmpp.Client('gmail.com')
client.connect(server=('talk.google.com',5223))
client.auth(username, passwd, 'botty')
client.sendInitPresence()
client.RegisterHandler('message',messageCB)

logging.basicConfig(filename='myPublicIpLog.log',level=logging.DEBUG)
while 1:
    client.Process(1)
    t2=datetime.now()
    tdelta=(t2-t1).total_seconds()
    if(tdelta>=15):
        t1=datetime.now()
        sendMessage()
        logging.info('Time reset at:'+str(datetime.now().hour)+':'+str(datetime.now().minute))
        
