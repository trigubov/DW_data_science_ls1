from flask import Flask, request, Response, jsonify
import datetime

app = Flask(__name__)

@app.route('/time')
def current_time():
    return {'time': datetime.datetime.now()}

@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    return f'Hello, {name}!'

@app.route('/')
def index():
    return "Test message. The server is running"

@app.route('/add', methods=['POST'])
def add():
    num = request.json['num']
    if num > 10:
        return 'too much', 400
    return jsonify({'result': num + 1})

if __name__ == '__main__':

    app.run('localhost', 5000)


