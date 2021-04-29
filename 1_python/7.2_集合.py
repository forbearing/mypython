1:概念
    1:集合（set）是一个无序的不重复元素序列
    2:创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
        s1 = {value1, value2, value3}
    3:集合没有索引

2:集合运算
    a = set('abracadabra')
    b = set('alacazam')
    a-b                 # 集合a中包含而集合b中不包含的元素
    a | b               # 集合a或b中包含的所有元素
    a & b               # 集合a和b中都包含了的元素
    a ^ b               # 不同时包含于a和b的元素

3:集合的基本操作
    1:添加元素
        s.add(x)            # 添加，将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
        s.add('abc')        # 插入字符串，错误
        s.add((1,2,3))      # 插入元组，正确
        s.add([1,2,3])      # 插入列表，错误
        s.update( x )       # 添加，也可以添加元素，且参数可以是列表，元组，字典等
        s.update('abc')     # 插入字符串，争取
        s.update((1,2,3))   # 插入元组，正确
        s.update([1,2,3])   # 插入列表，正确
        s.update([1,4], [5,6])  # x 可以是多个，用逗号隔开
    2:移除元素
        s.remove()          # 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
        s.discard()         # 移除集合中的元素，且如果元素不存在，不会发生错误
        s.discard("Facebook")
        s.pop()             # 随机删除集合中的一个元素。set 集合的 pop 方法会对集合进行
                            # 无序的排列，然后将这个无序排列集合的左面第一个元素进行删除
    3:计算元素个数
        len(s)
    4:清空集合
        s.clear()
    5:判断元素是否在集合中存在
        x in s

4:集合方法
    s.add()                 # 为集合添加元素
    s.clear()               # 移除集合中的所有元素
    s.copy()                # 拷贝一个集合
    s.difference(a)         # 返回多个集合的差集
    s.difference_update(a)  # 移除在集合a中也存在的元素
    s.discard()             # 删除集合中指定的元素
    s.intersection()        # 返回集合的交集
    s.intersection_update() # 返回集合的交集，并更新到集合s中
    s.isdisjoint(s2)        # 判断两个集合是否包含相同的元组，没有返回True，否则False
    s.issubset(d)           # 判断集合 s 是否是 集合 b 的子集，是返回 True
    s.issuperset(d)         # 判断集合 d 是否是 s 的子集
    s.pop()                 # 随机移除元素
    s.remove()              # 移除指定元素
    s.symmetric_difference()            # 返回两个集合中不重复的元素集合。
    s.symmetric_difference_update()     # 移除当前集合中在另外一个指定集合相同的元素
                                        # 并将另外一个指定集合中不同的元素插入到当前集合中
    s.union()               # 返回两个集合的并集
    s.update()              # 给集合添加元素
