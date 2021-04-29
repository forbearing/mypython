#!/usr/bin/env python3

class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)
# 查看类属性的查找顺序
