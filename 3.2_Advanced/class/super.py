#!/bin/env python3

# 想要在子类中调用父类的某个已经被覆盖的方法

# class A:
    # def spam(self):
        # print("A.spam")

# class B(A):
    # def spam(self):
        # print("B.spam")
        # super().spam()

# a = A()
# print(a.spam())
# b = B()
# print(b.spam())


# super() 函数的一个常见用法是在 __init__() 方法中确保父类被真确的初始化
class A:
    def __init__(self):
        self.x =  10
    return x

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 20


# super() 的另一个常见用法出现在覆盖 python 特殊方法的代码中
class Proxy:
    def __init__(self, obj):
        self._obj = ojb
    def __getattr__(self, name):
        return getattr(self._obj, name)
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)
