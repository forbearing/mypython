import numpy as np
1:形状转换: 
    1:reshape(), resize()
        # 函数 resize()的作用跟 reshape()类似，但是会改变所作用的数组，相当于有 inplace=True 的效果
        b.reshape(4,3)
        b.resize(4,3)
    2:ravel() flatten()
        # 1:将多维数组转换成一维数组
        # 2:两者的区别在于返回拷贝(copy)还是返回视图(view). latten() 返回一份拷贝，需要分配新的内存空间，
        #   对拷贝所做的修改不会影响原始矩阵，而 ravel() 返回的是视图(view)，会影响原始矩阵
        b.ravel()
        b.flatten()
    3:tuple 指定数组形状
        b.shape=(2,6)
    4:转置
        b.transpose()
        # 数组转置属性(T)可以转置，也可以通过 transpose() 函数来实现



2:堆叠数组
    1:水平叠加 hstack()
        b = np.arange(4)
        c = b*2
        np.hstack((b,c))
        np.column_stack((b,c))
        # column_stack() 函数以列方式对数组进行叠加，功能类似 hstack()
    2:垂直叠加 vstack()
        np.vstack((b,c))
        np.row_stack()
    3:concatenate() 方法，通过设置 axis 的值来设置叠加方向
        axis=0 沿垂直方向叠加
        axis=1 沿水平方向叠加
        np.concatenate((b,c),axis=1)
        np.concatenate((b,c),axis=0)
    4:深度叠加
        b = np.arange(12).reshape(2,6)
        c = np.arange(12).reshape(2,6)
        arr_dstack = np.dstack((b,c))
        # b,c 均为 shape 位 (2,6) 的二维数组，叠加后，arr_dstack 的 shape 为 (2,6,2)
        # 三位数组



3:数组的拆分
    # 跟数组的叠加类似，数组的拆分可以分为横向拆分、纵向拆分以及深度拆分。涉及的函数为 
    # hsplit()、vsplit()、dsplit() 以及 split()
    1:沿横向拆分 (axis=1)
        b = np.arange(12).reshape(2,6)
        np.hsplit(b,2)
        np.split(b,2, axis=1)
    2:沿纵向拆分 (axis=0)
        np.vsplit(b,2)
        np.split(b,2, axis=0)
    3:深度拆分
        b = np.arange(12).reshape(2,6)
        c = np.arange(12).reshape(2,6)
        arr_dstack = np.dstack((b,c))
        np.dsplit(arr_dstack, 2)
