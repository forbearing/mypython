#!/usr/bin/env python3

import pandas as pd
import numpy as np

date = np.arange(20170101, 20170105)
df1 = pd.DataFrame(np.arange(12).reshape((4,3)), index=date, columns=['A','B','C'])
df2 = pd.DataFrame(df1, index=date, columns=['A','B','C','D','E'])
# print(df1)
# print(df2)

s1 = pd.Series([3,4,6], index=date[:3])
s2 = pd.Series([32,5,2], index=date[1:])
# print(s1)
# print(s2)

# print(df2)
df2['D'] = s1
df2['E'] = s2
# print(df2)

# axis=0 代表行，1代表列
# how=['any','all'], any：任意一个或多个， all：全部
df3 = df2.dropna(axis=0, how='any')
df4 = df2.dropna(axis=0, how='all')
df5 = df2.fillna(value=0)               # 把控制赋值为0
df6 = df2.isnull()

print(np.any(df2.isnull()))             # 只要存在一个空值就返回 True
print(np.all(df2.isnull()))             # 所有空值才返回 true
