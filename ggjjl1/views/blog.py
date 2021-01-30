#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from jinja2 import TemplateNotFound

from ggjjl1.database import db
from ggjjl1.models import Post
from ggjjl1 import settings

bp = Blueprint('blog', __name__)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(
        Post.create_time.desc()
    ).paginate(page, per_page=5, error_out=True)
    try:
        return render_template('blog/index.html', pagination=pagination)
    except TemplateNotFound:
        abort(404)


@bp.route('/post/<int:id>')
def detail(id):
    post = Post.query.filter(Post.id == id).first()

    return render_template(
        'blog/detail.html',
        post=post,
    )


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = '标题不能为空！'

        if error is not None:
            flash(error)
        else:
            p = Post(title, body, author_id=1)
            db.session.add(p)
            db.session.commit()
            return redirect(url_for('blog.index'))

    return render_template(
        'blog/create.html'
    )


@bp.route("/api")
def test_api():
    return {
        "username": "Tim",
        "theme": "default",
        "image": "http://ggjjl1.com/test-image001.jpg",
    }
