#copy to android from PC
import win32clipboard
import TcpTaskerEventPy as Sender

key="putyourPassword"
ipadr="192.168.1.254:8080"
verific=True
prefix="COPYTODROIDCLIP=:="

win32clipboard.OpenClipboard()
try:
  eg.globals.clip = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
except:
  pass
win32clipboard.CloseClipboard()

try:
  eg.plugins.EventGhost.ShowOSD(u'{eg.globals.clip}', u'0;-24;0;0;0;700;0;0;0;1;0;0;2;32;Arial', (255, 255, 255), (0, 0, 0), 0, (0, 0), 0, 3.0, False)
  clipme=prefix+str(eg.globals.clip)
  Sender.sendmsgENCODED (ipadr,clipme,key,verific)
except:
  eg.plugins.EventGhost.ShowOSD(u'ERROR in sending', u'0;-24;0;0;0;700;0;0;0;1;0;0;2;32;Arial', (255, 255, 255), (0, 0, 0), 0, (0, 0), 0, 3.0, False) 
  pass


##############################################################################

#copy to android from PC

import TcpTaskerEventPy as Sender

key="putyourPassword"
ipadr="192.168.1.254:8080"
verific=True
message="GIVE_METEXT"
Sender.sendmsgENCODED (ipadr,message,key,verific)


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


