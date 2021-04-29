1:一维
    import numpy as np
    arr1 = np.arange(2,14)
    print(arr1[2])                  # 第二个位置的数据
    print(arr1[1:4])                # 第1到第4位置的数据
    print(arr1[2:-1])               # 第二道倒数第一个位置的数据，不包括倒数第一
    print(arr1[:5])                 # 前5歌数据
    print(arr1[-2:])                # 取最后两个数据


2:二维
    import numpy as np
    arr1 = np.arange(2,14)
    arr2 = arr1.reshape(3,4)
    print(arr2[1])
    print(arr2[1][1])
    print(arr2[1,1])
    print(arr2[:,2])          # 包括所有的行，第3列
    for i in arr2:            # 迭代行
        print(i)
    for i in arr2.T:          # 迭代列
        print(i)
    for i in arr2.flat:
        print(i)
