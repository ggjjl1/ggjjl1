#!usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

from ggjjl1.views import blog, auth

app = Flask(__name__)

app.register_blueprint(blog.bp)
app.register_blueprint(auth.bp)
app.add_url_rule('/', endpoint='index')


def format_datetime(value, format="%d %b %Y %I:%M %p"):
    """Format a date time to (Default): d Mon YYYY HH:MM P"""
    if value is None:
        return ""
    return value.strftime(format)


app.jinja_env.filters['formatdatetime'] = format_datetime

# if __name__ == '__main__':
#     app.run(host="0.0.0.0")
