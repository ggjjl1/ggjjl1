#!/usr/bin/env python
# -*- coding: utf-8 -*-

from markdown import markdown


def reverse_filter(s):
    """
    测试，反转列表或字符串
    """
    return s[::-1]


def mkdown(s):
    """
    解析mkdown文本，转化为普通html
    """
    html = markdown(s)
    return html
