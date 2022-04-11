#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

# 网站名称
SITE_NAME = "ggjjl1's website"

# 数据库地址
SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL", "mysql+mysqlconnector://root:123456@127.0.0.1:3306/ggjjl1")

# Flask应用密钥
SECRET_KEY = os.environ.get("SECRET_KEY", "bn^k3s!(!c((u_b@n8u1ju(f3hqm(5ym79yg_ctfv-!37&_0d$")
