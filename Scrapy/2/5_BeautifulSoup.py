1:BeautifulSoup
    - 灵活又方便的网页解析库，处理高效，支持多种解析器
    - 利用它不用编写正则表达式即可方便的实现网页信息的提取
    - pip install beautifulsoup4

2:解析库
    python 标准库
        使用方法: BeautifulSoup(markup, 'html.parser')
        优势: Python 内置的标准库、执行速度适中、文档容错能力强
        劣势: Python 2.7 or 3.2.2 之前的版本中文容错能力差
    lxml HTML 解析库
        使用方法: BeautifulSoup(markup, 'lxml')
        优势: 速度快、文档容错能力强
        劣势: 需要安装 C 语言库
    lxml XML 解析库
        使用方法: BeautifulSoup(markup, 'xml')
        优势: 速度快、唯一支持 XML 的解析器
        劣势: 需要安装 C 语言库
    html5lib
        使用方法: BeautifulSoup(markup, 'html5lib')
        优势: 最好的容错性，以浏览器的方式解析文档、生成 HTML 格式的文档
        劣势: 速度慢、不依赖外部扩展




基本使用
    html = '''
        <html><head><title>The Document's story</title></head>
        <body>
        <p class="title" name="dromouse"><b>The hybfkuf's storage</b></p>
        <p class="story">Once upon a time there were three title sistes
        <a href="http://www.hybfkuf.com/wokao" id="link1"</a>
        <a href="http://www.hybfkuf.com/hello" id="link2"</a>
        <a href="http://www.hybfkuf.com/linux" id="link3"</a>
        and they lived at the botton of a weel</p>
        <p class="python">...</p>
    '''
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.prettify())
    print(soup.title.string)




标签选择器
    === 选择元素
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title)
    print(type(soup.title))
    print(soup.head)
    print(soup.p)

    === 获取名称
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title.name)

    === 获取属性
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.p.attrs['name'])
    print(soup.p['name'])
    print(soup.p['class'])

    === 获取内容
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.p.string)

    === 嵌套选择
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.head.title.string)

    === 子节点和子孙节点
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.p.contents)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.p.children)
    for i, child in enumerate(soup.p.children):
        print(i,child)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.p.descendants)
    for i, child in enumerate(soup.p.descendants):
        print(i,child)

    === 父节点和祖先节点
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.a.parent)
    print(list(enumerate(soup.a.parents)))

    === 兄弟节点
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(list(enumerate(soup.a.next_siblings)))
    print(list(enumerate(soup.a.previous_siblings)))




标准选择器
    find_all(name, attrs, recursive, text, **kwargs)
    可根据标签名、属性、内容查找文档

    html = '''
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class='list' id='list-1'>
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''

    === name
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find_all('ul'))
    print(type(soup.find_all('ul')[0]))

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    for ul in soup.find_all('ul'):
        print(ul.find_all('li'))

    === attrs
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find_all(attrs={'id':'list-1'}))
    print(soup.find_all(attrs={'name':'elements'}))

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find_all(id='list-1'))
    print(soup.find_all(class_='element'))

    === text
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find_all(text='Foo'))

    === find(name, attrs, recursive, text, **kwargs)
    返回单个元素，find_all 返回所有元素

    === find_parents() find_parent()
    find_parents() 返回所有祖先节点
    find_parent() 返回所有直接父节点

    === find_next_siblings() find_next_sibling()
    find_next_siblings() 返回所有兄弟节点
    find_next_sibling() 返回第一个兄弟节点

    === find_previous_siblings() find_previous_sibling()
    find_previous_siblings() 返回前面所有兄弟节点
    find_previous_sibling() 返回前面第一个兄弟节点

    === find_all_next() find_next()
    find_all_next() 返回节点后所有符合条件的节点
    find_next() 返回第一个符合条件的节点

    === find_all_previous() find_previous()
    find_all_previous() 返回节点后所有符合条件的节点
    find_previous() 返回第一个符合条件的节点




CSS 选择器
    - 通过 select() 直接插入 CSS 选择器即可完成选择
    - 类名前加 ”.“ ID名前加 #

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.select('.panel .panel-heading'))
    print(soup.select('ul li'))
    print(soup.select('#list-2 .element'))
    print(type(soup.select('ul')[0]))

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    for ul in soup.select('ul'):
        print(ul.select('li'))

    === 获取属性
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    for ul in soup.select('ul'):
        print(ul['id'])
        print(ul.attrs['id'])

    === 获取内容
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    for ul in soup.select('li'):
        print(ul.get_text())
