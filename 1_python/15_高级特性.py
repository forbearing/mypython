生成器
    a = [x for x in range(1,10)]		    # 这是一个列表推导式
    g = (x for x in range(1,10))                    # 这是一个生成器
    next(g)                                         # 生成器只能用一次，还想用要重新生成
    1:一边循环一边计算的的机制，称为生成器：generator
    2:可以通过 next() 函数获得生成器的下一个返回值
        g1 = (x for x in range(1,10))
        next(g1)
    3:通过 next() 函数获得生成器的下一个返回值
    4:没有更多的元素，抛出 StopIteration 的异常
    5:生成器也可以使用 for 循环，因为生成器也是可迭代对象
        g = (x for x in range(1,10))
        for x in g:
            print(x)
    6:生成器的另一种方法
        - yield 函数执行到的地方，会交出 CPU 控制权，停止执行，调用 next 再继续 
        def fib(times):
            n = 0
            a,b = 0,1
            while n < times:
                yield b
                a,b = b,a+b
                n += 1
            return 'done '
        g = fib(5)
        for x in g:
            print(x)
    7:生成器的其他用法
        使用 __next__() 方法
            g.__next__() 等同于 next(g)
        使用 send() 方法
            next() 等价于send(None)
            def gen():
                i = 0
                while i < 5:
                    temp = yield i
                    print(temp)
                    i += 1
    8:生成器的特点
        1:节省内存
        2:迭代到下一次的调用时，所使用的参数都是第一次保留下的



迭代器和可迭代对象
    1:迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置的对象。
      迭代器只能往前不能后退
    2:可迭代对象(Iterable)
        1:集合数据类型，如 list、tuple、dict、set、str 等
        2:生成器和带 yield 的 generator function
    3:如何判断对象可迭代
        from collections import Iterable
        isinstance([],Iterable)
    4:迭代器（Iterator）可以被 next() 函数调用并不断返回下一个值的对象称为迭代器
        from collections import Iterator
        isinstance((x for x in range(10), Iterator))
        iter()函数：将迭代对象转换成迭代器



作用域
    1:命名空间（namespace）
        防止命名冲突
    2:全局变量和局部变量
        1:函数内的变量叫局部变量
        2:函数外的变量叫全局变量
        3:globals() locals()
        4:局部变量和全局变量的冲突（LEGB 原则）
            locals --> enclosing function --> globals --> builtins
        5:查看内建模块 dir(__builtin__)
    

闭包
    1:内部函数对外部函数作用域里变量的引用（非全局变量）则称为内部函数为闭包
    2:闭包的作用就是把外部函数的生命周期延长
    def test(num)
        # 在函数内部定义一个函数，并且这个函数用到了外边函数的变量
        def test_in(num_in)
            return num + num_in
        # 返回的就是闭包的结果
        return test_in

    def func1():
        def func2():
            print("func2")
        return func1
    f = func1()
    print(func1)
    print(func1())
    print(f())

    def outter(num):
        def inner(num_in):
            print("num_in is %d"%num_in)
            return num + num_inw
         return inner
     outter(10)(20)
     f1 = outter(10)
     f2 = f1(20)
     print(f2)
     
     def line_conf(a,b):            # 闭包的应用，一元一次方程
         def line(x):
             return a*x + b
         return line
     line1 = line_conf(1,1)
     line2 = line_conf(4,5)
     print(line1(5))
     print(line2(5))


装饰器
    1:装饰器其实就是一个闭包，把一个函数当作参数然后返回一个替代版函数
    2:装饰器有2个特性
        1:可以把被装饰的函数替换成其他函数
        2:可以在加载模块时候立即执行
    3:装饰器(decorator)功能
        1:引入日志
        2:函数执行时间统计
        3:执行函数前预备处理
        4:执行函数后清理功能
        5:权限校验等场景
        6:缓存
    def w1(func):
        def inner():
            # 验证1
            # 验证2
            # 验证3
            func()
        return inner
    @w1
    def f1():
        print("f1")
    # ==============================================

    def doca(func):
        def wrapper():
            print("func.__name__")
            func
        return wrapper
    def func():
        print("---- func ----")
    ret = doca(func)
    ret()
    @doca
    def func2():
        print("--- func2 ----")
    func2()
    #=================================================

    # 定义函数：完成包裹数据
    def makeBold(fn):
        def wrapped():
            return "<b>" + fn() + "</b>"
        return wrapped
    # 定义函数：完成包裹数据
    def makeItalic(fn):
        def wrapped():
            return "<i>" + fn() + "</i>"
        return wrapped
    @makeBold
    def func1():
        return "hello python 1"
    @makeItalic
    def func2():
        return "hello python 2"
    @makeBold
    @makeItalic
    def func3():
        return "hello python 3"
    print(func1())
    print(func2())
    print(func3())
    # ==============================================

    1:装饰器对无参函数进行装饰
        from time import ctime,sleep
        def timefunc(func):
            def wrappedfunc():
                print("%s called at %s" %(func.__name__, ctime()))
                func()
            return wrappedfunc
        @timefunc
        def foo()
        print("I am foo")
    2:装饰器对有参函数进行装饰
        from time import ctime,sleep
        def timefun(func):
            def wrappedfunc(a,b):
                print("%s called at %s" %(func.__name__, ctime()))
                print(a,b)
                func(a,b)
            return wrappedfunc
        @timefun
        def foo(a,b):
            print(a+b)
    3:装饰器对不定长参数函数进行装饰
        from time import ctime,sleep
        def timefunc(func):
            def wrappedfunc(*arg, **kwargs)
            print("%s called at %s" %(func.__name__, ctime()))
            func(*args, **kwargs)
        return wrappedfunc
        @timefunc
        def foo(a,b,c):
            print(a+b+c)
        foo(3,5,7)
        sleep(2)
        foo(2,4,9)
    4:装饰器对带有返回值的函数进行装饰
        from time import ctime,sleep
        def timefunc(func):
            def wrappedfunc():
                print("%s called at %s" %(func.__name__, ctime()))
                ret = func()
                return ret
            return wrappedfunc
        @timefunc
        def foo():
            print("I am foo")
        @timefun
        def getInfo():
            return 'hello python'
    6:通用装饰器
        1:不定长参数
        2:带返回值
