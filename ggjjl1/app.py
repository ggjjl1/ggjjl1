#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from . import settings


class Ggjjl1(Flask):
    """创建一个Flask应用"""

    def __init__(self, *args, **kwargs):
        kwargs.update(
            {
                "template_folder": settings.FLASK_TEMPLATE_PATH,
                "static_folder": settings.STATIC_ASSETS_PATH,
                "static_url_path": "/static",
            }
        )
        super(Ggjjl1, self).__init__(__name__, *args, **kwargs)
        self.wsgi_app = ProxyFix(self.wsgi_app, x_for=settings.PROXIES_COUNT, x_host=1)
        self.config.from_object("ggjjl1.settings")


def create_app():
    app = Ggjjl1()

    return app
