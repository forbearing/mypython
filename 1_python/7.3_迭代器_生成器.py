1:迭代器概念
    1:迭代是Python最强大的功能之一，是访问集合元素的一种方式。
    2:迭代器是一个可以记住遍历的位置的对象
    3:迭代对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
    4:迭代器只能往前不能退后
    5:迭代器有两个基本方法：iter() 和 next()
    6:字符串、列表或元素对象都可以用于创建迭代器
    7:可以直接作用于 for 循环的对象统称为可迭代对象, 可以使用 isinstance() 去
      判断一个对象是否是 Iterable 对象
    8:可以直接作用于 for 循环的数据类型一般分两种
        1:集合数据类型 list, tuple, dict, set, str
        2:generator: 包括生成器和带 yield 的 generator  function

    ---
    #from collections import Iterable
    from collections.abc import Iterable
    from collections.abc import Iterator
    s1 = {1,2,3,4}
    iter1 = iter(s1)
    isinstance(s1, Iterable)                                # True
    isinstance(s1, Iterator)                                # False
    isinstance(iter1, Iterable)                             # True
    isinstance(iter1, Iterator)                             # True
    print(isinstance((x for x in range(10)), Iterable))

    ---
    list1 = [1,2,3,4]
    it1 = iter(list1)
    print(next(iter1))
    print(next(iter1))

    for x in iter1:
        print(x, end=" ")

    while True:
        try:
            print(next(iter1))
        except StopIteration:
            sys.exit()

2:创建一个迭代器
    1:把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 
    2:__iter__() 方法返回一个特殊的迭代器对象，这个迭代器对象实现了 __next__() 方法并
      通过 StopIteration 异常标识迭代的完成。
    3:__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象

    class MyNumbers:
        def __iter__(self):
            self.a = 1
            return self
        def __next__(self):
            x = self.a
            self.a += 1
            return x
    myclass = MyNumbers()
    myiter = iter(myclass)
    print(next(myiter))
    print(next(myiter))

    - StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 
      方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。

    class MyNumbers:
        def __iter__(self):
            self.a = 1
            return self
        def __next__(self):
            if self.a <= 20:
                x = self.a
                self.a += 1
                return x
            else:
                raise StopIteration
    myclass = MyNumbers()
    myiter = iter(myclass)
    for x in myiter:
        print(x)


3:生成器概念
    1:使用了 yield 函数的函数称为生成器(generator)
    2:跟普通函数不同，生成器是一个返回迭代器的函数，只能用于迭代操作。更简单点理解
      生成器就是一个迭代器。
    3:在调用生成器止运行的过程中，每次遇到 yield 时，函数会暂停并保存当前运行的所有信息
      返回 yield 的值，并在下一次调用 next() 方法时从当前位置继续进行。
    4:调用一个生成器，返回的是一个迭代器对象

    import sys
    def fib(n):
        a,b,counter = 0,1,0
        while True:
            if counter > n:
                return
            yield a
            a,b = b,a+b
            counter +=1
    f = fib(10)
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()



=== 2020-6-2
    1:可迭代对象包含迭代器
    2:如果一个对象拥有 __iter__ 方法，其是可迭代对象，如果一个对象拥有 next 方法，其是迭代器
    3:定义可迭代对象，必须实现 __iter__ 方法，定义迭代器，必须实现 __iter__ 和 next 方法
    4:生成器是一种特殊的迭代器，它的返回值不是通过 return，而是 yield

    from collections.abc import Iterable
    from collections.abc import Iterator

    class MyList(object):                           # 定义可迭代对象
        def __init__(self, num):
            self.data = num                         # 上边界
        def __iter__(self):
            return MyListIterator(self.data)        # 返回可迭代对象的迭代器类的实例

    class MyListIterator(object):                   # 定义迭代器类，其是 MyList 可迭代对象的迭代器类
        def __init__(self, data):
            self.data = data                        # 上边界
            self.now = 0                            # 当前迭代值，初始为0
        def __iter__(self):
            return self                             # 返回该对象的迭代器类的实例，因为自己是迭代器，返回 self
        def __next__(self):
            while self.now < self.data:
                self.now += 1
                return self.now - 1
            raise StopIteration

    mylist = MyList(5)
    print(type(mylist))
    print(isinstance(mylist, Iterable))
    print(isinstance(mylist, Iterator))
    my_list_iter = iter(mylist)
    print(type(my_list_iter))
    print(isinstance(my_list_iter, Iterable))


    ===
    x = [1,2,3]
    from collections.abc import Iterable
    from ccollection.abc import Iterator
    print(isinstance(x, Iterable))
    print(isinstance(x, Iterator))
    
    ===
    迭代器是一个带状态的对象，你能在调用 next() 方法的时候返回容器中的下一个值，任何
    实现了 __iter__ 和 __next__() 方法的对象都是迭代器。__iter__ 返回迭代器自身，
    __next__返回容器中的下一个值

    # 生成无限序列
    from itertools import count
    counter = count(start=13)
    for x in counter:
        print(x)
    # 从一个有限序列生成无限序列
    from itertools import cycle
    colors = cycle(['red', 'white', 'bule'])
    next(colors)

    ===
    fib 就是一个普通的函数，它特殊的地方在于函数中没有 return 关键字，函数的返回值是一个
    生成器对象。当执行 f=fib() 返回的是一个生成器对象，此时函数中的代码并不会执行，
    只是显示或隐式地调用 next 的时候才会真正执行里面的代码
    def fib():
        prev, cur = 0, 1
        while True:
            yield cur
            pre, cur = cur, cur + pre
    f = fib()
    list(islice(f, 0, 10))

    ===
    y = (x*x for x in range(10))            生成式表达式，还有一个列表推导式
    
