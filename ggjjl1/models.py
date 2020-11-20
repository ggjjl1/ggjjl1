#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import check_password_hash, generate_password_hash
from ggjjl1.database import db


class User(db.Model):

    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    _password = db.Column("password", db.String(200), nullable=False)
    email = db.Column(db.String(100), unique=True)
    create_time = db.Column(
        db.DateTime, nullable=False,server_default=db.func.current_timestamp()
    )
    update_time = db.Column(
        db.DateTime, nullable=False,server_default=db.func.current_timestamp()
    )

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def __init__(self, name=None, password=None, email=None):
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name


class Post(db.Model):

    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.ForeignKey(User.id), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    create_time = db.Column(
        db.DateTime, nullable=False, server_default=db.func.current_timestamp()
    )
    update_time = db.Column(
        db.DateTime, nullable=False, server_default=db.func.current_timestamp()
    )

    def __init__(self, title=None, body=None, author_id=None):
        self.title = title
        self.body = body
        self.author_id = author_id

    def __repr__(self):
        return '<Post %r>' % self.title
