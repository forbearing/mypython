#!/usr/bin/env python3

from collections.abc import Sized

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    def __len__(self):
        return len(self.employee)

company = Company(['hybfkuf', 'hyb'])
print(hasattr(company, "__len__"))

print(isinstance(company, Sized))
