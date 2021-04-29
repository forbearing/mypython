概述
    1:urllib 提供了 parse 模块, 它定义了 URL 的标准接口，例如实现 URL 个部分的抽取、
      合并以及链接转换
    2:它支持如下协议的 URL 处理：file, ftp, gopher, hdl, http, https, imap, mailto, mms, news, 
      nntp, prospero, rsync, rtsp, rtspu, sftp, sip, sips, snews, svn, svn+ssh, telnet, wais




1:urlparse()
    1:该方法可以实现 URL 的识别和分段
    2:一个标准的连接格式： scheme://netloc/path;params?query#fragment
    3:一个标准的 URL 都会复合这些规则，利用 urlparse() 方法可以将它拆分开来
    
    from urllib.parse import urlparse
    result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
    print(type(result), result)

    1:urlparse() 方法将其拆分成6个部分，scheme, netloc, path, params, query, fragment
    2:scheme: 代表协议
    3:netloc: 域名
    4:path: 访问路径
    5:params: 代表参数
    6:query: 查询条件，一般用作 GET 类型的 URL
    7:fragment: 锚点，用于直接定位页面内部的下拉位置

    -------------------------------------------------------------------------------------------

    urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
    1:urlstring: 这是必填项，即待解析的 URL
    2:scheme: 它是默认的协议(比如 http,https 等).假如这个链接没有带协议信息,会将这个作为默认的协议
      result = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
    3:allow_fragments: 是否忽略 fragment, 如果它被设置为 False, fragment 部分就会被忽略，它会被
      解析为 path, parameters 或者 query 的一部分，而 fragment 部分为空
      result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', 
              allow_fragments=False)




2:urlunparse()
    1:它接受的参数是一个可迭代的对象，但是它的长度必须是6我，否则会抛出参数数量不足或者过度的问题
    
    from urllib.parse import urlunparse
    data =[’http'' '刷w.baidu.com', 'index.html’P ’user’3 ’a=6', 'comment')]
    print(urlunparse(data))




3:urlsplit()
    1:和 urlparse() 方法相似，只不过它不再单独解析 params 这一部分，只返回5个结果

4:urlunsplit()
    1:与 urlunparse() 类似，它也是将链接各个部分分组合成完整链接的方法，传入的参数也是一个迭代
      对象，例如列表、元祖等。唯一的区别就是长度必须为5

    from urllib.parse import urlunsplit
    data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
    print(urlunsplit(data))




5:urljoin()
    1:urlunparse() 和 urlunsplit() 方法，可以完成链接的合并，不过前提是要有特定长度的对象，链接的
      每一部分都要清洗分开
    2:urljoin()方法，我们可以提供一个 base_url(基础链接) 作为第一个参数，将新的链接作为第二个参数
      该方法会分析 base_url 的 scheme、netloc、path 这3个内容并对新链接缺失的部分进行补充，
      最后返回结果。
    
    urljoin('http://www.baidu.com', 'FAQ.html')
    urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html')
    urljoin('www.baidu.com', '?category=2#comment')
    urljoin('www.baidu.com#comment', '?category=2')




6:urlencode()
    1:在构造 GET 请求参数的是否非常有用
    2:这个方法非常常用，有时为了更加方便地构造参数，我们会事先用字典来表示，要转化为 URL 的
      参数，只需要调用该方法即可

    from urllib.parse import urlencode
    params={
            'name': 'germey',
            'age': 22
            }
    base_url = 'http://www.baidu.com'
    url = base_url + urlencode(params)
    print(url)




7:parse_qs()
    1:有了序列化，必须就有反序列化。如果我们有一串 GET 请求参数，利用 parse_qs() 方法，就可以
      将其转回字典。
    
    query = 'name=hyb&age=22'
    print(parse_qs(query))

8:parse_qsl()
    1:用于将参数转换为元祖组成的列表
    2:返回结果为一个列表，列表中的每一个元素都是一个元祖，元祖的第一个内容是参数名，
      第二个内容是参数值

    query = 'name=hyb&age=22'
    print(parse.qsl(query))





9:quote()
    1:此方法将内容转化为 URL 编码的格式。URL 中带有中文参数时，有时可能会导致乱码的问题,
      此时用这个方法可以将中文字符转化为 URL 编码
    
    from urllib.parse import quote
    keyword = '壁纸'
    url = 'https://www.baidu.com/s?wd=' + quote(keyword)
    print(url)

10:unquote()
    1:对 URL 解码
    
    from urllib.parse import unquote
    url = 'http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
    print(unquote(url))
