1:数据合并 concat
    import numpy as np
    import pandas as pd

    df1 = pd.DataFrame(np.arange(12).reshape((3,4)), columns=['a','b','c','d'])
    df2 = pd.DataFrame(np.arange(12,24).reshape((3,4)), columns=['a','b','c','d'])
    df3 = pd.DataFrame(np.arange(24,36).reshape((3,4)), columns=['a','b','c','d'])
    # print(df1)
    # print(df2)
    # print(df3)
    df4 = pd.concat([df1, df2, df3], axis=0)        # 纵向合并
    df4 = pd.concat([df1, df2, df3], axis=0, ignore_index=True) # 纵向合并，不考虑原来的 Index
    df5 = pd.concat([df1, df2, df3], axis=1)        # 水平合并


    df1 = pd.DataFrame(np.arange(12).reshape((3,4)), columns=['a','b','c','f'])
    df2 = pd.DataFrame(np.arange(12).reshape((3,4)), columns=['a','c','d','e'])
    # print(df1)
    # print(df2)
    df3 = pd.concat([df1, df2], join='outer', ignore_index=True)    # 合并两个表，缺少的部分填充 NaN
    df4 = pd.concat([df1, df2], join='inner', ignore_index=True)    # 合并两个表，缺少的部分去掉


    df1 = pd.DataFrame(np.arange(12).reshape((3,4)), columns=['a','b','c','f'])
    df2 = pd.DataFrame(np.arange(12).reshape((4,3)), columns=['a','c','d'])
    print(df1)
    print(df2)
    df3 = pd.concat([df1, df2], axis=1, join_axes[df1.index])       # 横向合并，index 使用 df1 的 index



2:数据合并 merge
    import numpy as np
    import pandas as pd

    left = pd.DataFrame({'Key': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    right = pd.DataFrame({'Key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})
    # print(left)
    # print(right)
    df = pd.merge(left, right, on='Key')
    # print(df)



    left = pd.DataFrame({'Key1': ['K0', 'K0', 'K1', 'K2'],
                         'Key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    right = pd.DataFrame({'Key1': ['K0', 'K1', 'K1', 'K3'],
                          'Key2': ['K0', 'K0', 'K0', 'K0'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})
    # print(left)
    # print(right)
    # how 的取值 left, right, inner, outeer
    df1 = pd.merge(left, right, on=['Key1','Key2'], how='inner')    # how 默认为 inner
    df2 = pd.merge(left, right, on=['Key1','Key2'], how='outer')
    df3 = pd.merge(left, right, on=['Key1','Key2'], how='left')
    df4 = pd.merge(left, right, on=['Key1','Key2'], how='right')
    df4 = pd.merge(left, right, on=['Key1','Key2'], how='right', indicator=True)    # 显示 merge 信息
    df4 = pd.merge(left, right, on=['Key1','Key2'], how='right', indicator='indicator_column')
    # print(df1)
    # print(df2)
    # print(df3)
    # print(df4)



    left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                         'B': ['B0', 'B1', 'B2']},
                        index=["K0", "K1", "K2"])
    right = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                          'D': ['D0', 'D1', 'D2']},
                         index=['K0', 'K1', 'K2'])
    # print(left)
    # print(right)
    df = pd.merge(left, right, left_index=True, right_index=True, how='outer')
    # print(df)



    boys  = pd.DataFrame({'K': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
    girls = pd.DataFrame({'K': ['K0', 'K1', 'K2'], 'age': [4, 5, 6]})
    print(boys)
    print(girls)
    df = pd.merge(boys, girls, on='K', suffixes=['_boy', '_girls'], how='outer')
    print(df)
