1:Series
    import pandas as pd
    import numpy as np

    s1 = pd.Series([4,7,-5,3])          # 创建一个 Series，索引为默认值
    # print(s1)
    # print(s1.values)
    # print(s1.index)

    s2 = pd.Series([4,7,-5,3], index=['a','b','c','d'], dtype=float)
    # print(s2)
    # print(s2.values)
    # print(s2.index)

    # 根据索引取值
    print(s2['a'])
    print(s2[['a','b','d']])

    # Series 可以堪称一个定长的有序字典
    dict1 = {"apple":5, "pen":3, "applepen":10}
    s = pd.Series(dict1)
    print(s)


2:DataFrame
    data = {'year':[2012,2013,2014,2015],
           'income':[10000,20000,30000,40000],
           'pay': [4000,7000,1000,2000]}
    df1 = pd.DataFrame(data)
    df2 = pd.DataFrame(np.arange(12).reshape((3,4)))
    df3 = pd.DataFrame(np.arange(12).reshape((3,4)), index=['a','c','b'], columns=['E','D','C','B'])

    # DataFrame 属性
    # print(df3.columns)          # 列属性
    # print(df3.index)            # 行属性
    # print(df3.values)           # 值
    # print(df3.describe())
    # print(df.T)

    # 排序
    df3.sort_index(axis=1)          # 列排序
    df3.sort_index(axis=0)          # 行排序
    df3.sort_values(by="C")         # 按值排序
