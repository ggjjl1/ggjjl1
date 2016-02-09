#usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import MySQLdb
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

#网站名称
blog_name = "gjl's website."
logo_name = blog_name

#打开数据库连接
db = MySQLdb.connect(host="123.56.179.65",user="huiyi",passwd="huiyi0331",db="gjl_website", charset="utf8")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print "database's version is: %s." % data

@app.route('/')
def index():
    return render_template('index.html', blog_name=blog_name, logo_name=logo_name)

@app.route('/post/')
def show_post():
    return render_template('post.html', blog_name=blog_name)

@app.route('/write/', methods=['GET', 'POST'])
def write():
    if request.method == 'GET':
        return render_template('write.html', blog_name=blog_name)
    elif request.method == 'POST':
        print "已经提交表单."
        title = request.form['title']
        content = request.form['content']
        ctime = int(time.time()) 
        print("title: %s, content: %s, ctime: %d" %(title, content, ctime))
        sql = "insert into post(title, content, ctime) values('%s', '%s', '%d')" % (title, content, ctime)
        print(sql)
        try:
            n = cursor.execute(sql)
            print n
            db.commit()
            if n == 1:
                return redirect(url_for('index'))
        except:
            print "insert data error!"

@app.route('/login/', methods=['GET', 'POST'])
def login():
   return render_template('login.html')

@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('hello.html')

@app.route('/handle/')
def handle():
    id = request.args.get('id', 0, type=int)
    return jsonify(result=id)

@app.route('/test_json/')
def test_json():
    return jsonify(username='admin',email='admin@ggjjl1.com',id='21')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
