=== 索引
df = pd.DataFrame([
            ['green', 'M', 10.1, 'class1'],
            ['red', 'L', 13.5, 'class2'],
            ['blue', 'XL', 15.3, 'class1']])
1:loc 通过标签索引，前闭合+后闭合
    print(df.loc[0])
    print(df.loc[0:1])          # 行索引
    print(df.loc[:0:1])         # 列索引
    print(df.loc[1,2])          # 值索引
2:iloc 通过行号/序号索引，只有前闭合
    df.columns=['a', 'b', 'c', 'd'] 

3:loc, iloc
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


=== 重新索引
1:Series 的 reindex 将会根据新索引进行排序，如果某个索引值当前不存在，就引入缺失值
    obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
    obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
    obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)

2:对于时间序列这样的有序数据，重新索引可能需要做一些插值处理。method 选项可以达到此目的
  ffill 可以实现向前值填充
3:reindex 的（插值）method 选项
    "fill"/"pad"            前向填充（或搬运）值
    "bill"/"backfill"       后向填充（或搬运）值
    obj3 = Series(['blue', 'purple', 'yellow'], index=[0,2,4])
    obj4 = obj3.reindex(range(6), method='ffill')

4:对于 DataFrame reindex 可以修改（行）索引、列，或两个都可以修改。如果仅传入一个序列，
  则会重新索引行
    frame = pd.DataFrame(np.arange(9).reshape((3,3)), 
            index=['a','c', 'd'], columns=['Ohio', 'Texas', 'California'])
    frame2 = frame.reindex(['a', 'b', 'c', 'd'])
    states=['Texas', 'Utah', 'California']
    frame3 = frame.reindex(columns=states)
5:也可以同时对行和列进行重新索引，而插值只能按行应用（即轴0）
    frame4 = frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill', columns=states)

6:reindex 函数的参数
    index       用于索引的新序列，既可以是 Index 实例，也可以是其他序列型的 Python 
                数据结构。Index 会被完全使用，就像没有任何复制一样
    method      插值（填充）方式
    fill_value  在重新索引的过程中，需要引入缺失时使用的替代值
    limit       前向或后向填充时的最大填充量
    level       在 MultiIndex 的指定级别上匹配简单索引，否则选取其子集
    copy        默认为 True，无论如何都复制，如果为 False，则新旧想等就不复制


=== 丢弃指定轴上的项
1:Series drop
    obj = pd.Series(np.arange(5), index=['a','b','c','d','e'])
    new_obj = obj.drop('c')
    new_obj = obj.drop(['d', 'c'])
2:DataFrame drop
    data = DataFrame(np.arange(16).reshape((4,4)), 
            index=['Ohio', 'Colorado', 'Utah', 'New York'],
            columns=['one', 'two', 'three', 'four'])
    data.drop('Ohio')
    data.drop(['Ohio', 'New York'])
    data.drop('two', axis=1)
    data.drop(['two', 'four'], axis=1)


=== 索引，选取和过滤
1:Series 索引的工作方式类似于 Numpy 数组的索引，只不过 Series 的索引不只是整数
2:利用标签切片运算与普通的切片运算不同，其末端是包含的
    obj = pd.Series(np.arange(4.), index=['a','b','c','d'])
    obj[obj<2]
    obj['b']
    obj['a':'c']
    obj[['a', 'b']]
    obj[1]
    obj[2:4]
    obj[[2,4]]
    obj['b':'c'] = 5

    data = DataFrame(np.arange(16).reshape((4,4)),
            index=['Ohio', 'Colorado', 'Utah', 'New York'],
            columns=['one', 'two', 'three', 'four'])
    data['two']
    data[['one', 'three']]
    data[:2]
    data[data['three'] > 5]
    data < 5
    data[data < 5] = 0



=== 算术运算和数据对齐
1:Pandas 的一个重要功能是，它可以对不同索引的对象进行算术运算。在对对象相加时，如果存在
  不同的索引对，则结果的索引就是该索引对的并集
2:自动的数据对齐操作不重叠的索引引入了NaN值，缺失值会在算术运算过程中传播
    s1 = pd.Series([7.3,-2.5,3.4,1.5], index=['a','c','d','e'])
    s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a','c','e','f','g'])
    print(s1+s2)

    df1 = pd.DataFrame(np.arange(9).reshape((3,3)),
            columns=list('bcd'), index=['Ohio','Texas','Colorado'])
    df2 = pd.DataFrame(np.arange(12.).reshape((4,3)),
            columns=list('bde'), index=['Utah','Ohio','Texas','Oregon'])
3:在算术方法中填充值
    df1.add(df2, fill_value=0)
    df1.reindex(columns=df2.columns, fill_value=0)
4:算术方法
    add、sub、div、mul

5:DataFrame 和 Series 之间的运算，会将 Series 的索引匹配到 DataFrame 的列，然后沿着
  行一直向下广播
    frame = pd.DataFrame(np.arange(12.).reshape((4,3)), 
            columns=list('bde'), index=['Utah','Ohio','Texas','Oregon'])
    obj = frame.iloc[0]
    print(frame - obj)
6:如果某个索引值在 DataFrame 的列或 Series 的索引中找不到，则参与运算的两个对象就会
  被重新索引以形成并集
    obj2 = pd.Series(range(3), index=['b', 'e', 'f'])
    print(frame - obj2)
7:如果你希望匹配行且在列上进行广播，则必须使用算术运算方法
  传入的轴号，就是希望匹配的轴
    obj3 = frame['d']
    frame.sub(obj3, axis=0)



=== 函数应用和映射
1:numpy 元素级的数组方法，可用于操作 pandas 对象
    frame = pd.DataFrame(np.random.randn(4,3), columns=list('bde'),
            index=['Utah','Ohio','Texas','Oregon'])
    np.abs(frame)
2:另一种常见操作是，将函数应用到各列或行所形成的一维数组上。DataFrame 的 apply 方法可以实现此功能
    f = lambda x: x.max()-x.min()
    frame.apply(f)
    frame.apply(f, axis=1)
    def f(x):
        return pd.Series([x.min(), x.max()], index=['min', max])
    frame.apply(f)
    format = lambda x: '%.2f' %x
    frame.applymap(format)


=== 排序和排名
1:对行或列索引进行排序（按字典排序），可使用 sort_index 方法，它将返回一个以排序的新对象
    obj = pd.Series(range(4), index=['d', 'a', 'c', 'd'])
    obj.sort_index()
2:对于 DataFrame，可以根据任意一个轴上的索引进行排序
    frame = pd.DataFrame(np.arange(8).reshape((2,4)),
            index=['three', 'one'], columns=['d','a','b','c'])
    frame.sort_index()
    frame.sort_index(axis=1)
3:默认是升序
    frame.sort_index(axis=1, accending=False)
