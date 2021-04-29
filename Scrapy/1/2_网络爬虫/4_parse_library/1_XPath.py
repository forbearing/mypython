1:XPath 概览
    1:XPath, XML Path Language, 即 XML 路径语言, 它是一门在 XML 文档中查找信息的语言.
      它最初是用来搜寻 XML 文档的,但是它同样适用于 HTML 文档的搜索
    2:XPath 的选择功能十分强大,它提供了非常简洁明了的路径选择表达式. 另外,它还提供了超过
      100 个内建函数,用于字符串,数值,时间的匹配以及节点,序列的处理等.几乎所有我们想要定位
      的节点, 都可以用 XPath 来选择
    3:XPath 于 1999年 11月 16日 成为 W3C 标准, 它被设计为供 XSLT, XPointer 以及其他 XML
      解析软件使用.




2:XPath 常见规则
    nodename	                选择此节点的所有子节点
    /				从当前节点选择直接子节点
    //				从当前节点选择子孙节点
    .				选取当前节点
    ..				选取当前节点的父节点
    @				选取属性
    示例: //title[@lang='eng']
    代表选择所有名称为 title, 同时属性 lang 的值为 eng 的节点




3:实例引入
    1:导入 lxml 库的 etree 模块, 然后声明了一段 HTML 文本, 调用 HTML 类进行初始化,这样就
      构造了一个 XPath 解析对象.
    2:需要注意的是 HTML 文本中的最后一个 li 节点是没有闭合的,但是 etree 模块时可以
      自动修正 HTML 文本.
    3:tostring() 方法可以输出修正后的 HTML 代码, 但是结果是 bytes 类型,
      这里利用 decode() 方法将其转换成 str 类型.
    from lxml import etree
    text = '''
    <div>
    <ul>
    <li class="item-0"><a href="link1.html">first item</a></li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-inactive"><a href="link3.html">third item</a></li>
    <li class="item-1"><a href="link4.html">fourth item</a></li>
    <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
    (/div>)
    '''
    html = etree.HTML(text)
    result = etree.tostring(html)
    print(result.decode('utf-8'))

    1:可以直接读取文本文件进行解析
    2:这次的输出结果,多了一个 DOCTYPE 的声明,不过对解析无任何影响
    from lxml import etree
    html = etree.parse('./test.html', etree.HTMLParser())
    result = etree.tostring(html)
    print(result.decode('utf-8'))




4:所有节点
    1:我们一般用 // 开头的 XPath 规则来选取所有符合要求的节点
    2:result = html.xapth('//*') 中的 * 代表所有节点,也就是整个 HTML 文本中的所有节点
      都会被获取, 返回的是一个列表. 每个元素都是 Element 类型, 其后跟了节点的名称, 如
      HTML, body, div, ul, li, a 等,所有节点都包含在列表中
    3:'/tmp/evince-6152/image.PM7TB0.png' '/tmp/evince-6152/image.PM7TB0.png' 
    from lxml import etree
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//*')
    print(result)




5:子节点:
    1:通过 / 或 // 查找元素的子节点或子孙节点.
    2:选择 li 节点的所有直接 a 子节点,可以使用如下方式实现
    3://li 用于选中所有 li 节点, /a 用于选中 li 节点的所有直接子节点 a, 两者结合在一起
      即获取所有 li 节点的所有直接 a 子节点
    from lxml import etree
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//li/a')
    print(result)

    1:/用于获取直接子节点,如果要获取所有子孙节点,就可以使用 //
    2:例如想要获取 ul 节点下的所有子孙 a 节点,可以如下实现
    from lxml import etree
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//ul//a')
    print(result)




6:父节点
    from lxml import etree
    html = etree.parse('./test.html', etree.HTMLParser())
    result= html.xpath('//a[@href="link4.html"]/../@class')
    print(result)
    # 选中 href 属性为 link4.html 的 a 节点,然后再获取父节点,然后再获取其 class 属性
    
    1:我们也可以通过 parent:: 来获取父节点,
    from lxml import etree
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//a[@href="link4.html"/parent::*/@class]')
    print(result)




