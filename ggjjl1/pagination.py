#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
自己实现一个分页
传入参数：1.数据库返回对象列表; 2.当前页码; 3.每页展示记录数（默认10）
总记录数 / PAGE_SIZE = 总共多少页
"""

DEFAULT_PAGESIZE = 10


class Pagination(object):
    def __init__(self, *args, **kwargs):
        self.current_page = kwargs.get('current_page', 1)  # 当前页码
        self.page_size = kwargs.get('page_size', DEFAULT_PAGESIZE)  # 每页大小
        self.records = kwargs.get('records', [])
        self.init()

    def init(self):
        self.total_count = len(self.records)
        self.total_pages = self.total_count / self.page_size \
                           + self.total_count % self.page_size
        self.has_prev = self.current_page > 1
        self.has_next = self.current_page < self.total_pages
