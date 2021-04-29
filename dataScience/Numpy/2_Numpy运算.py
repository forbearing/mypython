1:基本运算
    import numpy as np
    arr1 = np.array([[1,2,3],
                    [4,5,6]])
    arr2 = np.array([[1,1,2],
                   [2,3,3]])

    # 矩阵相加，按位相加
    print(arr1 + arr2)
    # 矩阵相减，按位减
    print(arr2 - arr1)
    # 矩阵相乘
    print(arr1 * arr2)
    # 幂
    print(arr1 ** arr2)
    # 除法
    print(arr1 / arr2)
    # 取余
    print(arr1 % arr2 )
    # 取整
    print(arr1 // arr2)

    print(arr1 + 2)      # 所有元素都加2
    print(arr1 * 10)     # 所有元素都乘10

    # 判断
    arr3 = arr1 > 3
    print(arr3)


2:矩阵运算
    arr1 = np.array([[1,2,3],
                    [4,5,6]])
    arr2 = np.ones((3,5))
    # 矩阵乘法
    np.dot(arr1, arr2)
    print(arr1.dot(arr2))
    # 转置
    print(arr1.T)
    print(np.transpose(arr1))

3:随机数
    import numpy as np
    # 3行2列，随机数从0-1
    sample1 = np.random.random((3,2))
    print(sample1)
    # 3行2列，符合标准正态分布的随机数
    sample2 = np.random.random(size=(3,2))
    # 3行2列，生成从0-10的随机整数
    sample3 = np.random.randint(0,10,size=(3,2))
    np.sum(sample3)
    np.min(sample3)
    np.max(sample3)
    np.sum(sample3, axis=0)    # 对列求和
    np.sum(sample3, axis=1)    # 对行求和
    np.argmin(sample3)         # 最小值元素的索引
    np.argmax(sample3)         # 最大值元素的索引
    np.mean(sample3)           # 求元素平均值
    print(sample3.mean())      # 求元素平均值
    np.median(sample3)         # 求元素中位数
    np.sqrt(sample3)           # 求元素开方

    sample5 = np.random.randint(1,10, size=(1,10))
    print(sample5)
    np.sort(sample5)
#    np.clip(sample5, 2, 7)     # 小于2为2，大于7为7,