7:属性匹配
    from lxml import etree
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath(//li[@class='item-0'])
    print(result)




8:文本获取
    1:使用 XPath 中的 text() 方法获取节点中的文本
    2:想要获取 li 节点内部的文本,有两种方式, 一种是先选取 a 节点再获取文本,另一种是使用 //
    3:如果想要获取子孙节点内部的所有文本,可以直接用 // 加 text() 的方式,这样可以保证获取到
      最全面的信息, 但是可能会夹杂一些换行符等特殊字符.
    4:如果想要获取某些特定子孙节点下的所有文本,可以先选取到特定的子孙节点,然后调用 text()
      方法获取其内部的文本,这样就可以保证获取的结果时整洁的
    from lxml import etree
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//li[@class="item-0"]/a/text()')
    print(result)

    from lxml import etree
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//li[@class="item-0"]//text()')
    print(result)




9:属性获取
    1:通过 @href 即可获取节点的 href 属性.此处和属性匹配的方法不同,属性匹配是 中括号加
      属性名和值来限定某个属性, 如 [@href='link1.html'], 而此处的 @href 指的是获取节点
      的某个属性,两者要区分开来
    from lxml import etree
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//li/a/@href')
    print(result)




10:属性多值匹配
    from lxml import etree
    text = '''
    <li class="li li-first"><a href="link.html">first item</a></li>
    '''
    html = etree.HTML(text)
    result = html.xpath('//li[@class="li"]/a/text()')
    print(result)
    # HTML 文本中的 li 节点的 class 属性有两个值 li 和 li-first, 此时如果还想用之前的属性
    # 匹配获取, 就无法匹配了
    
    1:contains() 方法,第一个参数传入属性名称,第二个参数传入属性值,只要比属性包含所传入
      的属性值,就可以完成匹配了
    from lxml import etree
    text = '''
    <li class="li li-first"><a href="link.html">first item</a></li>
    '''
    html = etree.HTML(text)
    result = html.xpath('//li[contains(@class), "li"]/a/text()')
    print(result)




11:多属性匹配
    1:根据多个属性确定一个节点,这时就需要同时匹配多个属性.此时可以使用云算法 and 来连接
    2:and 其实是 XPath 的运算符,另外,还有其他运算符
    from lxml import etree
    text = '''
    <li class="li li-first" name="item"><a href="link.html">first item</a></li>
    '''
    html = etree.HTML(text)
    result = html.xpath('//li[contains(@class, "li")] and @name="item"/a/text()')




12:按序选择
    1:有时候我们在选择的时候某些属性可能同时匹配了多个节点,但是只想要其中的某个节点,
      例如第二个节点或者第一个节点
    2:li[1] 表示第一个 li 节点, last() 选取最后一个 li 节点
    3:我们使用了 last(), position() 等函数. 在 XPath, 提供了 100 多个函数,包括存取,数值,
      字符串,逻辑,节点,序列等处理功能.
    from lxml import etree
    text = '''
    <div>
    <ul>
    <li class="item-0"><a href="link1.html">first item</a></li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-inactive"><a href="link3.html">third item</a></li>
    <li class="item-1"><a href="link4.html">fourth item</a></li>
    <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
    (/div>)
    '''
    html = etree.HTML(text)
    result = html.xpath('//li[1]/a/text()')
    result = html.xpath('//li[last()]/a/text()')
    resutl = html.xpath('//li[position()<3]/a/text()')
    result = html.xpath('//li[last()-1]/a/text()')




13:节点轴选择
    1:XPath 提供了很多节点轴选择方法, 包括获取子元素,兄弟元素,父元素,祖先元素等
    2:ancestor::* ancestor 轴, :: 表示是节点的选择器, 使用 * 表示匹配所有节点
    3:ancestor::div   表示匹配 div 的祖先节点
    4:attribute::*  获取节点的所有属性值
    5:child::a[@href="link1.html"]    获取 href 属性为 link1.html 的子节点节点
    6:descendant::span   获取所有包含span节点的子孙节点
    7:following::*      获取当前节点之后的所有节点
    7:following::*[2]    获取当前节点之后的第二个后续节点
    8:following-sibling::*    获取当前节点之后的所有同级节点
    html = etree.HTML(text)
    result = html.xpath('//li[1]/ancestor::*')
    result = html.xpath('//li[1]/ancestor::div')
    result = html.xpath('//li[1]/attribute::*')
    result = html.xpath('//li[1]/child::a[@href="link1.html"]')
    result = html.xpath('//li[1]/descendant::span')
    result = html.xapth('//li[1]/following::*[2]')
    result = html.xpath('//li[1]/following-sibling::*')
