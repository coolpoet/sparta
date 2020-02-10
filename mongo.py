from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기

# MongoDB에서 데이터 모두 보기
all_users = list(db.users.find({}))
print(all_users)



db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

db.users.update_many({'name':'boddy'},{'$set':{'age':19}})

db.users.delete_one({'name':'bobby'})

db.users.delete_many({'name':'boddy'})