#usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import datetime
import MySQLdb
from flask import Flask, render_template, request, redirect, url_for, jsonify
from ggjjl1 import db

app = Flask(__name__)

"""
网站名称
"""
blog_name = "gjl's website."
logo_name = blog_name


"""
将时间戳转换为日期
"""
def stamp2date(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")

print stamp2date(int(time.time()))


"""
从数据库中获取最新的文章
"""
def get_articles():
    conn = db.connect_db()
    cursor = conn.cursor()
    try:
        # 执行 sql 语句
        print("开始获取数据库中的文章")
        cursor.execute("select id,title,content,tag,user_id,ctime from article where valid=1")
        articles  = [dict(id=row[0], title=row[1], content=row[2], tag=row[3], user_id=row[4], ctime=row[5]) for row in cursor.fetchall()]
        # 释放数据库连接
        cursor.close()
        db.close()
    except:
        print("查询数据库失败")
    return articles



@app.route('/')
def index():
    articles = get_articles()
    return render_template('index.html', blog_name=blog_name, logo_name=logo_name, articles=articles)

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
