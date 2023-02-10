from flask import Flask, render_template, request
from bson import json_util
import json
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.vvxg7bx.mongodb.net/?retryWrites=true&w=majority')
db = client.chang

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/submit', methods=['POST'])
def submit_post():
    name = request.form['name']
    email = request.form['email']
    contact = request.form['contact']
    message = request.form['message']

    doc = {
        'name': name,
        'email': email,
        'contact':contact,
        'message': message,
    }
    result = db.applications.insert_one(doc) # applications 라는 Collection 에 저장
    doc_inserted = db.applications.find_one({'_id': result.inserted_id}) # 저장된 데이터를 반환

    return json.loads(json_util.dumps(doc_inserted))

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
