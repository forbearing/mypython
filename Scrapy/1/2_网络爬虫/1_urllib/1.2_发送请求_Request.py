利用 urlopen() 方法可以实现最基本请求的发起，但这几个简单的参数不足以构建一个完整的请求。如果请求
中需要加入 Headers 等信息，就可以利用更强大的 Request 类来构建。

rest = urllib.request.Request('https://python.org')
resp = urllib.request.urlopen(rest)
print(resp.read().decode('utf-8'))



Request 的构造方法
    class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, 
            unverifiable=False, method=None)
    url:
        用于请求 URL，这是必传参数，其他都是可选参数
    data:
        如果这个参数要传，必须传 bytes(字节流)类型的。如果它是字典，可以先用 urllib.parse
        模块里的 urlencode() 编码
    headers:
        1:一个字典，它就是请求头，我们可以在构造请求时通过 headers 参数直接构造，也可以通过调用
          请求实例的 add_header() 方法添加。
        2:添加请求头最常用的用法就是通过修改 User-Agent 来伪造浏览器，默认的 User-Agent 是
          Python-urllib，比如要伪装成火狐浏览器，可以设置为:
          Morilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11
    origin_req_host:
        请求方的 host 名称或者 IP 地址
    unverifiable:
        表示这个请求是否无法验证，默认是 False，意思就是说用户没有足够权限来选择接收这个请求的
        结果。例如，我们请求了一个 HTML 文档中的图片，但是我们没有自动抓取图像的权限，这时
        unverifiable 的值就是 True
    method:
        是一个字符串，用来指示请求使用的方法，比如 GET、POST 和 PUT 等



示例
    from urllib import request, parse
    url = 'http://httpbin.org/post'
    headers = {
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
                'Host': 'httpbin.org'
                }
    dict = {
            'name': 'Germey'
            }
    data = bytes(parse.urlencode(dict), encoding='utf-8')
    req = request.Request(url=url, data=data, headers=headers, method='POST')

    res = request.urlopen(req)
    print(res.read().decode('utf-8'))
