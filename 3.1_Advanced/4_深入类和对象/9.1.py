#!/usr/bin/env python3

class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")
        super().__init__()

if __name__ == "__main__":
    b = B()


# 既然我们重写了 B 的构造函数, 为什么还要调用 super?
# super 到底执行顺序是什么
