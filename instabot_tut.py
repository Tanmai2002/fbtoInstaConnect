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

class fbToInsta():
    def __init__(self,envVariable="connect-v2-cred"):
        self.vari=envVariable   
    def postpic(self,pic_path):
        isfile = os.path.isfile(pic_path) 
        if not isfile:
            print("file dont exist")
            return
        bot=instabot.Bot()
        bot.login()
        bot.upload_photo(pic_path)
    def downloadImg(self,url,name="test.jpg"):
        import requests
        r = requests.get(url, allow_redirects=True)
        open(name, 'wb').write(r.content)
    def connectDb(self,dburl='https://connectv2-ff192-default-rtdb.firebaseio.com/',dbname="users"):
        cred=credentials.Certificate(config(self.vari))
        firebase_admin.initialize_app(cred, {
            'databaseURL': dburl
        })

        self.dbRef=db.reference(f"/{dbname}")
    def makeAnImagefromString(self,quoteLines,l=1080,b=1080,text_size=50):
        
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
                y=(b-th)//3+(text_size+25)*c
                d.text((x,y), quote, fill=(255,245,0),font=fonts)
                c+=1
        im2 = Image.open(r"Craziness Speaks.png").convert('RGB')
        im3 = Image.blend(img, im2, 0.15)
        im3.save('pil_text.png')


t=fbToInsta()
t.makeAnImagefromString(["Life is a game that demands fame."," whis dfgf fdx xfzdZds  hjcghcghc gcgc cfcfhcfgccfgcg gxdfxdxgfx xfxfd."," dfxfdxgfc cfcg cgfcghchgcgf fxgfxgx"])
# t.connectDb()
# print(config(vari))
# i=0
# for val in jst.values():
#     downloadImg(val['ImgName'],f"test{i}.jpg")
#     i+=1
# postpic("testers.jpg")
# downloadImg("https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1074&q=80")