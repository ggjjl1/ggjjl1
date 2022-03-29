#!/usr/bin/env python
# -*- coding: utf-8 -*-

from markdown import markdown


def reverse_filter(s):
    """
    测试，反转列表或字符串
    """
    return s[::-1]


def mkdown(text):
    """
    解析mkdown文本，转化为普通html
    """
    html = markdown(text, extensions=[
        'markdown.extensions.fenced_code',  # 解析代码块
        'markdown.extensions.codehilite',  # 代码高亮.codehilite
    ], safe_mode=True, enable_attributes=False)
    return html
