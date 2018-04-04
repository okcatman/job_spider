#!/usr/bin/env python
#coding:utf8

#提供API接口
from flask import Flask
import sqlite3
import random

app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return 'welcome to proxy pool'

@app.route('/get',methods=['GET'])
def api():
    conn = sqlite3.connect('ip.db')
    cursor = conn.cursor()
    try:
        a = cursor.execute('select * from ip').fetchall()
        if len(a) == 0:
            return 'error'
        else:
            a = random.choice(a)
            return a[0]
    except:
        return 'error'


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5001,debug=True)