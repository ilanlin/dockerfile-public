#coding=utf-8  
__author__ = 'cloudtogo'

from flask import Flask
import sys

app = Flask(__name__)


@app.route('/')
def hello():
    return '恭喜您成功地发布了一个运行在云端的python程序 hello-GIT,公网github,public，main分支,module1目录'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=81)
