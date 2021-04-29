1:常用函数
    # 函数在使用时需要指定 axis 轴的方向，若不指定，默认统计整个数组。
    np.sum()，返回求和
    np.mean()，返回均值
    np.max()，返回最大值
    np.min()，返回最小值
    np.ptp()，数组沿指定轴返回最大值减去最小值，即(max-min) • np.std()，返回标准偏差(standarddeviation)
    np.var()，返回方差(variance)
    np.cumsum()，返回累加值
    np.cumprod()，返回累乘积值

2:示例
    b = np.arange(12).reshape(2,6)
    np.max(b)
    np.max(b, axis=1)
    np.max(b, axis=0)
    np.ptp(b)
    np.ptp(b, axis=1)
    np.ptp(b, axis=0)
    b.resize(4,3)

3:数组的广播
    1:当数组跟一个标量进行数学运算时，标量需要根据数组的形状进行扩展，然后执行运算。
      这个扩展的过程称为“广播(broadcasting)”
    b = np.arange(12).reshape(4,3)
    d = b + 2
