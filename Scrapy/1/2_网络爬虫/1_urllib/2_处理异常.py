1:URLError
    1:URLError 类来自 urllib 库的 error 模块，它继承自 OSError 类，是 error 异常模块的基类，由
      request 模块产生的异常可以通过捕获这个类来处理
    2:reason 属性，返回错误的原因

    --------------------------------------------------------------------------------------------

    from urllib import request,error
    try:
        resp = resquest.urlopen("https://www.baidu.com")
    except error.URLError as e:
        print(e.reason)




2:HTTPError
    1:它是 URLError 的子类，专门用来处理 HTTP 请求错误，比如认证请求失败等。
    2:它有三个属性
        code        返回 HTTP 状态吗，比如 404 表示网页不存在，500 表示服务器内部错误等。
        reason      同父类一样，用于返回错误的原因
        headers     返回请求头

    --------------------------------------------------------------------------------------------
    
    from urllib import request,error

    try:
        resp = request.urlopen("https://www.baidu.com/wokao.html")
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers, seq='\n')

    --------------------------------------------------------------------------------------------

    from urllib import request, error

    try:
        response = request.urlopen('https://cuiqingcai.com/index.html')
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers, seq='\n')
    except error.URLError as e:
        print(e.reason)
    else:
        print('Request Successful')

    1:因为 URLError 是 HTTPError 的父类，所以可以先选择捕获子类的错误，再去捕获父类的错误
    2:这样就可以先做到先捕获 HTTPError，如果不是 HTTPError 异常，就会捕获 URLError 异常，输出
      错误原因，最后用 else 来处理正常的逻辑。

    --------------------------------------------------------------------------------------------

    import socket
    import urllib.request
    import urllib.error

    try:
        response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
    except urllib.error.URLError as e:
        print(type(e.reason))
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')

    1:有时候 reason 属性返回的不一定是字符串，也可能是一个对象
