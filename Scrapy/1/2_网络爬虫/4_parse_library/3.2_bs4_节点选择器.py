1:选择元素
    1:经过选择器后输出的类型是 bs4.element.Tag 类型,这是 BeautifulSoup 中一个重要的数据结构
    2:Tag 具有一些属性,比如 string 属性
    3:soup.p, 当有多个节点时,这种选择方法只会选择到第一个匹配的节点,其后的所有的节点都会被忽略
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
    print(type(soup.title))
    print(soup.title)
    print(soup.title.string)
    print(soup.head)
    print(soup.head.string)
    print(soup.p)
    print(soup.p.string)




2:提取信息
    1:获取名称
        print(soup.title.name)
    2:获取属性
        print(soup.p.attrs)
        print(soup.p.attrs['name'])
        print(soup.p['name'])
        print(soup.p['class'])
        # 每个节点可能由多个属性, 比如 id 或 class 等, attrs 可以获取所有属性
    3:获取内容
        print(soup.p.string)
        # 此处获取的是第一个 p 节点的文本




3:嵌套选择
    1:获取了 head 节点元素,我们可以继续调用 head 来选其内部的 head 节点元素
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    """
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.head.title)




4:关联选择
    ==== 子孙节点 ====
    1:再做选择的时候,有时候不能做到一步就选到想要的节点元素, 需要先选中某一个节点元素,
      然后以他为基准再选择它的子节点,父节点,兄弟节点
    2:contents 属性得到的结果时直接子节点的列表
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.p.contents)

    1:children 属性返回结果是生成器类型
    2:descendants 会递归所有子节点,得到所有的子孙节点
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.p.children)
    for i, child in enumerate(soup.p.childen):
        print(i, child)

    ==== 父节点和祖先节点 ====
    1:获取某个元素的父节点,调用 parents 属性
    2:只是父节点, 而没有再向外寻找父节点的祖先节点
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.a.parents)
    print(list(enumerate(soup.a.parents)))

    ==== 兄弟节点 ====
    1:获取同级的节点(兄弟节点)
    2:next_sibling, previous_sibling 分别获取节点的下一个和上一个兄弟元素
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print('Next Sibling', soup.a.next_sibling)
    print('Prev Sibling', soup.a.previous_sibling)
    print('Next Siblings', list(enumerate(soup.a.next_siblings)))
    print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))

    ==== 提取信息 ====""
    soup = BeautifulSoup(html, 'lxml')
    print('Next Slibing')
    print(type(soup.a.next_sibling))
    print(soup.a.next_sibling)
    print(soup.a.next_sibling.string)
    print('Parent:')
    print(type(soup.a.parents))
    print(list(soup.a.parents)[0])
    print(list(soup.a.parents)[0].attrs['class'])




5:方法选择器
