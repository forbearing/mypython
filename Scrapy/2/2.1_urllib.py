1:什么是 Urllib
    Python 内置的 HTTP 请求库
    urllib.request          请求模块
    urllib.error            异常处理模块
    urllib.parse            url 解析模块
    urllib.robotparser      robot.txt 解析模块

2:相比 python2 变化
    python2
        import urllib2
        response = urllib2.urlopen('http://www.baidu.com')
    python3
        import urllib.request
        response = urllib.request.urlopen('http://www.baidu.com')




urlopen

    urllib.request.urlopen(url, date=None, [timeout,]*, cafile=None,
            capath=None, cadefault=False, context=None)

    import urllib.request
    response = urllib.request.urlopen('http://www.baidu.com')
    print(response.read().decode('utf-8'))

    import urllib.request
    import urllib.parse
    data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')
    response = urllib.request.urlopen('http://httpbin.org/post', data=data)
    print(response.read())

    import urllib.request
    response = urllib.request.urlopen('http:///httpbin.org/get', timeout=1)
    print(response.read())

    import socket
    import urllib.request
    import urllib.error
    try:
        response = urllib.request.urlopen('http://httpbin.org', timeout=0.1)
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print("TIME OUT")




响应

    响应类型
    import urllib.request
    response = urllib.request.urlopen('https://www.python.org')
    print(type(response))

    状态码, 响应头
    import urllib.request
    response = urllib.request.urlopen('https://www.python.org')
    print(response.status)
    print(response.getheaders())
    print(response.getheader('Server'))




Request

    import urllib.request
    request = urllib.request.Request('https://python.org')
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf8'))

    from urllib import request, parse2
    url = 'http://httpbin.org/post'
    headers = {
            'User-Agent': 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)',
            'Host': 'httpbin.org'
            }
    dict = {
            'name': 'Germey'
            }
    data = bytes(parse.urlencode(dict), encoding='utf8')
    req = request.Request(url=url, data=data, headers=headers,
            method='POST')
    res = request.urlopen(req)
    print(res.read().decode('utf8'))

    from urllib import request,parse
    url = 'http://httpbin.org/post'
    dict = {
            'name': 'Germey'
            }
    data = bytes(parse.urlencode(dict),encoding='utf8')
    req = request.Request(url=url, data=data, method='POST')
    req.add_header('User-Agent': 'Mozilla/4.0(compatible; MSIE 5.5; Windows N')
    res =  request.urlopen(req)
    print(res.read().decode('utf8'))




Handler

    代理
    import urllib.request
    proxy_handler = urllib.request.ProxyHandler({
        'http': 'http://127.0.0.1:1080'
        'https': 'https://127.0.0.1:1080'
        })
    opener = urllib.request.build_opener(proxy_handler)
    response = opener.open('http://httpbin.org/get')
    print(response.read())

    Cookie
    import urllib.request, http.cookiejar
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    res = opener('http://www.baidu.com')
    for item in cookie:
        print(item.name + ' = ' + item.value)

    import http.cookiejar, urllib.request
    filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    res = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)

    import http.cookiejar, urllib.request
    filename = 'cookie.txt'
    cookie = http.cookiejar.LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    res = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)

    import http.cookiejar,urllib.request
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    res = opener.open('https://www.baidu.com')
    print(res.read().decode('utf8'))




异常处理

    from urllib import request, error
    try:
        res = request.urlopen('https://hybfkuf.com/index.html')
    except  error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
    except error.URLError as e:
        print(e.reason)
    else:
        print("Request Successfully")

    import socket
    import urllib.request
    import urllib.error
    try:
        res = url.request.urlopen('https://www.baidu.com', timeout=0.01)
    except urllib.error.URLError as e:
        print(type(e.reason))
        if isinstance(e.reason, socket.timeout):
            print("TIME OUT")



URL 解析

    === urlparse
    urllib.parse.urlparse(urlstring, scheme="", allow_fragments=True)

    from urllib.parse import urlparse
    result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
    print(type(result), result)

    from urllib.parse import urlparse
    result = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
    print(result)

    from urllib.parse import urlparse
    result = urlparse('http://www.baidu.com/index.html;user?id=5#commmend',
            allow_fragments=False)
    print(result)

    from urllib.parse import urlparse
    result = urlparse('http://www.baidu.com/index.html#comment',
            allow_fragments=False)
    print(result)

    === urlunparse
    from urllib.parse import urlunparse
    data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
    print(urlunparse(data))

    === urljoin
    from urllib.parse import urljoin
    print(urljoin('http://www.baidu.com', 'FAQ.html'))
    print(urljoin('http://www.baidu.com', 'https://hybfkuf.com/FAQ.html'))
    print(urljoin('http://www.baidu.com/about.html',
        'https://hybfkuf.com/FAQ.html'))
    print(urljoin('http://www.baidu.com/about.html',
        'https://hybfkuf.com/FAQ.html?question=2'))
    print(urljoin('http://www.baidu.com?wd=abc', 'https://hybfkuf.com/index.php'))
    print(urljoin('www.baidu.com', '?category=2#comment'))
    print(urljoin('www.baidu.com#comment', '?category=2'))

    === urlencode
    from urllib.parse import urlencode
    params = {
            'name': 'germey',
            'age': 22
            }
    base_url = 'http://www.baidu.com'
    url = base_url + urlencode(params)
    print(url)
