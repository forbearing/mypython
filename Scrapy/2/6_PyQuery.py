1:PyQuery
    - 强大又灵活的网页解析库. 如果你觉得正则表达式写起来太麻烦, 如果你觉得 BeautifulSoup
      语法太难记, 如果你熟悉 jQuery 的语法, 那么 PyQuery 就是你的绝佳选择
    - pip install pyquery


初始化
    === 字符串初始化
    html = '''
    <div>
        <ul>
            <li class="item-0">first item</li>
            <li class="item=1"<a href="link2.html"second item</a></li>
            <li class="item-0 active"><a href="link3.html"<span class="bold" third item  </span></a></li>
            <li class="item-1 active"><a href="link4.html"fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
    '''
    from pyquery import PyQuery as pq
    doc = pq(html)
    print(doc('li'))

    === URL 初始化
    from pyquery import PyQuery as pq
    doc = pq(url="https://www.baidu.com")
    print(doc('head'))

    === 文件初始化
    from pyquery import PyQuery as pq
    doc = pq(filename='demo.html')
    print(doc('li'))



基本 CSS 选择器
    html = '''
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
    '''
    from pyquery import PyQuery as pq
    doc = pq(html)
    print(doc("#container .list li"))



查找元素
    === 子元素
    from pyquery import PyQuery as pq
    doc = pq(html)
    items = doc('.list')
    print(type(items))
    print(items)
    lis = items.find('li')
    print(type(lis))
    print(lis)

    lis = items.children()
    print(type(lis))
    print(lis)

    lis = items.children('.active')
    print(lis)

    === 父类型
    from pyquery import PyQuery as pq
    doc = pq(html)
    items = doc('.list')
    container = items.parent()
    print(type(container))
    print(container)

    container = items.parents()
    print(type(container))
    print(container)

    parent = iterms.parents('.wrap')
    print(parent)

    === 兄弟元素
    html = '''
    <div class="wrap">
        <div id="container">
            <ul class="list">
                <li class="item-0">first item</li>
                <li class="item-1"><a href="link2.html">second item</a></li>
                <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
                <li class="item-1 active"><a href="link4.html">fourth item</a></li>
                <li class="item-0"><a href="link5.html">fifth item</a></li>
            </ul>
        </div>
    </div>
    '''
    from pyquery import PyQuery as pq
    doc = pq(html)
    li = doc('.list .item-0.active')
    print(li.siblings())
    print(li.sibling('.active'))



遍历
    === 单个元素
    from pyquery import PyQuery as pq
    doc = pq(html)
    li = doc('.item-0.active')
    print(li)

    from pyquery import PyQuery as pq
    doc = pq(html)
    lis = doc('li').items()
    print(type(lis))
    for li in lis:
        print(li)



获取信息
    === 获取属性
    a = doc('.item-0.active a')
    print(a)
    print(a.attr('href'))
    print(a.attr.href)

    === 获取文本
    a = doc('.item-0.active a')
    print(a)
    print(a.text())

    === 获取 HTML
    li = doc('.item-0.active')
    print(li)
    print(li.html())



DOM 操作
    === addClass, removeClass
    doc = pq(html)
    li = doc('.item-0.active')
    print(li)
    li.removeClass('active')
    print(li)
    li.addClass('active')

    li = doc('.item-0.active')
    print(li)
    li.remove_class('active')
    print(li)
    li.add_class('active')
    print(li)

    === attr, css
    li = doc('.item-0.active')
    print(li)
    li.attr('name', 'link')
    print(li)
    li.css('font-size', '14px')
    print(li)

    === remove
    html = '''
    <div class="wrap">
        Hello World
        <p>This is a paragraph.</p>
    </div>
    '''
    from pyquery improt PyQuery as pq
    doc = pq(html)
    wrap = doc('.wrap')
    print(wrap.text())
    wrap.find('p').remove()
    print(wrap.text())



伪类选择器
    html = '''
    <div class="wrap">
        <div id="container">
            <ul class="list">
                <li class="item-0">first item</li>
                <li class="item-1"><a href="link2.html">second item</a></li>
                <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
                <li class="item-1 active"><a href="link4.html">fourth item</a></li>
                <li class="item-0"><a href="link5.html">fifth item</a></li>
            </ul>
        </div>
    </div>
    '''
    from pyquery improt PyQuery as pq
    doc = pq(html)
    li = doc('li:first-child')
    li = doc("li:last-child")
    li = doc("li:nth-child(2)")
    li = doc("li:gt(2)")
    li = doc("li:nth-child(2n)")
    li = doc("li:contains(second)")
    print(li)
