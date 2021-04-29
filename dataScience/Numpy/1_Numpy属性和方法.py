1:概述
    - Numpy（Numerical Python）是 Python 语言的一个扩展库，支持大量的维度数组和矩阵运算，
      此外也针对数组运算提供大量的数学函数库
    - Numpy 是一个运行速度非常快的数学库，主要用于数组计算
        - 一个强大的 N 维数组对象 ndarray
        - 广播功能函数
        - 整合 C/C++/Fortran 代码的工具
        - 线性代数、傅立叶变换、随机数生成等功能
2:Numpy 应用
    - Numpy 通常与 SciPy（Scientific Python）和 Matplotlib（绘图库）一起使用，这种组合
      广泛用于替代 MatLib，是一个强大的科学计算环境
    - SciPy 是一个开源的 Python 算法库和数学工具包
    - SciPy 包含的模块哟有最优化、线性代数、积分、插值、特殊函数、快速傅立叶变换、
      信号处理和图像处理、常微积分求解和其他科学与工程中常用的计算




1:Numpy 属性

    import numpy as np
    array = np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]
                    ])
    print(array, type(array))
    print(array.ndim)        # 维度
    print(array.shape)       # 形状
    print(array.size)        # 大小
    print(array.dtype)       # 元素类型


3:Numpy 常用方法

    # 自定义元素属性
    a = np.array([1,2,3], dtype=np.int32)
    b = np.array([1,2,3], dtype=np.float)
    print(b.dtype)

    # 一维
    a = np.array([1,2,3])
    # 二维
    b = np.array([[1,2,3],
                  [4,5,6]])
    # 三维
    c = np.array([[[1,2,3],
                  [4,5,6]]])

    # 全部为 0 的矩阵
    zero = np.zeros((2,3))
    # 全部为 1 的矩阵
    one = np.ones((3,4))
    # 生成3行2列全部接近于0（不等于0）的矩阵
    empty = np.empty((3,2))
    # arange
    e = np.arange(10)
    e = np.arange(4,12)
    e = np.arange(1,20,3)
    # reshape, 重新定义矩阵的形状
    h = np.arange(8).reshape(2,4)
    h = np.arange(8).reshape(4,2)
