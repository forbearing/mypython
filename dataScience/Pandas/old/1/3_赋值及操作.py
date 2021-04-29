import pandas as pd
import numpy as np

date = np.arange(20170101, 20170107)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=date, columns=['A','B','C','D'])
print(df)

# 赋值
df.iloc[2,2] = 100
df.loc[20170106,'B'] = 200
df[df.A>10] = 0
df.A[df.A==0] = 1
df['E'] = 10
df['F'] = pd.Series([1,2,3,4,5,6], index=date)
df.loc[20170107, ['A','B','C']] = [1,2,3]

# 插入
s1 = pd.Series([1,2,3,4,5,6], index=['A','B','C','D','E','F'])
s1.name = 'S1'
df2 = df.append(s1)
df.insert(1,'G',df2['E'])           # 在第一列插入索引为G的 df2 中的E列

# 删除
g = df.pop('G')                     # 弹出G列
df.insert(6, 'G', g)                # 在最后插入

del df['G']                         # 删除 G 列
df3 = df.drop(['A','B'], axis=1)    # 删除多个列
df4 = df.drop([20170101,20170102], axis=0)
