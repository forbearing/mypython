type 
    生成一个类
    返回对象是什么类型的

a=1
b="abc"
print(type(1))
print(type(b))
print(type(int))
print(type(str))


class Student():
    pass
stu = Student()
print(type(stu))
print(type(Student))
    type -> int -> 1
    type -> class -> obj
    - type 是用来生成类对象的, 平常我们使用的实例是由我们自己定义的类或者
      内置的类来生成的实例


class Student:
    pass
class MyStudent(Student):
    pass
stu = Student()
print(MyStudent.__bases__)
print(Student.__bases__)
print(type.__bases__)
print(object.__bases__)
    - object 是所有类的基类
    - type 也是一个类, 同时也是一个对象, 其父类为 object
