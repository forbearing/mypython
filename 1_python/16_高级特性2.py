类装饰器
    1:装饰器函数其实是这样一个接口约束，它必须接受一个 callable 对象作为参数，然后返回一个
      callable 对象
    2:一般 callable 对象都是函数，但也有例外。只要某个对象重写了 __call__() 方法，那么这个
      对象就是 callable 的
        class Test(object):     # class Test():
            def __call__(self):
                print("call me")
            t = Test()
            t()
    1:类装饰器示例
        class User:
            def __init__(self, func):
                self.__func = func
            def __call__(self):
                print("类装饰器")
                self.__func()
        @User   # 生成一个 User 对象，会调用 __init__ 方法，并且把下面的函数作为参数传进去
        def test():
            print("Just testing")
        test()  # 调用 Test 的一个对象的 __call__ 方法


对象池
    1:Python 为了优化速度，使用小整数[-5,257] 对象池，避免为了整数频繁申请和销毁内存
    2:同理，单个字符也提供对象池，常驻内存
    3:每一个大整数，均创建一个新的对象
    4:对于字符串，单个单词，不可修改，默认开启 inten 机制，采用引用计数机制公用对象，
      引用计数器为0 则销毁
        a = 'hello'
        b = 'hello'
        id(a), id(b)            # 内存地址相同
        a = 100
        b = 100
        id(a), id(b)            # 内存地址相同
        a = 'hello python'
        b = 'hello python'
        id(a), id(b)            # 内存地址不同，不是单词，因为中间有空格


垃圾收集GC
    1:Grabage collection(垃圾回收)
        为新生成的对象分配内存
        识别哪些垃圾对象
        从垃圾对象那回收内存
    2:python 采用的是引用计数机制为主，标记-清除和分代收集两种机制为辅的策略
    3:python 里每一个东西都是对象，它们的核心就是一个结构体: PyObject
    4:引用计数机制的优点
        - 简单
        - 实时性：一旦没有引用，内存就直接释放了，不用像其他机制等到特定时机。
          实时性还带来了一个好处：处理回收内存的时间分摊到了平时
    5:引用计数机制的缺点
        - 维护引用计数消耗资源
        - 循环引用
    6:导致引用计数 +1 的情况
        - 对象被创建，例如 a = 23
        - 对象被引用，例如 b = a
        - 对象被作为参数，传入到一个函数中，例如 func(a)
        - 对象作为一个元素，存储在容器中，例如 list1 = [a,a]
    7:导致引用计数 -1 的情况
        - 对象的别名被显式销毁，例如 del a
        - 对象的别名被赋予新的对象，例如 a = 24
        - 一个对象离开它的作用域，例如 f 函数执行完毕时，func 函数中的局部变量（全局变量不会）
        - 对象所在的容器被销毁，或从容器中删除对象
    8:查看一个对象的引用计数
        import sys
        a = 'hello python'
        sys.getrrefcount(a)
    9:引用计数的缺陷是循环引用的问题
        import gc
        class ClassA():
            def __init__(self):
                print('ClassA')
        def f2():
            while True:
                c1 = ClassA()
                c2 = ClassA()
                c1.t = c2
                c2.t = c1
                del c1
                del c2
            # 把 pytonn 的 gc 关闭
            gc.disable()
            f2()
            执行 f2(), 进程占用的内存会不断增大
        1:有三种情况会触发垃圾回收
            1:调用 gc.collect()
            2:当 gc 模块的计数器达到阀值的时候
            3:程序退出的时候
        2:垃圾回收的对象会在 gc.garbage 列表里面
        3:gc.get_threshold() 获取的 gc 模块中自动执行垃圾回收的频率
        4:gc.get_count() 获取当前自动执行垃圾回收的计数器，返回一个长度为3的列表
        5:gc.collect([generation]) 显式进行垃圾回收，可以输入参数，0代表只检查第一代的对象，
          1代表检查一、二代的对象，2代表检查一、二、三代的对象，如果不传参数，执行一个 full
          collection，也就是等于传2，返回不可达(unreachable objects) 对象的数目
        6:gc 模块唯一处理不了的是循环引用的类都有 __del__ 方法，所以项目中要避免定义 
          __del__ 方法


