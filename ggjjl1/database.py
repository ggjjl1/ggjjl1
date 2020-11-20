#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

# engine = create_engine('mysql://root:123456@127.0.0.1:3306/ggjjl1?charset=utf8',echo=True)
# db_session = scoped_session(
#     sessionmaker(
#         autocommit=False,
#         autoflush=False,
#         bind=engine
#     )
# )
#
# Base = declarative_base()
# Base.query = db_session.query_property()
#
#
# def init_db():
#     Base.metadata.create_all(bind=engine)


db = SQLAlchemy()
# Column = partial(db.Column, nullable=False)
