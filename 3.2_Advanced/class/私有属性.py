#!/bin/env python3

# 1:任何以单下划线 _ 开头的都应该是内部是实现
# 2:访问内部属性会导致代码的脆弱性
# 3:下划线开头的同样适用于模块名和模块级别函数
#   如果你看到某个模块名以下划线开头(比如__socket), 那它就是内部实现
#   模块级别函数比如 sys._getframe() 在使用时就得加倍小心

class A:
    def __init__(self):
        self._internal = 0
        self.public = 1
    def public_method(self):
        '''
        A public method
        '''
        pass
    def _internal_method(self):
        '''
        A internal method
        '''
        pass


class B:
    def __init__(self):
        self.__private = 10
    def __private_method(self):
        print("Hello Python")
    def private_method(self):
        self.__private_method()
b = B()
print(b._B__private)
print(b._B__private_method())
print(b.private_method())


class C(B):
    def __init__(self):
        self.__private = 20
    def __private_method(self):
        pass

# 1:这样重命名的目的就是继承 -- 这种属性通过继承是无法被覆盖的.
# 2:此处为 _C_private 和 _C_private_method, 这根B名称是完全不同的
# 3:单下划线和双下划线都是用来命名私有属性,大多数而言,你应该让你的非公共名称以单
#   下划线开头,如果你清除你的代码会涉及到子类,并且有些内部属性应该在子类中隐藏起来
#   那么才考虑使用双下划线方案
# 4:如果你定义的一个变量和某个保留关键字冲突,可以使用单下划线作为后缀


