#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

# 网站名称
SITE_NAME = "ggjjl1's website"

# 数据库地址
DATABASE_NAME = 'root'
DATABASE_PASS = '123456'
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345678@127.0.0.1:3306/ggjjl1"

# Flask应用密钥
SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
