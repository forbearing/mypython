python 内置了 map() 和 reduce()

map(fn, lsd)
    参数1 是函数
    参数2 是序列
    功能: 将传入的函数依次作用在序列中的每一个元素,并把结果作为新的 Iterator 返回
    map(float, ['1','2','3','4'])


reduce(fn, lsd)
    参数1 是函数
    参数2 为列表
    功能: 一个函数作用在序列上,这个函数必须接受两个参数. reduce 把结果继续和序列的
        下一个元素累计运算.

    ---
    from functools import reduce
    def myAdd(a, b):
        return a+b
    redu = reduce(myAdd, range(1,10))
    print(redu)


filter(fn, lsd)
    参数1 为函数
    参数2 为序列
    功能: 用于过滤序列,把传入的函数依次作用于序列的每个元素,根据返回的元素是 True 或
        False 来决定是否保留该元素.

    ---
    # 过滤掉偶数,留下奇数
    def func(x):
        if x % 2:
            return True
        else:
            False
    fil = filter(func, range(1,10))
    for i  in fil:
        print(i, end=" ")


sorted
    ---
    # 普通排序
    list1 = [4,7,2,5,6]
    list2 = sorted(list1)           # 默认使用升序排序
    print(list1)
    print(list2)

    ---
    # 按绝对值大小排序
    list1 = [4,-7,9.-2, 2]
    list2 = sorted(list1, key=abs)  # key 接受函数来实现自定义排序规则
    print(list1)
    print(list2)

    ---
    # 降序排序
    list1 = [4,-7,9.-2, 2]
    list2 = sorted(list1, reverse)

    ---
    # 按照字符串的长短来排序
    list2 = sorted(list1, key=len)
