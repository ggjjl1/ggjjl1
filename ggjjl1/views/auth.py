#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from ggjjl1.database import db_session
from ggjjl1.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        email = request.form['email']
        error = None

        if not name:
            error = '用户名不能为空！'
        elif not password:
            error = '密码不能为空！'
        elif User.query.filter(
                User.name == name or User.email == email
        ).first() is not None:
            error = '用户或邮箱已存在！'

        if error is None:
            user = User(name, generate_password_hash(password), email)
            db_session.add(user)
            db_session.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        error = None

        user = User.query.filter(User.name == name).first()

        if user is None:
            error = '用户名不存在！'
        elif not check_password_hash(user['password'], password):
            error = '密码错误！'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter(User.id == user_id).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
