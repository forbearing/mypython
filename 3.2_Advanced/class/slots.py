#!/bin/env python3

# 创建大量对象节省内存方法
#   __slots__ 是内存优化工具,也可以作为一个封装工具来防止用户给实例增加新的属性

class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

