print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))



1:嵌套选择
    html = '''
    <div class="panel">
    <div class="panel-heading">
    <h4>Hello</h4>
    </div class="panel-body">
    <ul class="list" id="list-1">
    <li class="element">Foo</li>
    <li class="element">Bar</li>
    <li class="element">Jay</li>
    </ul>
    <ul class="list list-smal" id="list-2">
    <li class="element">Foo</li>
    <li class="element">Bar</li>
    </ul>
    <div>
    </div>
    </div>
    '''
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    for ul in soup.select('ul'):
        print(ul.select('li'))
    # 输出所有 ul 节点下所有 li 节点组成的列表



2:获取属性
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    for ul in soup.select('ul'):
        print(ul['id'])
        print(ul.attrs['id'])
    # 直接传入中括号和属性名,以及通过 attrs 属性获得属性值,都可以成功



3:获取文本
    1:要想获得文本,可以使用前面讲的 string 属性,也可以 get_text() 方法
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    for li in soup.select('li'):
        print(li.get_text())
        print(li.string)
