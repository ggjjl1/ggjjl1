#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from ggjjl1 import create_app
from ggjjl1.database import db

app = create_app()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
