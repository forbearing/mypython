1:装饰器
    1:概念
        - 是一个闭包，把一个函数当作参数，返回一个替代版的函数，本质上
          就是一个返回函数的函数
        - @outer 相当于 func=outer(func)
          使用 @ 符号将装饰器应用到函数，python2.4支持使用 @ 符号 

    ---
    def decorate(func):
        def myWrapper(age):
            if age < 0:
                age = abs(age)
            func(age)
        return myWrapper
    @decorate
    def func(age):
        print("my age is: %s" %age)
    func(10)
    func(-10)

    ---
    from functools import wraps
    def a_new_decorate(a_func):
        @wraps(a_func)
        def wrapTheFunction():
            print("Before function")
            a_func()
            print("After function")
        return wrapTheFunction
    @a_new_decorate
    def a_function_requiringg_decoration():
        print("I'm doing a boring job")
    a_function_requiringg_decoration()
    print(a_function_requiringg_decoration.__name__)
    @wraps 接受一个函数来进行装饰，并加入了复制函数的名称、注释文档、参数列表等功能。

    --- 装饰器蓝本
    from functools import wraps
    def decorator_name(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not can_run:
                return "Function will not run"
            return f(*args, **kwargs)
        return decorated

    @decorator_name
    def func():
        return("Function is running")

    can_run = True
    print(func())

    can_run = False
    print(func())

    --- 使用场景: 授权(Authorization)
    # 装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。
    # 它们被大量使用于Flask和Django web框架中
    from functools import wraps
    def requires_auth(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if not auth or not check_auth(auto.username, auth.password):
                authenticate()
            return f(*args, **kwargs)
        return decorated

    --- 使用场景: 日志(Logging)
    from functools import wraps
    def logit(func):
        @wraps(func)
        def with_logging(*args, **kwargs):
            print(func.__name__ + "was called")
            return func(*args, **kwargs)
        return with_logging
    @logit
    def addition_func(x):
        return x + x
    result = addition_func(4)



2:带参数的装饰器
    ---
    from functools import wraps
    def logit(logfile='out.log'):
        def logging_decorator(func):
            @wraps(func)
            def wrapped_function(*args, **kwargs):
                log_string = func.__name__ + "was called"
                print(log_string)
                witch open(logfile, 'a') as opened_file:
                    opened_file.write(log_string + '\n')
                return func(*args, **kwargs)
            return  wrapped_function
        return logging_decorator

    @logit()
    def myfunc1():
        pass
    myfunc1()       # 一个叫做 out.log 的文件出现了，里面的的内容就是上面的字符串
    @logit(logfile="func2.log")
    def myfunc2():
        pass
    myfunc2()       # 一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串

    ---
    from functools import wraps
    def logit(logfile="out.log"):
        def myDecorator(func):
            @wraps(func)
            def myWrapper(*args, **kwargs):
                log_string = func.__name__ + " was called"
                with open(logfile, 'a') as opened_file:
                    opened_file.write(log_string)
                return func(*args, **kwargs)
            return myWrapper
        return myDecorator

    @logit()
    def func1():
        pass
    func1()

    @logit(logfile="mylogfile.log")
    def func2():
        pass
    func2()



3:装饰器类
    from functools import wraps
    class logit(object):
        def __init__(self, logfile='out.log'):
            self.logfile = logfile
        def __call__(self, func):
            @wraps(func)
            def wrapped_function(*args, **kwargs):
                log_string = func.__name__ + "was called"
                print(log_string)
                with open(self.logfile, 'a') as opened_file:
                    opened_file.write(log_string + '\n')
                self.notify()
                return func(*args, **kwargs)
            return wrapped_function
        def notify(self):
            pass
    # 这种实现有一个附加的优势、在比嵌套函数的方式更整洁，而且包裹一个函数还是使用
    # 以前的语法
    @logit()
    def func1():
        pass

    --- 给 logit 创建子类，来添加 email 的功能
    class email_logit(logit):
        '''
         一个logit的实现版本，可以在函数调用时发送email给管理员
        '''
        def __init__(self, email="admin@myproject.com", *args, **kwargs):
            self.email = email
            super(email_logit, self).__init__(*args, **kwargs)
        def notify(self):
            pass

4: @staticmethod @classmethod
    1:解释
        1:一般来说，要使用某个类的方法，需要先实例化一个对象再调用方法，而使用
          @staticmethod @classmethod, 就不需要实例化，直接 "类名.方法名()" 来调用
        2:@staticmethod, 静态方法
          不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样
        3:@classmethod, 类方法
          也不需要self参数，但第一个参数需要是表示自身类的cls参数
        4:如果在 @staticmethod 中调用类的一些属性和方法，只能直接 "类名.属性名" 或 
          "类名.方法名"。而 @classmethod 因为持有 cls 参数，可以调用类的属性，类的方法，
          实例化对象等。避免硬编码
