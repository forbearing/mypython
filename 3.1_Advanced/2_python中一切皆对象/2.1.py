#!/usr/bin/env python3

a=1
b='abc'
print(type(1))
print(type(b))
print(type(int))
print(type(str))

class Student:
    pass
class MyStudent(Student):
    pass

stu=Student()
print(type(stu))
print(type(Student))
print(type(object))
print(int.__bases__)
print(str.__bases__)
print(Student.__bases__)
print(MyStudent.__bases__)
print(type.__bases__)
print(object.__bases__)
~
