1:字符串初始化
    html = '''
    <div>
    <ul>
    <li class="item-0">first item</li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
    <li class="item-1 active"><a href="link4.html">fourth item</a></li>
    <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
    '''
    from pyquery import PyQuery as pq
    doc = pq(html)
    print(doc('li'))
    # 声明一个变量,并将其当做参数传递给 PyQuery 类,这样就完成了初始化,
    # 将初始化的对象传入 CSS 选择器, 比如在这个实例中,传入 li 节点,这样就可以选择所有的 li 节点




2:URL 初始化
    from pyquery import PyQuery as pq
    doc = pq(url="https://cuiqingcai.com")
    print(doc('title'))
    # 这其实相当于用网页的源代码以字符串的形式传递给 PyQuery 类来进行初始化




3:文件初始化
    from pyquery import PyQuery as pq
    doc = pq(filename='demo.html')
    print(doc('li'))
    # 首先读取本地的文件内容,然后用文件内容以字符串的形式传递给 PyQuery 类来初始化
    # 三种初始化方式中,最常用的方式是以字符串形式传递
