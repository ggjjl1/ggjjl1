from flask import Flask
from flask_migrate import Migrate

from . import settings
from .filter import reverse_filter, mkdown


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = settings.SECRET_KEY

    from ggjjl1.database import db
    db.init_app(app)

    from ggjjl1.views import blog, auth
    app.register_blueprint(blog.bp)
    app.register_blueprint(auth.bp)
    app.add_url_rule('/', endpoint='index')
    app.add_url_rule('/auth/register', endpoint='register')
    app.add_url_rule('/auth/login', endpoint='login')

    # 模板过滤器
    app.jinja_env.filters['reverse'] = reverse_filter
    app.jinja_env.filters['mkdown'] = mkdown

    return app
