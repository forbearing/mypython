===
1:表格型数据结构
2:DataFrame 既有行索引也有列索引，可以被看作由 Series 组成的字典（共用同一个索引）
3:跟其他类似的数据结构相比（如R的data.frame），DataFrame 中面向行和面向列的
  操作基本是平衡的。


===
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data)

1:如果指定了序列，则 DataFrame 的列就会按照指定顺序进行排序
    frame = pd.DataFrame(data, columns=['year', 'state', 'pop'])
2:如果传入的列在数据中找不到，就会产生 NA 值：
    frame = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                                index=['one', 'two', 'three', 'four', 'five'])
3:如果类似字典标记的方式或属性的方式，可以将 DataFrame 的列获得一个 Series
  返回的 Series 拥有原 DataFrame 相同的索引。且其 name 属性已经设置好了
    print(frame.year)
    print(frame['year'])
    frame['debet'] = 16.5
    frame['debet'] = np.arange(5.0)
4:将列表或数组赋值给某个列时，其长度必须跟 DataFrame 的长度相匹配。如果赋值的是一个 
  Series，就会精确匹配 DataFrame 的索引，所有的空位都将会被填上缺失值
    val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
    frame['debt'] = val
5:为不存在的列赋值会创建出一个新列。关键字 del 用于删除列
    frame['eastern'] = frame.state == 'Ohio'
    del frame['eastern']
6:对索引方式返回的列只是相应数据的视图而已，并不是副本。因此，对返回的 Series 所做的
  任何就地修改全都会反映到源 DataFrame 上。通过 Series 的 copy 方法即可显式复制。
7:一个常见的数据结构是嵌套字典（字典中包含字典）。如果给它传递给 DataFrame，它就会被
  解释为：外层字典的键作为列，内层键则作为行索引，
  也可以对结果进行转置
    data2 = {'Nevada':{2001:2.4, 2002:2.9}, 'ohio':{2000:1.5, 2001:1.7, 2002:3.6}}
    frame2 = pd.DataFrame(data2)
    frame2.T
8:内层字典会被合并、排列以形成最终的索引，如果显式指定了索引，则不会这样
    fram3 = DataFrame(data2, index=[2001, 2002, 2003])
    print(frame3.values)            # 返回二维 ndarray
    print(frame3.index)
9:由 Series 组成的字典差不多也是一样的用法



=== 
DataFrame 构造函数所能接受的各种数据
    二维 ndarray
        数据矩阵，还可以传入行标和列标
    由数组、列表或元祖组成的字典
        每个序列会变成 DataFrame 的一列。所有序列的长度必须相同
    Numpy 的结构化/记录数组
        类似于“由数组组成的字典”
    由 Series 组成的字典
        每个 Series 会成为一列。如果没有显式指定索引，则各 Series 的索引会被合并成结果的行索引
    由字典组成的字典
        各内层字典会成为一列。键会被合并成结果的行索引，跟“由Series组成的字典”的情况一样
    字典或Series的列表
        各项会成为 DataFrame 的一样。字典键或 Series 索引的并集将会成为 DataFrame 的列标
    由列表或元祖组成的列表
        类似于 “二维ndarray”
    另一个 DataFrame
        该 DataFrame 的索引将会被沿用，除非显式指定了其他索引
    Numpy 的 MaskedArray
        类似于 “二维ndaray”的情况，只是掩码值在结果 DataFrame 会变成 NA/缺失值



===
1:Index 对象是不可修改的，不可修改性非常重要，因为这样才能使 Index 对象在多个数据
  结构之间安全共享。
    obj = Series(range(3), index=['a','b','c'])
    index = obj.index
    print(index[1:])
    index[0] = 10               # index 对象不可修改

    index = pd.Index(np.arange(3))
    obj2 = pd.Series([1.5, -2.5, 6], index=index)
    print(obj2.index is index)


===
1:pandas 库中内置的 Index 类，可以被继承从而实现特别的轴索引功能
  虽然大部分用户都不需要知道太多 Index 对象的细节，但它们确实是 pandas
  数据模型的重要组成部分
2:pandas 中主要的 Index 对象
    index
        最泛华的 Index 对象，将轴标签表示为一个由 Python 对象组成的 Numpy 数组
    int64Index
        针对整数的特殊 Index
    MultiIndex
        “层次化” 索引对象，表示单个轴上的多层索引。可以看做由元祖组成的数组
    DatatimeIndex
        存储纳秒级时间戳（用 Numpy 的 datatime64 类型表示）
    PeriodIndex
        针对 Period 数据（时间间隔）的特殊 Index
3:除了长的像数组，Index 的功能也类似于一个固定大小的集合
    print('one' in frame.index)
    [rint('state' in frame.columns)]
4:Index 的方法和属性
    append          连接一个Index对象，产生一个新的Index
    difference      计算一个差集，并得到一个新的 Index
    intersection    计算交集
    union           计算并集
    isin            计算一个指示各值是否都包含在参数集合中的布尔型数组
    delete          删除索引i处的元素，并得到新的 Index
    drop            删除传入的值，并得到新的 Index
    insert          将元素插入到索引i处，并得到新的 index
    is_monotonic    当各个元素均大于前一个元素时，返回 True
    is_unique       当 Index 没有重复值时，返回 True
    unique          计算 Index 中唯一值的数组
