
前面的选择方法是通过属性来选择的,这种方法非常快,但是如果进行比较复杂的选择,就比较麻烦
不够灵活, BeautifulSoup 为我们提供了一些查询方法




1:find_all() ====
    find_all(name, attrs, recursive, text, **kwargs)
    功能: 查询所有符合条件的元素, 给它传入一些属性或文本,就可以得到符合条件的元素

    1:name: 根据节点名来查询元素
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find_all(name='ul'))
    print(type(soup.find_all(name='ul'))[0])

    for ul in soup.find_all(name='ul'):
        print(ul.find_all(name='li'))
        for li in ul.find_all(name='li'):
            print(li.string)
    
    2:attrs
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find_all(attrs={'id':'list-1'}))
    print(soup.find_all(attrs={'name': 'elements'}))
    
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find_all(id='list-1'))
    print(soup.find_all(class='element'))
    # 对于一些常用的属性,比如 id 和 class ,可以不用 attrs 来传递

    3:text: 匹配节点的文本,传入的形式可以是字符串,也可以是正则表达式对象
    import re
    from bs4 import BeautifulSoup(html, 'lxml')
    soup = BeautifulSoup(html, 'lxml')
    res = soup.find_all(text=re.compile('link'))
    print(res)




2:find
    1:返回单个匹配的元素,
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find(name='ul'))
    print(type(soup.find(name='ul')))
    print(soup.find(class_'list'))



3:
    find_parents()              返回所有祖先节点
    find_parent()               返回直接祖先节点
    find_next_siblings()        返回后面所有兄弟节点
    find_next_sibling()         返回后面第一个兄弟节点
    find_previous_siblings()    返回前面所有的兄弟节点
    find_previous_sibling()     返回前面第一个兄弟节点
    find_all_next()             返回节点后所有符合条件的节点
    find_next()                 返回第一个符合条件的节点
    find_all_previous()         返回节点前所有符合的节点,
    find_previous()             返回节点前第一个符合条件的节点
