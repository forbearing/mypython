1:Numpy 数组对象
    1:Numpy 中的多维数组称为 ndarray，这是 Numpy 中最常见的数组对象。ndarray 对象通常包含两个部分:
        1:ndarray数据本身
        2:描述数据的元数据
    2:Numpy 数组的优势
        1:Numpy数组通常是由相同种类的元素组成的，即数组中的数据项的类型一致。这样有一个好处，
          由于知道数组 元素的类型相同，所以能快速确定存储数据所需空间的大小。
        2:Numpy数组能够运用向量化运算来处理整个数组，速度较快;而Python的列表则通常需要
          借助循环语句遍历 列表，运行效率相对来说要差。
        3:Numpy使用了优化过的CAPI，运算速度较快

    --- 时间消耗对比
    import time
    import numpy as np

    def pySum():
        a = list(range(1000000))
        b = list(range(1000000))
        c = []
        for i in range(len(a)):
            c.append(a[i]**2 + b[i]**2)
        return c

    def npSum():
        a = np.arange(1000000)
        b = np.arange(1000000)
        c = a**2 + b**2
        return c

    start = time.time()
    pySum()
    end = time.time()
    consume = end - start
    print("python consume time: %s" %consume)

    start = time.time()
    npSum()
    end = time.time()
    consume = end - start
    print("numpy consume time: %s" %consume)



2:创建 ndarray 数组
    1:基于 list 或 tuple
        arr = np.array([1,2,3,4])
        arr = np.array((1,2,3,4))
        arr = np.array([[1,2,3,4], [3,4,5,6]])      # 二维数组
    2:基于 np.arange
        arr1 = np.arange(5)
        arr2 = np.array([np.arange(3), np.arange(3)])
    3:基于 arange 以及 reshape
        arr = np.arange(24).reshape(6,4)
        arr = np.arange(24).reshape(2,3,4)



3:Numpy 的数值类型
    bool        布尔类型，True/False，占用1比特
    inti        其长度取决于平台的整数，一般为 int32 或 int64
    int8        字节长度的整数，取值: [-128, 127]
    int16       16位长度的整数，取值: [-32768, 32767]
    int32, int64
    unit8       8位无符号整数，取值: [0,255]
    unit16      16位无符号整数，取值: [0,65535]
    unit32, unit64
    float16     16位半精度浮点数：1位符号位，5位指数，10位尾数
    float32     32位半精度浮点数：1位符号位，8位指数，23位尾数
    float64     双精度度浮点数：1位符号位，11位指数，52位尾数
    float       同 float64
    complex64   复数类型，实部和虚部都是32位浮点数
    complex128  复数类型，实部和虚部都是64位浮点数
    complex     同 complex128

    1:数据转换函数
        np.int8(10.233)
        np.float(True)
        bool(10)
    2:创建数组时指定数值类型
        a = np.arange(5, dtype=float)
        a = np.arange(4, dtype='D')         # D 表示复数类型



4:ndarray 数组属性
    1:ndim: 数组维度数量
        arr = np.array([[1,2,3], [7,8,9]])
        print(arr.ndim)
    2:shape: 数组对象的尺度，即n行m列，shape是一个元组(tuple)
        arr.shape
    3:size: 用来保存元素的数量，相当于shape中nXm的值
        arr.size
    4:itemsize: 返回数组中各个元素所占用的字节数大小
        arr.itemsize
    5:nbytes: 整个数组所需的字节数量,其值等于数组的size属性值乘以 itemsize 属性值
        arr.nbytes
    6:T属性: 数组转置
        arr = np.arange(24).reshape(4,6)
        arr.T
    7:real, imag: 复数的实部和虚部
        d = np.array([1.2+2j, 2+3j])
        d.real
        d.imag
    8:flat: 返回一个numpy.flatiter对象，即可迭代的对象
        arr  = np.arange(12).reshape(3,4)
        arr1 = arr.flat
        for item in arr1:
            print(item)
        arr.flat = 10
        arr.flat[[1,4]] = 1



5:ndarray 数组的切片和索引
    1:一维数组
        a = np.arange(7)
        print(a[1:4])
        print(b[:6:2])
    2:二维数组的切片和索引
        b = np.arange(24).reshape(6,4)
        b[0:3, 0:2]



6:类型转换
    1:数组转换成 list，使用 tolist()
        a = np.arange(6)
        a.tolist()
        b = np.arange(12).reshape(2,6)
        b.tolist()
    2:转换成指定类型，astype()
        b.astype(float)
