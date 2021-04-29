##!/usr/bin/env python3
1:介绍
    1:Xpath，XML Path Language，一门在 XML 中查找信息的语言。Xpath 最初是用来搜寻
      XML 文档的，但是它同样适用于 HTML 文档的搜索
    2:Xpath 的功能十分强大，它提供了非常简明的路径选择方式，另外他提供了超过100个内建
      函数用于字符串、数值、时间的匹配以及节点、序列的处理等。几乎所有我们想要定位的
      节点都可以用 Xpath 来选择。

2:XPath 常用规则
    NodeName        选取此节点的所有子节点
    /               从当前节点选取直接子节点
    //              从当前节点选取子孙节点
    .               选择当前节点
    ..              选择当前节点的父节点
    @               选取属性
    //title[@lang='eng']
        选择所有名称为 title，同时属性 lang 的值为 eng 的节点

    ---
    from lxml import etree
    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
             <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
             <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
             <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
             <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
         </ul>
     </div>
    '''
    html = etree.html(text)         # 生成一个 XPath 解析对象
    res = etree.tostring(html)      # bytes 类型
    print(res.decode("utf8"))

    ---
    from lxml import etree
    html = etree.parse('./test.html', etree.HTMLParse())
    res = etree.tostring(html)
    print(res.decode("utf8"))
    # 这次的输出结果略有不同，多了一个 DOCTYPE 的声明，不过对解析无任何影响



3:所有节点
    1:* 代表所有节点，也就是整个 HTML 文件中的所有节点都会被获取
    2:返回形式是一个列表，每个元素都是 Element 类型，其后跟了节点的名称，如 html、body
      div、ul、li、a 等，所有的节点都包含在列表中。
    3:也可以指定节点名称，例如 //li

    from lxml import etree
    html = etre.parse('./test.html', etree.HTMLParse())
    res = html.xpath('//*')
    res = html.xpath('//li')
    print(res)
    print(res[0])


4:子节点
    1://li/a 表示选中 li 节点的所有直接子节点a。二者结合在一起获取了所有 li 节点的所有
      直接 a 子节点。

    from lxml import etree
    html = etree.parse('./test.html', etre.HTMLParser())
    res = html.xpath('//li/a')
    print(res)

    res = html.xpath('//li//a')
    # 获取 ul 节点下的所有子孙 a 节点

5:父节点
    result = html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/../@class')

6:属性匹配
    result = html.xpath('//li[@class="item-0"]')

7:文本获取
    esult = html.xpath('//li[@class="item-0"]/a/text()')
    result = html.xpath('//li[@class="item-0"]//text()')
    1:如果我们要想获取子孙节点内部的所有文本，可以直接用 // 加 text() 的方式获取，这样
      可以保证获取到最全面的文本信息，但是可能会夹杂一些换行符等特殊字符。如果我们想获取
      某些特定子孙节点下的所有文本，可以先选取到特定的子孙节点，然后再调用 text() 
      方法获取其内部文本，这样可以保证获取的结果是整洁的

8:属性获取
    1:获取所有 li 节点下所有 a 节点的 href 属性
    2:注意此处和属性匹配的方法不同，属性匹配是中括号加属性名和值来限定某个属性，
      而此处的 @href 指的是获取节点的某个属性。二者需要做好区分。
    result = html.xpath('//li/a/@href')


8:属性多值匹配
    1:有时候某些节点的某个属性可能有多个值
    2:如果属性有多个值就需要用 contains() 函数

    from lxml import etree
    text = '''
    <li class="li li-first"><a href="https://ask.hellobi.com/link.html">first item</a></li>
    '''
    # li 节点的 class 属性有两个值 li 和 li-first
    html = etre.HTML(text)
    result = html.xpath('//li[@class="li"]/a/text()')       # 错误，匹配不到
    result = html.xpath('//li[contains(@class, "li")]/a/text()')

9:多属性匹配
    1:匹配多个属性，需要使用 and

    from lxml import etree
    text = '''
    <li class="li li-first" name="item"><a href="https://ask.hellobi.com/link.html">first item</a></li>
    '''
    html = etree.HTML(text)
    result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')


10:按序选择
    1:有时候我们在选择的时候可能某些属性同时匹配了多个节点
    2:可以利用中括号传入索引的方法获取特定次序的节点

    html = etree.HTML(text)
    res = html.xpath('//li[1]/a/text()')            # 第一个 li
    res = html.xpath('//li[last()]/a/text()')       # 最后一个li
    res = html.xpath('//li[position()<3]/a/text()') # 位置小于 3 的 li 节点
    res = html.xpath('//li[last()-2]/a/text()')


11:节点轴选择
    1:XPath 提供了很多节点轴选择方法，英文叫做 XPath Axes，包括获取子元素、兄弟元素、
      父元素、祖先元素等等
    2:ancestor 可以获取所有祖先节点，"::" 表示节点的选择器，"*" 表示匹配所有节点。
      返回给了 html, body, div, ul
    3:ancestor::div 只获取 div 这个祖先节点
    4:attribute 轴，获取所有属性值，"*" 表示获取节点的所有属性
      "li[1]/attribute::*" 返回 li 节点的所有属性值
    5:descendant 轴，获取所有子孙节点
    6:child, 获取所有直接子节点
    7:following, 获取当前节点之后的所有节点
    8:following-sibling, 可以获取当前节点之后的所有同级节点

    from lxml import etree
    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="https://ask.hellobi.com/link1.html"><span>first item</span></a></li>
             <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
             <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
             <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
             <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
         </ul>
     </div>
    '''
    html = etree.HTML(text)
    result = html.xpath('//li[1]/ancestor::*')
    result = html.xpath('//li[1]/ancestor::div')
    result = html.xpath('//li[1]/attribute::*')
    result = html.xpath('//li[1]/child::a[@href="https://ask.hellobi.com/link1.html"]')
    result = html.xpath('//li[1]/descendant::span')
    result = html.xpath('//li[1]/following::*[2]')
    result = html.xpath('//li[1]/following-sibling::*')
