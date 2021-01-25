import os
import click
from flask import Flask
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@127.0.0.1:3306/ggjjl1'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "dev")

    from ggjjl1.database import db
    db.init_app(app)

    from ggjjl1.views import blog, auth
    app.register_blueprint(blog.bp)
    app.register_blueprint(auth.bp)
    app.add_url_rule('/', endpoint='index')
    app.add_url_rule('/auth/register', endpoint='register')
    app.add_url_rule('/auth/login', endpoint='login')

    return app
