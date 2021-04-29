提取到节点之后，最终的目的是提取节点所包含的信息，比较重要的信息有两类：
一是获取属性，二是获取文本。



1:获取属性
    html = '''
    <div class="wrap">
    <div id="container">
    <ul class="list">
    <li class="item-0">first item</li>
    <li class="item-1"><a href="link2.html">second items</a></li>
    <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
    <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
    </div>
    </div>
    '''
    from pyquery import PyQuery as pq
    doc = pq(html)
    a = doc('.item-0 a')
    print(a, type(a))
    print('\n')
    print(a.attr('href')) 
    # 首先选中 class 为 item-0 和 active 的 li 节点的 a 节点，它的类型是 PyQuery 类型。
    # 然后调用 attr() 方法。在这个方法中传入属性的名称，就可以得到这个属性值了。

    from pyquery import PyQuery as pq
    doc = pq(html)
    a = doc('a')
    print(a, type(a))
    print(a.attr('href'))
    print(a.attr.href)
    # 当返回结果中包含多个时，调用 attr 方法，只会得到第一个节点的属性
    # 遇到这种情况，如果想要获取 a 节点的所有属性，就要使用遍历

    from pyquery import PyQuery as pq
    doc = pq(html)
    a = doc('a')
    for item in a.items():
        print(item.attr('href'))
    # 在进行属性获取时，可以观察返回节点是一个还是多个，如果是多个，则需要遍历才能
    # 依次获取每个节点的属性




2:获取文本
    html = '''
    <div class="wrap">
    <div id="container">
    <ul class="list">
    <li class="item-0">first item</li>
    <li class="item-1"><a href="link2.html">second items</a></li>
    <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
    <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
    </div>
    </div>
    '''
    from pyquery import PyQuery as pq
    doc = pq(html)
    a = doc('.item-0.active a')
    print(a, a.text())
    # 首先选中一个 a 节点，然后调用 text() 方法，就可以获取内部的文本信息，此时它会忽略
    # 内部包含的所有 HTML，只返回纯文本信息。

    doc = pq(html)
    lis = doc('li')
    for li in lis.items():
        print(li.text(), type(li.text()))
        print(li.html(), type(li.html()))
    # lis.html() lis,text() 只分别返回第一个 li 节点内部的 HTML 文本和纯文本。
