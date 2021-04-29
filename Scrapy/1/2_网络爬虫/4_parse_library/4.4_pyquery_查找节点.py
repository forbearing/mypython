1:子节点
    from pyquery import PyQuery as pq
    doc = pq(html)
    items = doc('.list')
    print(type(items))
    print(items)
    lis = items.find('li')
    print(type(lis))
    print(lis)
    # 查找子节点,使用 find() 方法,此时传入的参数是 CSS 选择器, 选取其内部的 li 节点

    lis = items.children()
    print(type(lis))
    print(lis)
    # find() 的查找范围是节点的所有子孙节点, 如果只想查找子节点,使用 children 方法

    lis = items.children('.active')
    print(lis)
    # 筛选所有子节点中符合条件的节点,比如筛选出子节点中 class 为 active 的节点.




2:父节点
    1:使用 parent() 方法来获取某个节点的父节点
    from pyquery import PyQuery as pq
    doc = pq(html)
    items = doc('.list')
    container = items.parent()
    print(type(container))
    print(container)




3:兄弟节点
    from pyquery import PyQuery as pq
    doc = pq(html)
    li = doc('.list .item-0.active')
    print(li.siblings())
    # 首先选择 class 为 list 的节点内部 class 为 item-0 和 active 的节点，也就是第三个 li 节点

    from pyquery import PyQuery as pq
    doc = pq(html)
    li = doc('.list .item-0.active')
    print(li.siblings('.active'))
    # 如果要筛选某个兄弟节点，依然可以向 siblings 方法传入 CSS 选择器，这样就可以从
    # 所有兄弟节点中挑选出符合条件的节点了。

