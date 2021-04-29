#!/usr/bin/env python3


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    def __getitem__(self, item):
        return self.employee[item]
    def __len__(self):
        return len(self.employee)

company = Company(['tom', 'bob', 'jane'])

a = ['a', 'b']
a.extend(company)
print(a)
