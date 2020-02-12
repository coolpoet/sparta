from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta   


@app.route('/')
def home():
    return render_template('homework1.html')

@app.route('/order', methods=['GET'])
def listing():
    order = list(db.orders.find({}, {'_id':False}))
    return jsonify({'result':'success', 'order':order})

@app.route('/order', methods=['POST'])
def saving():
    name_receive = request.form['name_give']  # 클라이언트로부터 url을 받는 부분
    email_receive = request.form['email_give']
    phone_receive = request.form['phone_give']
    comment_receive = request.form['comment_give']  

    order = {'name': name_receive, 
             'email': email_receive, 
             'phone': phone_receive,
             'comment': comment_receive}

    db.orders.insert_one(order)
    
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)