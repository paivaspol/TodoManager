from flask import Flask, request
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/add_todo', methods = [ 'POST' ])
def add_todo():
    print request.method
    return 'yea'

@app.route('/get_todo', methods = [ 'GET' ])
def get_todo():
    return 'todos'

if __name__ == '__main__':
    app.run()
