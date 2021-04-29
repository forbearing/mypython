#!/usr/bin/env python3

class A:
    aa = 1                  # aa 为类变量
    def __init__(self, x, y):
        self.x = x          # self 为 A 的类实例
        self.y = y          # self.x 和 self.y 为实例变量

a = A(2,3)
print(a.x, a.y, a.aa)
print(A.aa)
# 属性的查找方式: 先查找对象变量,如果查找不到,向上查询类变量.
#print(A.x)                  # 报错


a = A(22,33)
A.aa = 11                   # 修改类变量, 类变量是所有实例共享的
a.aa = 100                  # 在对象上新建一个 aa 变量
print(a.x, a.y, a.aa)       # 从下往上查找原则, 先查到 a.aa 而不是 A.aa
print(A.aa)
