from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/add_todo')
def add_todo():
    print request.method
    return 'yea'

@app.route('/get_todo', methods = [ 'GET' ])
def get_todo():
    return 'todos'

if __name__ == '__main__':
    app.run()
