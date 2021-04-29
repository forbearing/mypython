1:创建绘图对象--figure图像
plt.figure(num=None,figsize=None,dpi=None,facecolor=None,edgecolor=None,
               frameon=True,FigureClass=<class 'matplotlib.figure.Figure'>,clear=False,**kwargs)
    num：接收 int 或 string，可选，默认值为 None。如果该参数未提供，将创建新图形，并且图形编号将递增，图形对象将此数字保存在数字属性中。如果提供了 num，并且已存在具有此 num 的数字，请将其设置为活动状态，并返回对它的引用。如果此图不存在，则创建它并返回它。如果 num 是一个字符串，则窗口标题将设置为此数字的 num；
    figsize：接收整数元组（tuple），可选，默认值为 None。该参数指定绘图对象的宽度和高度，单位为英寸。如果没有提供，默认为 rcfigure.figsize；
    dpi：接收 int，可选，默认值为 None。该参数指定绘图对象的分辨率，即每英寸多少个像素。如果没有提供，默认值为 80 或默认为 rcfigure.dpi；
    facecolor：可选，默认值为 None。该参数指定背景颜色。如果未提供，默认为 rcfigure.facecolor；
    edgecolor：可选，默认值为 None。该参数指定边框颜色。如果未提供，则默认为 rcfigure.edgecolor；
    frameon：接收 boolean，可选，默认值为 True。如果为 False，则禁止绘制图框；
    FigureClass：从 matplotlib.figure.Figure 派生的类，可选，使用自定义图形实例；
    clear：接收 boolean，可选，默认值为 False。如果为 True，并且该图已经存在，那么它将被清除。

2:绘制图表
plt.plot(x,y,label,color,linewidth,linestyle)或 plt.plot(x,y,fmt,label)
    label：给所绘制的曲线设置一个名字，此名字在图例（Legend）中显示。只要在字符串前后添加“$”符号，
        Matplotlib 就会使用其内嵌的 LaTeX 引擎来绘制数学公式；
    color：指定曲线的颜色
    linewidth：指定曲线的宽度
    linestyle：指定曲线的样式
    fmt：指定曲线的颜色和线型，如“b—”，其中b表示蓝色，“—”表示线型为虚线，该参数也称为格式化参数。
        在 IPython 中输入“plt.plot?”，可以查看格式化字符串的详细配置。

3:添加各类标签和图例
    plt.xlabel()	在当前图形中指定 x 轴的名称，可加指定位置、颜色、字体大小等参数
    plt.ylabel()	在当前图形中指定 y 轴的名称，可以指定位置、颜色、字休大小等参数
    plt.title()	在当前图形中指定图表的标题，可以指定标题名称、位置、颜色、字体大小等参数
    plt.xlim()	指定当前图形 x 轴的范围，只能输入一个数值区间，不能使用字符串
    plt.ylim()	指定当前图形 y 轴的范围，只能输入一个数值区间，不能使用字符串
    plt.xticks()	指定 x 轴刻度的数目与取值
    plt.yticks()	指定 y 轴刻度的数目与取值
    plt.legend()	指定当前图形的图例，可以指定图例的大小、位置和标签

4:保存和显示图表
    plt.savefig()	保存绘制的图表为图片,可以指定图表的分辨率、边缘和颜色等参数
    plt.show()	在本机显示图表

5:绘制子图
    1:将一个绘图对象分为几个绘图区域，在每个绘图区域中可以绘制不同的图像
    2:subplot(numRows,numCols,plotNum)
    3:参数说明
        numRows：表示将整个绘图区域等分为 numRows 行
        numCols：表示将整个绘图区域等分为 numCols 列
        plotNum：表示当前选中要操作的区域
    4:subplot() 函数的作用就是将整个绘图区域等分为 numRows（行）×numCols（列）个子区域，
      然后按照从左到右、从上到下的顺序对每个子区域进行编号，左上的子区域的编号为 1。
    5:如果 numRows、numCols 和 plotNum 这 3 个数都小于 10，可以把它们缩写为一个整数，
      例如 subplot(223) 和 subplot(2,2,3) 是相同的。subplot() 在 plotNum 指定的区域中
      创建图形。如果新创建的图形和先前创建的图形重叠，则先前创建的图形将被删除。




---
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)
plt.figure(figsize=(10,6))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=3)
plt.plot(x,z,"b--",label="$cos(x)$")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('my title')
plt.legend()
plt.show()


---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)
k = x
plt.subplot(221)                 # 第一行的左图
plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.subplot(222)                 # 第一行的右图
plt.plot(x, z, 'b--', label="$cos(x)$")
plt.subplot(212)                 # 第二行整行
plt.plot(x, k, 'g--', label="$x$")
plt.legend()
plt.savefig('/Users/jonas/Desktop/1.png', dpi=3000)   # dpi是指保存图像的分辨率，默认值为80
#plt.savefig('/Users/jonas/Desktop/1.png', dpi=100)   # dpi是指保存图像的分辨率，默认值为80
