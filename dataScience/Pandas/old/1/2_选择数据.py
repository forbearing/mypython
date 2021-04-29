import pandas as pd
import numpy as np

date = pd.date_range('20170101', periods=6)
df1 = pd.DataFrame(np.arange(24).reshape((6,4)), index=date, columns=['A','B','C','D'])

# 选取单维度的数据
print(df1['A'])
print(df1.A)
print(df1[0:2])             #选取前两行 
print(df1['20170102':'20170103'])

# 通过标签选择数据
df1.loc['20170102']
df1.loc['20170101',['A','C']]
df1.loc[:, ['A','B']]

# 通过位置选择数据
df1.iloc[2]
df1.iloc[1:3, 2:4]
df1.iloc[[1,2,4], [1,3]]

# 通过混合标签位置选择
df1.ix[2:4, ['A','C']]
df1.ix['20170102':'20170104', 2:4]

# 判断
df1.A > 6
