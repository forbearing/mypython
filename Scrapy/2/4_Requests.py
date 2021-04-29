1:介绍
    1:Request 是用 Python 语言编写的, 基于 urllib, 采用 Apache2 Licensed
      开源协议的 HTTP
    2:它比 urllib 更加方便, 可以节省我们大量的工作,完全满足 http 测试需求
    3:一句话, python 实现的简单易用的 HTTP 库
    4:安装 pip3 install requests




request
    import requests
    response  = requests.get('https://www.baidu.com/')
    print(type(response))
    print(type(response.text))
    print(response.status_code)
    print(response.text)
    print(response.cookies)

    === 各种请求方式
    import requests
    requests.post('http://httpbin.org/post')
    requests.put('http://httpbin.org/put')
    requests.delete('http://httpbin.org/delete')
    requests.head('http://httpbni.org/get')
    requests.get('http://httpbin.org/get')




GET 请求
    === 基本写法
    import request
    response = requests.get('http://httpbin.org/get')
    print(response.text)

    === 带参数 GET 请求
    import requests
    response = requests.get('http://httpbin.org/get?name=hybfkuf&age=23')
    print(response.text)

    import requests
    data = {
            'name': 'hybfku',
            'age': 23
            }
    response = requests.get('http://httpbin.org/get', params=data)
    print(response.text)

    === 解析 json
    import requests
    import json
    response = requests.get('http://httpbin.org/get')
    print(response.json())
    print(json.loads(response.text))

    === 获取二进制数据
    import requests
    response = requests.get('https://github.com/favicon.ico')
    print(type(response.text), type(response.content))
    print(response.text)
    print(response.content)

    import requests
    response = requests.get('https://github.com/favicon.ico')
    with open('favicon.ico', 'wb') as f:
        f.write(response.content)
        f.close()

    === 添加 headers
    import requests
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
            }
    res = requests.get('https://www.zhihu.com/explore', headers=headers)
    print(res.text)




POST 请求
    import requests
    data = {
            'name': 'hybfkuf',
            'age': 23
            }
    res = requests.post('http://httpbin.org/post', data=data)
    print(res.text)




响应
    === response 属性
    import requests
    response = requests.get('https://www.baidu.com')
    print(type(response.status_code), response.status_code)
    print(type(response.headers), response.headers)
    print(type(response.cookies), response.cookies)
    print(type(response.url), response.url)
    print(type(response.history), response.history)

    === 状态码判断
    res.status_code == 200
    res.status_code == requests.codes.ok




高级用法
    === 文件上传
    import requests
    files = {'file': open('favicon.ico', 'rb')}
    response = requests.post('http://httpbin.org/post', files=files)
    print(response.text)

    === 获取 cookie
    import requests
    response = requests.get('https://www.baidu.com')
    print(response.cookies)
    for key, value in response.cookies.items():
        print(key + '=' + value)

    === 会话维持
    import requests
    requests.get('http://httpbin.org/cookies/set/number/123456789')
    response = requests.get('http://httpbin.org/cookies')
    print(response.text)            # 拿不到刚才设置的 cookie

    import requests
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    response = s.get('http://httpbin.org/cookies')
    print(response.text)            # 可以 拿到刚才设置的 cookie

    === 证书验证
    import requests
    response = requests.get('https://www.12306.cn')
    print(response.status_code)

    import requests
    from requests_packages import urllib3
    urllib3_disable_warnings()
    response = requests.get('https://www.12306.cn', verify=False)
    print(response.status_code)

    import requests
    response = requests.get('https://www.12306.cn',
            cert=('/path/server.cert','/path/key'))
    print(response.status_code)

    === 代理设置
    import requests
    proxies = {
            'http': 'http://127.0.0.1:8743',
            'https': 'https://127.0.0.1:8743'
            }
    response = requests.get('https://www.taobao.com', proxies=proxies)

    import requests
    proxies = {
            'http': 'http://user:password@127.0.0.1:8743',
            }
    response = requests.get('https://www.taobao.com', proxies=proxies)
    print(response.status_code)

    pip install 'requests[socks]'

    import requests
    proxies = {
            'http': 'socks5://127.0.0.1:8742',
            'https': 'socks5://127.0.0.1:8742'
            }
    response = requests.get('https://www.taobao.com', proxies=proxies)
    print(response.status_code)

    === 超时设置
    import requests
    from requests.exceptions import ReadTimeout
    try:
        response = requests.get('https://www.taobao.com', timeout=1)
        print(response.status_code)
    except ReadTimeout:
        print("TIMEOUT")

    === 认证设置
    import requests
    from requests.auth import HTTPBasicAuth
    r = requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user','123'))
    print(r.status_code)

    === 异常处理
    import requests
    from requests.exceptions import ReadTimeout, HTTPError, RequestException
    try:
        response = requests.get('https://taobao.com', timeout=0.5)
        print(response.status_code)
    except ReadTimeout:
        print("Timeout")
    except HTTPError:
        print("Http Error")
    except RequestException:
        print('Error')




总结
    1:推荐使用 lxml 解析库，必要时使用 html.parser
    2:标签选择筛选功能弱但是速度快
    3:建议使用 find(), find_all() 查询匹配单个结果或者多个结果
    4:如果对 CSS 选择器熟悉建议使用 select()
    5:记住常用的获取属性和问本值的方法
