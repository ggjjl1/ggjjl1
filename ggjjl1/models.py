#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime, Text
from ggjjl1.database import Base
from datetime import datetime


class User(Base):
    """用户"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    password = Column(String(200))
    email = Column(String(120), unique=True)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)

    def __init__(self, name=None, password=None, email=None):
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name


class Article(Base):
    """文章"""
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), unique=True)
    content = Column(Text)
    author = Column(Integer)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)

    def __init__(self, title=None, content=None, author=None):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return '<Article %r>' % self.title
