1:概述
    1:urllib 确实有一些不方便的地方，比如处理网页验证和 Cookie 时，需要写 Opener 和 Handler
      来实现这些操作，因此有了更为强大的库 requests
    2:有了它，Cookies、登录验证、代理设置等操作都不是事
    3:urllib 库中的 urlopen() 方法实际上是以 GET 方法请求网页，而 request 中相应的方法是 get()方法




示例
    import requests
    r = requests.get('https://www.baidu.com/')
    print(type(r))
    print(r.status_code)
    print(type(r.txt))
    print(r.txt)
    print(r.cookies)

    r = requests.post('http://httpbin.org/post')
    r = requests.put('http://httpbin.org/put')
    r = requests.delete('http://httpbin.org/delete')
    r = requests.head('http://httpbin.org/get')
    r = requests.options('http://httpbin.org/get')
