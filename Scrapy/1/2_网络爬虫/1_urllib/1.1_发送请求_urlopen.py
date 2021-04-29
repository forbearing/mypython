urlopen
    urllib.request.urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, 
                cadefault=False context=None)
    res = urllib.request.urlopen('https://www.python.org')
            res.status
            res.gethreaders()
            res.getheader('Server')
    
    
    
1:data 参数
    data 参数可选。如果要添加该参数，并且如果它是字节流编码格式的内容，即 bytes 类型，则需要
    通过 bytes() 方法转化。另外，如果传递了这个参数，则它的请求方式就不再是 GET 方法，
    而是 POST 方法

    data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')
    res = urllib.request.urlopen('http://httpbin.org/post', data=data)
    print(res.read())
        # urllib.parse.urlencode() 将字典转换为字符串



2:timeout 参数
    timeout 参数用于设置超时时间，单位为秒，意思是如果请求超出了设置的时间，还没有得到响应，
    就会抛出异常。如果不指定该参数，就会使用全局默认时间。它支持 HTTP、HTTPS、FTP 请求

    res = urlopen.request.urlopen('http://httpbin.org/get', timeout=0.1)

    import socket
    import urllib.request
    import urllib.error
    try:
        response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('TimeOut')


3:其他参数
    context
        它必须是 ssl.SSLContext 类型，用来指定 SSL 设置
    cafile, capath 
        分别制定 CA 证书和它的路径，这个在请求 HTTPS 链接时会有用
    cadefault
        弃用，其默认值为 False
