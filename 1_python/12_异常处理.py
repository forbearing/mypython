1:捕获异常
    1:try 嵌套，如果里面的 try 没有捕获到这个异常，那么外面的 try 会接受这个异常并进行处理，
      如果外面的 try 没有捕获到，那么再传递
    try:
        print(a)
    except (NameError,ZeroDivisionError) as ex:
        print("NameError")
        print(ex)
        # Exception 表示捕获所有异常
    else:
        print("没有异常的情况下")
    finally:
        print("最终要执行的代码，不管前面是否出现 exception")

2:自定义异常
    class PasswordException(Exception):
        def __init__(self,password,length):
            self.password = password
            self.length = length
        def __str__(self):
            return "密码不符合规范"
    def reg(username,password):
        if len(password) < 6:
            raise PasswordException(password,6)
    try:
        reg('zs','123')
    except (PasswordException,Exception) as ex:
        print(ex)
