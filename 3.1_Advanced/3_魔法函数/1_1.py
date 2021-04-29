#!/usr/bin/env python3

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list;
    def __getitem__(self, item):
        return self.employee[item]

company = Company(['tom', 'bob', 'jane'])
company1 = company[:2]

for em in company:
    print(em)

for em in company1:
    print(em)

# for 循环 company 对象时, python 解释器就会调用 __getitem__ 函数,直至抛出异常.
