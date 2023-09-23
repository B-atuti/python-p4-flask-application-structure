#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Welcome to my app!! </h1>"

@app.route('/<string:username>')
def user(username):
    return f'<h1> Welcome {username}</h1>'

@app.route('/about')
def about():
    return f'<h1>This is the my about page.</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=5555)
    