内建属性
    __init__    构造初始化函数          创建实例后，赋值时使用，在 __new__ 后
    __new__     生成实例所需属性        创建实例时
    __class__   实例所在的类            实例.__class__
    __str__     实例字符串表示，可读性  print(实例)
    __repr__    实例字符串表示，准确性
    __del__     析构                    del 删除实例
    __dict__    实例自定义属性
    __doc__     类文档，子类不继承
    __getattribute__        属性访问拦截器
    __bases     类的所有父类构成元素
    1:属性访问拦截器
        class School(object):
            def __init__(self,subject1):
                self.subject1 = subject1
                self.subject2 = 'cpp'
            # 重写属性访问拦截器
            def __getattribute__(self,obj):
                if obj == 'subject1':
                    return 'redirect python'
                else:
                    return object.__getattribute__(self,obj)
        s = School('python')
    2:使用属性访问拦截器的坑
        class Person(object):
            def __getattribute__(self,obj):
                print("---test---")
                if obj.startwith("a"):
                    return 'haha'
                else:
                    return self.test
            def test(self):
                print("heihei")
        t = Person()
        t.a         # 返回 haha
        t.b         # 会让程序死掉 


内建方法
    dir(__builtins__)
    range(start,stop[,step])        
        # 计数从 start 开始，默认是从0开始i，到 stop 结束，但不包括 stop，每次条约间距默认为1
    map(function,sequence[,sequence, ...])      # 根据提供的函数对指定序列做映射
    filter(function or None, sequence)          # 指定定序列执行过滤操作
    reduce(function,sequence[,initial])         # 对参数序列中元素进行积累


集合
    1:集合与之前列表、元素类似，可以存储多个数据，但是这些数据是不重复的，并没没有顺序
    2:集合对象支持的运算：
      union(并集)
      intersection(交集)
      difference(差集)
      sysmmetric_difference(对称差集)


functools
    1:functools 是 python2.5 被引入的，一些工具函数放在此包里
      import functools
      dir(functools)
    2:partial 函数（偏函数）
        - 把一个函数的某些参数设置默认值，返回一个新的函数，调用这个新函数会更简单
    3:wraps 函数
        - 使用装饰器时，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变）
        - wraps 的装饰器可以消除这样的副作用
        def showargs(*args, **kwargs):
            print(args)
            pritn(kwargs)
        import functools
        p1 = functools.partial(showargs,1,2,3)
        p1()
        p2 = functools.partial(showargs,'python','hello python')
        p2()
        p3 = functools.partial(showargs,a='python',b='hello python')
        p3()
        ==================================================================================
        import functools
        def note(func):
            "note function"
            @functools.wraps(func)
            def wrapper():
                "wrapper function"
                print("note something")
                return func()
            return wrapper
        @note
        def test():
            "test function"
            print("I am test")
        test()
        print(test, doc)


常用模块
    === 标准模块 ===
    builtins                内建函数默认加载
    os                      操作系统接口
    sys                     Python 自身的运行环境
    functools               常用的工具
    json                    编码和解码 JSON 对象
    logging                 记录日志、调试
    multiprocessing         多进程
    threading               多线程拷贝
    time                    时间
    datetime                日期和时间
    calendar                日历
    hashlib                 加密算法
    random                  生成随机数
    re                      字符串正则匹配
    socket                  标准的 BSD Socket API
    copy                    
    === 第三方模块 ===
    requests                使用的是 urllib3，继承了 urllib2 的所有特性
    urllib                  基于 http 的高层库
    scrapy                  爬虫
    beautifulsoup4          HTML/XML 的解析器
    celery                  分布式任务调度模块
    redis                   缓存
    Pillow(PIL)             图像处理
    xlsxwriter              仅写 excel 功能，支持xls, 2013 或更早版本
    xlrd                    仅读 excel 功能
    elasticsearch           全文搜索引擎
    pymysql                 数据库连接库
    mongoengine/pymongo     mongodbpython 接口
    matplotlib              画图
    numpy/scipy             科学计算
    django/tornado/flask    web框架
    xmitodict               xml 转 dict
    SimpleHTTPServer        简单地 HTTP Server，不使用 Web 框架
    gevent                  基于协程的 Python 网络库
    fabric                  系统管理


pdb 调试
    1:执行时调试
        python -m pdb file.py
    2:交互式调试
        import pdb
        pdb.run('testfun(args)')
    3:程序里埋点
        import pdb
        pdb.set_trace()


