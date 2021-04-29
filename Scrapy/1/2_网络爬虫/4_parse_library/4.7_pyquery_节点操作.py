pyquery 提供了一系列方法来对接点进行动态修改，比如为某个节点添加一个 class，移除某个
节点等，这些操作有时候会为提取信息来带极大的便利




1:addClass, removeClass
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
    li = doc('.item-0.active')
    print(li)
    li.removeClass('active')
    li.addClass('active')
    print(li)




2:attr, text, html
    1:除了操作 class 这个属性，也可以用 attr() 方法对属性进行操作。还可以用
      text() 和 html() 来改变节点内部的内容
    2:attr() 来修改属性，第一个参数为属性名，第二个参数为属性值。
    3:attr() 方法只传入第一个参数的属性名，则是获取这个属性值，如果传入第二个参数则是修改
      属性值。text() 和 html() 方法如果不传参，则是获取节点内纯文本和 HTML 文本。
      如果传入参数，则进行赋值。
    html = '''
    <ul class="list">
    <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
    </ul>
    '''
    from pyquery import PyQuery as pq
    doc = pq(html)
    li = doc('.item-0.active')
    print(li)
    li.attr('name', 'link')
    print(li)
    li.text('changed item')
    print(li)
    li.html('<span>changed item</span>')
    print(li)




3:remove()
    1:移除属性，它有时会为信息带来非常大的便利
    2:其他节点操作方法：append(), empty(), prepend()。它们和 jQuery 的用法完全一致
    html = '''
    <div class="wrap">
        Hello, World
    <p>This is a paragraph.</p>
    </div>
    '''
    from pyquery import PyQuery as pq
    doc=  pq(html)
    wrap = doc('.wrap')
    print(wrap.text())
    wrap.find('p').remove()
    print()
