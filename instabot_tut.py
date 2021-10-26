from firebase_admin import credentials
import instabot
import firebase_admin
from firebase_admin import db
import os
import pprint
from decouple import config
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
        
t=fbToInsta()
t.connectDb()
# print(config(vari))
# i=0
# for val in jst.values():
#     downloadImg(val['ImgName'],f"test{i}.jpg")
#     i+=1
# postpic("testers.jpg")
# downloadImg("https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1074&q=80")