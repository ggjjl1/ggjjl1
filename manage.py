#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from ggjjl1 import database, create_app

app = create_app()

db = database.db
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
