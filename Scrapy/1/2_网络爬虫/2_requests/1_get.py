1:示例
    
    import requests
    r = requests.get('http://httpbin.org/get')
    print(r.text)

    -----------------------------------------------------------------------------------------

    import requests
    data = {
            'name': 'hyb',
            'age': 22
            }
    r = requests.get('http://httpbin.org/get', params=data)

    -----------------------------------------------------------------------------------------

    import requests
    r = requests.get('http://httpbin.org/get')
    print(type(r.text()))
    print(r.json())
    print(type(r.json()))

    1:网页的返回类型实际上是 str 类型，但是它很特殊，是 JSON 格式的。
    2:如果想直接解析返回结果，得到一个字典的话，可以直接调用 json() 方法
    3:如果返回结果不是 JSON 格式，便会出现解析错误，抛出 json.decoder.JSONDecodeError 异常




2:抓去二进制数据
    import requests
    r =requests.get('https://github.com/favicon.ico')
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)
    
    1:如果要抓取图片、音频、视频等文件




3:添加 headers
    import requests
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) ApplewebKit/537.36 \
                (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
            }
    r = requests.get('https://www.zhihu.com/explore', headers=headers)
    print(r.text)

    1:如果不传递 headers，有些网站，比如知乎，就不能正常请求
