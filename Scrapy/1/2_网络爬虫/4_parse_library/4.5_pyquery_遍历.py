1:遍历
    1:pyquery 的选择结果可能是多个节点，也可能是单个节点，类型都是 PyQuery 类型。
      并没有返回像 Beautiful Soup 那样的列表。
    2:对于单个节点来说，可以直接打印输出，也可以直接转成字符串
    3:如果要把每一个 li 节点进行遍历，需要调用 items() 方法
    4:调用 items() 方法后，会得到一个生成器，遍历一下，就可以逐个得到 li 节点对象了
      它的类型也是 PyQuery 类型。
    from pyquery import PyQuery as pq
    doc = pq(html)
    lis = doc('.item-0.active')
    for li in lis.items():
        print(li, type(li))




2:获取信息
