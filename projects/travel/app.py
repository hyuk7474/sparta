# 아래 2줄은 항상 제일 위에 위치
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import Mongoclient
client = MongoClient('localhost', 27017) 
db = client.dbsparta  


@app.route('/')
def home(): 
   print('요청이 들어왔습니다!')
   return render_template('index.html')


@app.route('/menu', methods=['GET'])
def listing():
    


@app.route('/test', methods=['POST'])  # GET 메소드 응답만 받겠다
def saving():
    link_url = request.form['link_url']
    comment = request.form['comment']

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(link_url ,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    url_image = og_image['content']
    url_title = og_title['content']
    url_description = og_description['content']

    document = {,
        url = 'link_url',
        comment = 'comment',
        title = 'url_title',
        image = 'url_image',
        description = 'url_description',
    }
    db.travels.insert_one(document)

    return jsonify({'result': 'success', 'msg': 'POST에 저장되었습니다.'})


    
    

if __name__ == '__main__':  
    # 0.0.0.0 -> 모든 IP에게 요청을 받아주겠음
    # port=5000 -> 5000번 포트에 서버를 등록해서 요청을 받아주겠음
    # debug=True -> 무언가 에러가 났을 때 에러 메시지를 그대로 보여줌
   app.run('0.0.0.0',port=5000,debug=True)