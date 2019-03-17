
import base64
import hashlib
import socket
import time
from random import randint

from Crypto import Random
from Crypto.Cipher import AES


# Here is the AESCipher classe
class AESCipher(object):

    def __init__(self, key):
        self.bs = 16
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[0:-ord(s[-1])]
#End of AES Cypher class

""""
Here is the message encryption

"""

def encrypt(message, key, verification):
    MULTIPLYER =10000
    if(verification is not None and verification):
        millis = int(round(time.time() * 1000))*MULTIPLYER+randint(1000, 9999)
        message=message+"=:="+str(millis)
    cypher = AESCipher(key)
    return cypher.encrypt(message)


""""
Here is the message encryption sending function

"""

def sendmsgENCODED(ipadress,message,key=None,verification=None):
    """
    ipadress is "192.168.1.222:8888" change it according to your configuration
    message is the essage to send
    key is the password. if you set it the message will encrypted with Aes 128
    verification can be True or False. if True it will append a time base id at the end
    of the message before encryption;
    eg if we send message "hello world" and verification is True
    it wll encrypt the message with like this "hello world=:=15528197335140840"
    
    here 15528197335140840 is a time base. actually the last four digit is a random number
    and  1552819733514 is the System current millis;

    
    """
    
    
    try:
        if(key is not None):
            message=encrypt(message,key,verification)
        target = ipadress.split(":")
        ip=target[0]
        port=int(target[1])
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        client.send((message).encode())
    except Exception as e:
        print(e)
        
"""
the following is for decryption of mesage after recieving.
Please note that verification will not work well if you dont initialize 
a globale constant "eg.globals.previousId" in autostart. 
and also it soulod be a list. this list should be pass as parametre while caclling
"decodeMessage(message,key,verification,prevIds)"
prevIds is this list;
it make sure that no same message is sent to this device
"""
def decodeMessage(message,key,verification=False,prevIds=None):
    
    """"
    message is the encypted message
    key is the passeord used
    verification can be True or False
    prevIds is the list which store the previous message id
    """
    cypher = AESCipher(key)
    cypher=cypher.decrypt(message)
    if(verification==True):
        isverified=checkverify(cypher,prevIds)
        if(isverified):
            return cypher
        else:
            return None
    return cypher

def checkverify(message,prevIds=None):
    MULTIPLYER=10000
    CONSTANT = 600000 * MULTIPLYER;#maximum valid time 10 minute after that it will ce invalid
    milli=int(round(time.time() * 1000))*MULTIPLYER
    id=(message.split("=:="))[-1]
    try:
        id=int(id)
        if(id<1):
            id=0
    except Exception as e:
        id=0
        print(e)
    if(prevIds is not None):
        for prev in prevIds:
            if(prev<milli):
                prevIds.remove(prev)
            if(prev == id):
                return False
        prevIds.insert(len(prevIds),id)
    return id > milli - CONSTANT and id < milli + CONSTANT;
    
    
    
#sendmsgENCODED ("192.168.1.254:8080","hullo","aaa",True)
#str="oAg5jgiC/8Ya2NUrq9u5zsvPdJVZNHlyoPSZP/ELorjnUpIWvCdw9D+Ke+kBxtJr"
#print(str)
#print(checkverify("H=:=15528197335140840"))

