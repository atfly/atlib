#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Flask
from flask import request
from flask import render_template
import sys

reload(sys)
sys.setdefaultencoding('utf8')
app = Flask(__name__)


@app.route('/upload', methods=['POST', 'GET'])
def uploadfile():
    if request.method == "POST":
        file = request.files['file']
        if file:
            filename = file.filename
            return "processed " + filename
        else:
            return "not a file"


@app.route('/helloworld', methods=['POST', 'GET'])
def hellorld():
    if request.method == 'POST':
        req = request.form['he'].encode('utf-8')
        return "req"


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
