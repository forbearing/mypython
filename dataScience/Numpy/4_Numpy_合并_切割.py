1:合并
    import numpy as np
    arr1 = np.array([1,2,3])
    arr2 = np.array([4,5,6])
    arr3 = np.vstack((arr1,arr2))       # 垂直合并
    arr4 = np.hstack((arr1,arr2))       # 水平合并
    arrv = np.vstack((arr1,arr2,arr3))
    arrh = np.hstack((arr1,arr2,arr4))

    arr = np.concatenate((arr1,arr2,arr1))
    arr = np.concatenate((arr3, arrv), axis=0)  # 纵向合并，合并的维度要相同，array形状也要匹配
    arr = np.concatenate((arr3, arr3), axis=1)  # 横向合并，合并的维度要相同，array形状也要相同

    arr1.T  # 一维的 array 不能转置
    arr = arr1[np.newaxis,:]
    # print(arr, arr.shape, arr.T)
    arr = arr1[:,np.newaxis]
    arr = np.atleast_2d(arr1)           # 至少二维，如果不是变成二维
    arr = np.atleast_3d(arr1)           # 至少三维，如果不是变成三维
    print(arr)


2:切割
    import numpy as np
    arr1 = np.arange(12).reshape((3,4))
    arr2, arr3 = np.split(arr1, 2, axis=1)              # 水平方向切割，分成 2部分
    arr2, arr3, arr4 = np.split(arr1, 3, axis=0)        # 垂直方向已切割，分成3部分
    #arr2, arr3, arr4 = np.split(arr1, 3, axis=1)       # 报错
    arr2, arr3, arr4 = np.array_split(arr1, 3, axis=1)  # 水平方向切割，不等分切割

    arrv2, arrv3, arrv4 = np.vsplit(arr1, 3)            # 垂直切割
    arrh2, arrh3 = np.hsplit(arr1, 2)            # 水平切割
    print(arr1)
    print(arrh2)
    print(arrh3)
