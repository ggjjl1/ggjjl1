#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from jinja2 import TemplateNotFound
from flask_paginate import Pagination, get_page_parameter

from ggjjl1.database import init_db, db_session
from ggjjl1.models import Article
from ggjjl1 import settings

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    page = request.args.get(get_page_parameter(), default=1, type=int)
    articles = Article.query.all()
    pagination = Pagination(
        page=page, total=len(articles), record_name='articles', bs_version="3_3", alignment='center'
    )
    try:
        return render_template(
            'blog/index.html',
            articles=articles,
            pagination=pagination,
            title=settings.SITE_NAME,
            logo_name=settings.LOGO_NAME
        )
    except TemplateNotFound:
        abort(404)


@bp.route('/article/<int:id>')
def detail(id):
    article = Article.query.filter(Article.id == id).first()

    return render_template(
        'blog/detail.html',
        article=article,
        title=settings.SITE_NAME,
        logo_name=settings.LOGO_NAME
    )


@bp.route('/post', methods=('GET', 'POST'))
def post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        error = None

        if not title:
            error = '标题不能为空！'

        if error is not None:
            flash(error)
        else:
            article = Article(title, content, author=1)
            db_session.add(article)
            db_session.commit()
            return redirect(url_for('blog.index'))

    return render_template(
        'blog/post.html',
        logo_name=settings.LOGO_NAME
    )
