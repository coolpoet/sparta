from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

## 코딩 할 준비 ##

all_musics = list(db.musics.find())

print(all_musics) 