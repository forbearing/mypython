1:对象的三个特征
    身份: 对象在内存当中的地址
        id(a)   # 显示对象的内存地址
    类型:
        type(a)
    值
        print(a)

2:None (全局只有一个)
    a = None
    b = None
    id(a) == id(b)

3:数值
    int float complex bool

4:迭代类型

5:序列类型
    list
    bytes bytearray memoryview(二进制序列)
    range
    tuple
    str
    array

6:映射(dict)

7:集合
    set
    frozenset

8:上下文管理类型
    with

9:其他
    1:模块类型
        from import (这两个关键字也是类型)
    2:class 和实例
    3:函数类型
    4:方法类型
    5:代码类型
    6:object 对象
    7:type 对象
    8:elipsis 类型 (省略号的类型)
    9:notimplemented 类型
        面向对象的高级的设计时会用到
