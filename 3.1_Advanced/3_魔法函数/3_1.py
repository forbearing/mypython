#!/usr/bin/env python3

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    def __str__(self):
        return ",".join(self.employee)
    def __repr__(self):
        return "__repr__"

company = Company(['Tom', "Jam", "Bob"])
print(company)
company


__str__
    1:开发模式下使用
        print(company)

__repr__
    1:company 相当于 repr(company) 相当于 company.__repr__()
