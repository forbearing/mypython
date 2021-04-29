1:简介
    1:借助网页的结构和属性等特性来解析网页
    2:Beautiful Soup 就是 Python 的一个 HTML 或 XML 的解析库,可以用它来方便地从网页中提取数据
    3:Beautiful Soup 提供了一些简单的, Python 式的函数来处理导航,搜索,修改分析树等功能
    4:自动将输入文档转换成 Unicode 编码,输出文档转换为 UTF-8 编码,你不需要考虑编码格式,
      除非文档没有指定一个编码方式,这时你仅仅需要说明一下原始编码方式就可以了.
    5:Beautiful Soup 已成为和 lxml, html6lib 一样出色的 Python 解释器,为用户灵活地提供了
      不同的解析策略或强劲的速度




2:解析器
    1:Beautiful Soup 在解析时实际上依赖解析器, 它除了支持 Python 标准库中的 HTML 解析器外,
      还支持一些第三方解析器(比如 lxml), 下面列出了 Beautiful Soup 支持的解析器
    2:lxml 解析器有解析 HTML 和 XML 的功能,而且速度快,容错能力强,所以推荐使用

    1:Python 标准库
        1:使用方法: BeautifulSoup(markup, "html.parser")
        2:优势: Python 内置标准库,执行速度适中,文档容错能力强
    2:lxml HTML 解析器
        1:使用方法: BeautifulSoup(markup, "lxml")
        2:优势: 速度快,文档容错能力强
    3:lxml XML 解析器
        1:使用方法: BeautifulSoup(markup, 'xml')
        2:优势: 速度快, 唯一支持 XML 的解析器
    4:html5lib
        1:使用方法: BeautifulSoup(markup, 'html5lib')
        2:优势: 最好的容错性,以浏览器的方式解析文档,生成 HTML5 格式的文档




3:基本使用
    1:prettify() 方法把要解析的字符串以标准的缩进格式输出. 输出结果中包含 body 和 html
      节点,这是 BeautifulSoup 自动更正的结果,不是由 prettify() 方法做的,是在
      初始化 BeautifulSoup 时就完成了
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class='title' name='dromous'><b>The Dormouse's story</b></p>
    <p class='story'>Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id='link2'>Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id='link3'>Tillier</a>;
    and they lived at the bottom of a well. </P>
    <p class="story">...</p>
    """
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.prettify())
    print(soup.title.string)
    # 首先声明变量 html, 它时一个 HTML 字符串, 这不是一个而完整的 HTML 字符串,因为 body
    # 和 html 节点没有闭合, 作为第一个参数传给 BeautifulSoup 对象,该对象的第二个参数为
    # 解析器的类型(这里是 lxml), 此时就完成了 BeautfulSoup 对象的初始化,然后赋值给 soup 变量




4:节点选择器
