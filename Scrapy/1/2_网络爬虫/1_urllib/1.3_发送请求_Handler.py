概述
    1:Request 虽然可以构造请求，但是处理不了你一些更高级的操作（比如 Cookie 处理，代理设置等）
    2:Hander，我们可以把它理解为各种处理器，有专门处理登录验证的，有处理 Cookie 的，有处理代理
      设置的。利用它们，我们几乎可以做到 HTTP 请求中所有的事情。
    3:urllib.request 模块里面的 BaseHandler 类，它是所有其他 Handler 的父类，它提供了最基本的方法
      例如 default_open()、protocol_request() 等
    4:各种 Handler 子类继承这个 BaseHandler 类
        HTTPDefaultErrorHandler 
            用于处理 HTTP 响应错误，错误都会抛出 HTTPError 类型的异常
        HTTPRedirectHandler
            用于处理重定向
        HTTPCookieProcessor
            用于处理 Cookies
        ProxyHandler:
            用于设置代理，默认代理为空
        HTTPPasswordMgr
            用于管理密码，它维护了用户名和密码的表
        HTTPBasicAuthHandler
            用于管理认证，如果一个链接打开时需要认证，那么可以用它来解决认证问题u
    5:另一个比较重要的类就是 OpenerDirector，我们可以称为 Opener，之前使用的 urlopen() 方法其实
      就是 urllib 为我们提供的一个 Opener
    6:Handler 构建 Opener




1:验证 HTTPBasicAuthHandler

    from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
    from urllib.error import URLError

    username = 'username'
    password = 'password'
    url = 'http://localhost:5000/'

    p = HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, url, username, password)
    auth_handler = HTTPBasicAuthHandler()
    opener = build_opener(auth_handler)

    try:
            result = opener.open(url)
                html = result.read().decode('utf-8')
    except URLError as e:
            print(e.reason)

    1:首先实例化 HTTPBasicAuthHandler 对象，其参数是 HTTPPasswordMgrWithDefaultRealm 对象
    2:它利用 add_password() 添加用户名和密码，这样就建立了一个处理验证的 Handler
    3:接下来，利用这个 Handler 并使用 build_openner() 方法构建一个 Opener, 这个 Opener 在发送
      请求时就相当于已经验证成功了
    4:接下来，利用 Opener 的 open() 方法打开链接，就完成验证了，获取的结果就是验证后的
      页面源代码内容




2:代理 ProxyHandler
    
    from urllib.request import ProxyHandler
    from urllib.error import URLError
    from urllib.request import build_opener
    proxy_handler = ProxyHandler({
                'http': 'http://127.0.0.1:1087'
                })
    opener = build_opener(proxy_handler)
    try:
        resp = opener.open('https://www.baidu.com')
            print(resp.read().decode('utf-8'))
    except URLError as e:
            print(e.reason)

    1:ProxyHandler 其实就是一个字典
    2:利用这个 Handler 及 build_opener() 方法构造一个 Opener，之后发送请求即可。




3:Cookie HTTPCookieProcessor
    
    from http.cookiejar import CookieJar
    from urllib.request import build_opener
    from urllib.request import URLError
    from urllib.request import HTTPCookieProcessor

    cookie = CookieJar()
    handler = HTTPCookieProcessor(cookie)
    opener = build_opener(handler)
    resp = opener.open('http://www.baidu.com')
    for item in cookie:
            print(item.name+"="+item.value))

    1:我们必须声明一个 CookieJar 对象，接下来，就需要 HTTPCookieProcessor 来构建一个 Handler，
    2:最后利用 build_opener() 方法构建出 Opener, 执行 open() 函数即可

    ---------------------------------------------------------------------------------------

    import http.cookiejar
    from urllib.request import HTTPCookieProcessor
    from urllib.request import build_opener
    from urllib.request import URLError

    filename = 'cookies.txt'
    cookie = http.cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    resp = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)

    1:CookieJar 换成 MozillaCookieJar，它在生成文件时会用到，是 CookieJar 的子类，可以用来处理 
      Cookies 和文件相关的事件，比如读取和保存 Cookies，可以将 Cookies 保存成 
      Mozilla 型浏览器的 Cookies 格式。

    ---------------------------------------------------------------------------------------

    import http.cookiejar
    from urllib.request import URLError
    from urllib.request import HTTPCookieProcessor
    from urllib.request import build_opener

    cookie = http.cookiejar.LWPCookieJar()
    handler = http.request.HTTPCookieProcessor(cookie)
    opener = http.request.build_opener(handler)
    resp = opener.open('http://www.baidu.com')
    print(resp.read().decode('utf-8'))

    1:LWPCookieJar 同样可以读取和保存 Cookies，但是保存的格式和 MozillaCookieJar 不一样。它会保存
      成 libwww-perl(LWP) 格式的 Cookies 文件
