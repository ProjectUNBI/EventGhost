#copy to android from PC

import win32clipboard
import socket
import codecs
import re
import base64
 
def sendmsgENCODED(arg1):
    target = '192.168.1.254'
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target, 8080))
    client.send((u'copyfromWindows'+"=:="+arg1).encode())
 
win32clipboard.OpenClipboard()
try:
    eg.globals.clip = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
except:
    pass
win32clipboard.CloseClipboard()
millis = str(int(round(time.time() * 1000)))
clipme=str(eg.globals.clip)
print clipme.decode("utf-8")
try:
   eg.plugins.EventGhost.ShowOSD(u'{eg.globals.clip}', u'0;-24;0;0;0;700;0;0;0;1;0;0;2;32;Arial', (255, 255, 255), (0, 0, 0), 0, (0, 0), 0, 3.0, False)
   clipme=base64.b64encode(bytes(clipme))
   sendmsgENCODED(clipme)
   eg.globals.PendingAction.append([millis,'Copying Clipboard to XIOMI'])
except:
   eg.plugins.EventGhost.ShowOSD(u'ERROR in Parsing', u'0;-24;0;0;0;700;0;0;0;1;0;0;2;32;Arial', (255, 255, 255), (0, 0, 0), 0, (0, 0), 0, 3.0, False)




##############################################################################


#copy  from android command

import socket
import codecs
import re
import base64
 
def sendmsgENCODED(arg1):
    target = '192.168.1.254'
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target, 8080))
    client.send((u'copyToPC'+"=:="+arg1).encode())
 
textTosend="copyToPC"
print textTosend.decode("utf-8")
try:
   eg.plugins.EventGhost.ShowOSD(u'Copying from mobile', u'0;-24;0;0;0;700;0;0;0;1;0;0;2;32;Arial', (255, 255, 255), (0, 0, 0), 0, (0, 0), 0, 3.0, False)
   sendmsgENCODED(textTosend)
except:
   eg.plugins.EventGhost.ShowOSD(u'ERROR in Parsing', u'0;-24;0;0;0;700;0;0;0;1;0;0;2;32;Arial', (255, 255, 255), (0, 0, 0), 0, (0, 0), 0, 3.0, False)






###################################################################################


#After Receiving comand from android


from win32clipboard import *
import win32gui, win32con
import base64
print eg.event.payload.armessage
clip=str(eg.event.payload.armessage)

try:
    OpenClipboard() 
    EmptyClipboard()
    decoded=base64.b64decode(bytes(clip[16:]+"="))
    SetClipboardData(win32con.CF_TEXT, decoded) # set clipboard data
except Exception, e:
    # handle it
    CloseClipboard()
    eg.plugins.EventGhost.ShowOSD("Error in copying from Xiomi", u'0;-24;0;0;0;700;0;0;0;1;0;0;2;32;Arial', (255, 255, 255), (0, 0, 0), 0, (0, 0), 0, 3.0, False)
CloseClipboard()
eg.plugins.EventGhost.ShowOSD("Text Copied From XIOMI", u'0;-24;0;0;0;700;0;0;0;1;0;0;2;32;Arial', (255, 255, 255), (0, 0, 0), 0, (0, 0), 0, 3.0, False)


