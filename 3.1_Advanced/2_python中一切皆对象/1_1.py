#!/usr/bin/env python3

def func(name="hybfkuf-function"):
    print(name)

class Person(object):
    def __init__(self):
        print("hybfkuf-class")

my_func = func
my_class = Person
#my_func()
#my_class()

my_list = []
my_list.append(my_func)
my_list.append(my_class)

for item in my_list:
    print(item())               # my_func 会有两个一个返回值 None 和 print 返回值
