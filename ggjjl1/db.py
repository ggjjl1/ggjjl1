#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import MySQLdb

def connect_db():
    """连接数据库"""
    try:
        db = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="ggjjl1", charset="utf8")
    except:
        print("连接数据库成功")
    return db

def init_db():
	pass
