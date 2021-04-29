#!/usr/bin/env python3

class Person:
    school_name = "BeijingDaxue"
    """
    Document
    """

class Student(Person):
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    stu = Student('hybfkuf')
    # print(stu.school_name)
    # print(stu.__dict__)
    # print(Student.__dict__)
    # print(Person.__dict__)
    print(dir(Person))
    print(dir(Student))
    print(dir(stu))
