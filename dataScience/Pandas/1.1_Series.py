#!/usr/bin/env python3

import numpy as np
import pandas as pd
obj = pd.Series([4,7,-5,-3])
print(obj)
print(obj.values)
print(obj.index)
print(obj[0])
print(obj['a'])     # 等同于 obj[0]
print(obj[['a', 'c', 'd']])
obj[0] = 10
obj['a'] = 20


=== 数组运算
1:根据布尔数组进行过滤、标量乘法、应用数学函数等，都会保留索引和值之间的链接
obj = pd.Series([6,7,-5,3], index=['d','b','a','c'])
obj[obj>0]
obj*2
np.exp(obj)

2:可以看作一个定长的有序字典，因为它是索引值到数据值的一个映射
'b' in obj
'e' in objk


===
1:如果数据被存放在一个 Python 字典，也可以直接通过这个字典来创建 Series
sdata = {'Ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
obj = Series(sdata)
stats = ['California', 'Ohio', 'Oregon', 'Texas']
obj1 = Series(sdata, index=stats)

2:pandas 的 isnull 和 notnull 函数可以用于检测缺失数据
pd.isnull(obj)
pd.notnull(obj)
obj.isnull()
obj.notnull()

3:对许多应用而言，Series 最重要的一个功能是：它在算术运算中会自动补齐不同索引的数据
obj + obj1

4:Series 对象本身及其索引都有一个 name 属性，该属性跟 pandas 其他的关键功能关系非常密切
obj.name = 'population'
obj.index.name = 'state'
