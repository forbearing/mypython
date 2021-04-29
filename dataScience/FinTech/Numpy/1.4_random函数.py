#!/usr/bin/env python3
import numpy as np

1:numpy.random.rand()
    numpy.random.rand(d0,d1,...,dn)
    1:rand 函数根据给定维度生成 [0,1) 之间的数据，包含 0，不包含 1
    2:dn表格每个维度
    3:返回值为指定维度的 array

    np.random.rand(4,2)
    np.random.rand(4,3,2)



2:numpy.random.randn()
    numpy.random.randn(d0,d1,...,dn)
    1:randn函数返回一个或一组样本，具有标准正态分布。
    2:dn表格每个维度
    3:返回值为指定维度的 array
    4:当没有参数时，返回单个数据

    np.random.randn()
    np.random.randn(2,4)
    np.random.randn(4,3,2)



3:numpy.random.randint()
    numpy.random.randint(low, high=None, size=None, dtype=“l”)
    1:返回随机整数，范围区间为 [low,high)，包含 low，不包含 high
    2:参数:low为最小值，high为最大值，size为数组维度大小，dtype为数据类型，默认的数据类型是np.int
    3:high没有填写时，默认生成随机数的范围是[0，low)

    np.random.randint(1,size=5)             # 返回[0,1)之间的随机整数，所以只有0
    np.random.randint(1,5)                  # 返回[0,5)之间的随机整数
    np.random.randint(-5,5,(2,2))



4:numpy.random.random_integers
    numpy.random.random_integers(low, high=None, size=None)
    1:返回随机整数，范围区间为 [low,high]，包含 low 和 high
    2:参数:low为最小值，high为最大值，size为数组维度大小
    3:high没有填写时，默认生成随机数的范围是[1，low]
    4:该函数在最新的 numpy 版本中已被替代，建议使用 randint 函数

    np.random.random_integers(1,size=5)



5:生成 [0,1) 之间的浮点数
    np.random.random()
    np.random.random(size=None)
    np.random.random(4)
    np.random.random(size=4)
    np.random.random(size=(2,2))

    np.random.sample(size=None)
    np.random.random_sample(size=None)
    np.random.ranf(size=None)



6:numpy.random.choice()
    numpy.random.choice(a, size=None, replace=True, p=None)
    1:从给定的一维数组中生成随机数
    2:参数:a为一维数组类似数据或整数;size为数组维度;p为数组中的数据出现的概率 
    3:a为整数时，对应的一维数组为np.arange(a)

    a = np.arange(12)
    np.random.choice(5,3)
    np.random.choice(5,3, replace=False)        
        # 当 replace 为 False 时，生成的随机数不能又重复的数值
    np.random.choice(a,3, replace=False)
    np.random.choice(a, size=(2,2))

    demo_list = ['lenovo', 'sansumg', 'moto', 'xiaomi', 'iphone']
    np.random.choice(demo_list, size=(3,3))

7:numpy.random.seed()
    1:np.random.seed()的作用:使得随机数据可预测。
    2:当我们设置相同的 seed，每次生成的随机数相同。如果不设置 seed，则每次会生成不同的随机数
    np.random.seed(0)
    np.random.rand(5)
