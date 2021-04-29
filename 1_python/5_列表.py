1:概念:
    1:序列的每一个元素都分配一个数字(它的位置，索引)，第一个索引为0，第二个索引为1
    2:Python 有6个序列的内置类型，但最常见的是列表和元组
    3:序列可以进行的操作包括：索引、切片、加、乘、检查成员
    4:Python 已经内置确定序列的长度以及确定最大值和最小值的元素的方法
    5:列表是最常用的 Python 数据类型
    6:列表中的元素类型可以不同，
    7:创建一个列表，只要把逗号分割的不同的数据项用 "[]"  扩起来就行



1:列表包含以下函数
    len(list)               列表个数
    max(list)               返回列表最大值
    min(list)               返回列表元素最小值
    list(seq)               将元组转换为列表

2:列表包含以下方法
    list.count(ojb)
        统计某个元素在列表中出现的次数
    list.index(obj)
        从列表中找出某个值第一个匹配项的索引位置
    list.append(obj)
        在列表末尾添加新的对象
    list.insert(index, obj)
        将对象插入列表
    list.extend(seq)
        在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    list.pop(index=-1)
        移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    list.remove(obj)
        移除列表中某个值的第一个匹配项
    list.reverse()                          反向列表中元素
    list.sort( key=None, reverse=False)     对原列表进行排序
    list.clear()                            清空列表
    list.copy()                             复制列表
