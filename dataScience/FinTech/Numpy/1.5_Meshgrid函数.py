#!/usr/bin/env python3

1:用法
    [X,Y]=meshgrid(x,y)
    [X,Y]=meshgrid(x) 与 [X,Y]=meshgrid(x,x) 是等同的
    [X,Y,Z]=meshgrid(x,y,z) 生成三维数组，可用来计算三变量的函数和绘制三维立体图

    import numpy as np
    import matplotlib.pyplot as plt

    %matplotlib inline

    m,n = (5,3)
    x = np.linspace(0,1,m)
    y = np.linspace(0,1,n)
    X, Y = np.meshgrid(x,y)


2:应用
    Meshgrid 函数常用的场景有等高线绘制及机器学习中 SVC 超平面的绘
