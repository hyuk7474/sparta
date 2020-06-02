from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def prac1():
    print('In')
    return '안녕하세요!!'

@app.route('/json')
def json_data():
    person = [{'name': 'joeun', 'age': 39, 'hobby': 'climbing'}, {'name': 'Inhyuk', 'age': 31, 'hobby': 'climbing'}]
    return jsonify(person)




if __name__ == '__main__': 
   app.run('0.0.0.0',port=5000,debug=True)