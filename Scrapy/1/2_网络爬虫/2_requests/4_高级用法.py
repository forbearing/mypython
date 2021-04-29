1:文件上传
    1:requests 可以模拟提交一些数据。假如有的网站需要上传文件，我们可以用它来实现。

    import requests
    files = {'file': open('favicon.ico', 'rb')}
    r = requests.post('http://httpbin.org/post', files=files)
    print(r.text)




2:Cookies
    1:urllib 处理 Cookies 写法比较复杂，而有了 requests，获取和设置 Cookies 只需要一步就可以完成

    import requests
    r = requests.get('http://www.google.com')
    print(r.cookies)
    for key,value in r.cookies.items():
        print(key + ' = ' + value)

    2:r.cookies 是 RequestCookieJar 类型，然后用 items() 方法将其转换为元祖组成的列表，遍历输出
      每一个 Cookie 的名称和值，实现 Cookie 的遍历解析




3:会话维持
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)

    1:利用 Session，我们可以模拟同一个会话而不用担心 Cookies 的问题。它通常用于模拟登录成功之后
      再进行下一步的操作
    2:Session 在平常用得非常广泛，可以用于模拟在一个浏览器中打开同一站点的不同页面




4:SSL 证书验证
    1:请求一个 HTTPS 站点，但是证书验证错误的页面

    import request
    resonse = requests.get('https://www.12306.cn', verify=False)
    print('response.status_code')
    # 不过会发出警报，它建议我们给它指定证书。我们可以通过设置忽略警告的方式来屏蔽这个警告
    
    import request
    from request.packages import urllib3
    urllib3.disable_warnings()
    response = requests.get('https://www.12306.cn', verify=False)
    print(response.status_code)

    import logging
    import requests
    logging.captureWarnings(True)
    response = requests.get('https://www.12306.cn', verify=False)
    print(response.status_code)
    # 或者通过捕获警告到日志的方式忽略警告

    import reuqest
    response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
    print('response.status_code')
    # 我们也可以指定一个本地证书用作客户端证书，这可以是单个文件（包含密钥和文件）
    #   或一个包含两个文件路径的元祖
    # 注意本地证书的 key 必须是解密状态，加密状态的 key 是不支持的




5:代理设置
    import requests
    proxies = {
            "http": "http://10.10.1.10:3128"
            "https": "http://10.10.1.10:1080"
            }
    requests.get("http://www.taobao.com", proxies=proxies)

    import requests
    proxies = {
            "http": "http://user:password@10.10.1.10.3128"
            }
    requests.get('http://www.taogao.com', proxies=proxies)
    # 若代理需要使用 HTTP Basic Auth, 可以使用类似 http://user:password@host:port 
    # 的语法来设置代理
    
    pip3 install 'request[socks]'
    import requests
    proxies = {
            'http': 'socks5://user:password@host:port'
            'https': 'socks5://user:password@host:port'
            }
    requests.get('http://taobao.com', proxies=proxies)




6:超时设置
    import requests
    r = requests.get('https://www.taobao.com', timeout=1)
    print(r.status_code)
    1:实际上,请求分为两个阶段,即链接(connect) 和读取(read)
    2:上面设置的 timeout 将用作连接和读取这两者的 timeout 总和
    3:如果分别指定,就可以传入一个元组
        r = requests.get('https://www.taobao.com', timeout(5,11,30))
    4:如果想要永久等待,可以直接将 timeout 设置为 None, 或不设置直接留空,因为默认是 None
        r = requests.get('http://www.taobao.com', timeout=None)
        r = requests.get('http://www.taobao.com')




7:身份认证
    import requests
    from requests.auth import HTTPBasicAuth
    r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
    print(r.status_code)

    1:如果参数都传入一个 HTTPBasicAuth 类,就显得有点麻烦, 所以 requests 提供了一个更简单的
      写法,可以直接传入一个元组,它会默认使用 HTTPBasicAuth 这个类来认证
    import requests
    r = requests.get('http://localhost:5000', auth=('username','password'))

    1:rerquest 还提供了其他认证方式, 如 OAuth 认证,不过此时需要安装 oath 包,安装命令如下
        pip3 install requests_oauthlib
    import requests
    from requests_oauthlib import OAuth1
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
            'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
    requests.get(url, auth=auth)




8:Prepared Request
    1:前面介绍 urllib 时,我么可以将请求表示为数据结构,其中各个参数都可以通过一个 Request 
      对象来表示. 这在 requests 里同样可以做到,这个数据结构叫做 Prepared Request
    2:引入 Request, 用 url,data,headers 参数构建了一个 Request 对象,这时需要载调用
      Session 的 prepare_request() 方法将其转换为一个 Prepared Request 对象.然后调用
      send() 方法发送即可, 可以达到同样的 POST 请求效果
    3:有了 Request 这个对象,就可以将请求当做独立的对象来看待, 这样在进行队列调度时会非常方便
    from requests import Request, Session
    url = 'http:///httpbin.org/post'
    data = {
            'name': 'germey'
            }
    headers = {
            'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) 
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
            }
    s = Session()
    req = Request('POST', url, data=data, headers=headers)
    prepped = s.prepare_requests(req)
    r = s.send(prepped)
    print(r.text)
