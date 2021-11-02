import time
from firebase_admin import credentials
import instabot
import firebase_admin
from firebase_admin import db
import os
import pprint
from decouple import config
import numpy as np
import cv2 as cv
from PIL import Image,ImageDraw,ImageFont
import textwrap

import requests
def waitTillInternetisOn():
    try:
        i=requests.get("https://www.google.com")
        return
    except Exception as e:
        time.sleep(2)
        print("wait")
        waitTillInternetisOn()
            
def logcurrTime():
    with open("logs.txt","w") as f:
        f.write(str(int(time.time())))
def checkIfTimePassed(t=86400//2):
    texz=time.time()
    with open('logs.txt','r') as f:
        texz=int(f.read())
    condn=time.time()-texz>t
    if not condn:
        tm=t-int(time.time())+texz

        print(f"{tm//3600}:{(tm%3600)//60}:{(tm%3600)%60} to go" )
    return condn


def stringTolist(quote):
    return quote.split("\n")
class fbToInsta():
    def __init__(self,envVariable="f2i-v2-cred"):
        self.vari=envVariable   
    def postpic(self,pic_path):
        
        isfile = os.path.isfile(pic_path) 
        if not isfile:
            print("file dont exist")
            return
        bot=instabot.Bot()
        bot.login(username=config("uname"))
        if checkIfTimePassed():
            r=bot.upload_photo(pic_path)
            self.dbRef.child(self.quoteSelected[0]).child("published").set("Published on "+time.asctime())
            logcurrTime()
        input()
        
    def downloadImg(self,url,name="test.jpg"):
        import requests
        r = requests.get(url, allow_redirects=True)
        open(name, 'wb').write(r.content)
    def connectDb(self,dburl='https://fb2insta-default-rtdb.firebaseio.com/',dbname="quotes"):
        cred=credentials.Certificate(config(self.vari))
        firebase_admin.initialize_app(cred, {
            'databaseURL': dburl
        })

        self.dbRef=db.reference(f"/{dbname}")
        self.listQuotes=self.dbRef.get()
        return self.listQuotes
    def makeAnImagefromString(self,quoteLines,l=480,b=480,text_size=25):
        c=0
        img=Image.new("RGB",(l,b),(0,0,0))
        for q in quoteLines:
            temp=textwrap.wrap(q,50)
            quote=""
            for i in temp:
                quote=i+"\n"
        
            
                fonts=ImageFont.truetype("CrimsonText-BoldItalic.ttf",size=text_size)
                d = ImageDraw.Draw(img)
                tw,th = d.textsize(quote, font=fonts)
                x=max((l-tw)//2,20)
                y=(b-th)//3+(text_size*1.5)*c
                d.text((x,y), quote, fill=(255,245,0),font=fonts)
                c+=1
        im2 = Image.open(r"cspic.png").convert('RGB')
        im3 = Image.blend(img, im2, 0.15)
        im3.save('pil_text.jpg')

    def selectAQuote(self):
        self.quoteSelected=None
        for key,value in self.listQuotes.items():
            if value["published"]=="NO":
                tl=stringTolist(value["quote"])
                self.quoteSelected=[key,tl]
                break
    def publishQuoteDefault(self):
        waitTillInternetisOn()
        self.connectDb()
        self.selectAQuote()
        if self.quoteSelected==None:
            print("Error :quote didnt received")
            return
        self.makeAnImagefromString(self.quoteSelected[1])
        self.postpic('pil_text.jpg')

if __name__=="__main__":
    t=fbToInsta()
    if not os.path.isfile('logs.txt'):
        logcurrTime()
    # print()
    if checkIfTimePassed(300):
        t.publishQuoteDefault()
    
# t.publishQuoteDefault()

# stringTolist()
# t.selectAQuote()
# t.makeAnImagefromString()

# print(config(vari))
# i=0
# for val in jst.values():
#     downloadImg(val['ImgName'],f"test{i}.jpg")
#     i+=1
# t.postpic("pil_text.jpg")
# downloadImg("https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1074&q=80")