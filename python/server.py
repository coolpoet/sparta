from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('bootstrap.html')

@app.route('/test', methods=['POST'])
def test_post():

    title_receive = request.form['title_give']
    
    movie_info = db.movies.find_one({'title': title_receive},{'_id':0})
    
    star = movie_info['star']

    db.movies.update_many({'star':star}, {'$set':{'star':0}})

    return jsonify({'result':'success'})

@app.route('/test', methods=['GET'])
def test_get():

    title_receive = request.args.get('title_give')

    movie_info = db.movies.find_one({'title': title_receive},{'_id':0})
    star = movie_info['star']

    movies = list(db.movies.find({'star':star},{'_id':0})) 
    print(movies)
    titles = []

    for m in movies:
        titles.append(m['title'])

    return jsonify({'title':titles})




if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)