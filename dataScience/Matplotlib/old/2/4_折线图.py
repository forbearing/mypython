#!/usr/bin/env python3
1:
    折线图的主要功能是查看因变量 y 随着自变量 x 改变的趋势，最适合于显示随时间
    （根据常用比例设置）而变化的连续数据。同时还可以看出数量的差异和增长趋势的变化

2:绘制折线图的函数为 plot
    matplotlib.pyplot.plot(*args,**kwargs)
        x,y         接收 array。表示 x 轴和 y 轴对应的数据，无默认
        color       接收特定 string。指定线条的颜色，默认为 None
        linestyle   接收特定 string。指定线条的类型，默认为“-”
        marker      接收特定 string。表示绘制的点的类型，默认为 None
        alpha       接收 0~1 的小数。表示点的透明度，默认为 None
