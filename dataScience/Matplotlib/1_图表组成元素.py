1:plot() -- 展现变量的趋势变化
    函数功能：展现变量的趋势变化
    调用签名： plt.plot（x，y，Is="一" ，Iw=2，label="plot figure'"）参数说明
    参数说明
        x： x轴上的数值。
        y： y轴上的数值。
        ls： 折线图的线条风格。
        lw：折线图的线条宽度。
        label：标记图形内容的标签文本。
    ---
    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame
    import matplotlib
    import matplotlib.pyplot as plt

    x = np.linspace(0.5, 3.5, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plt.plot(x,y1, ls='-', lw=2, label='$sin(x)$')
    plt.plot(x,y2)
    plt.legend()
    plt.show()


2:scatter -- 寻找变量之间的关系
    函数功能：寻找变量之间的关系
    调用签名： plt.scatter（x，y1，c="b"，label="scatter figure"）参数说明
    参数说明
        x： x轴上的数值。
        y： y轴上的数值。
        C： 散点图中的标记的颜色。
        label： 标记图形内容的标签文本。
    ---
    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame
    import matplotlib
    import matplotlib.pyplot as plt

    x = np.linspace(0.05, 10, 1000)
    y = np.random.randn(1000)
    plt.scatter(x,y, c='g', label="scatter figure")
    plt.legend()
    plt.show()


3:xlim() -- 设置X轴的数值显示范围
    函数功能：设置x轴的数值显示范围
    调用签名： plt.xlim（xmin，xmax）
    参数说明
        xmin： x轴上的最小值。
        xmax： x轴上的最大值。
        平移性： 上面的函数功能，调用签名和参数说明同样可以平移到函数ylim（）上.
    ---
    x = np.linspace(0.05, 10, 1000)
    y = np.random.randn(1000)
    plt.scatter(x,y, c='g', label="scatter figure")
    plt.legend()
    plt.xlim(0.05, 10)
    plt.show()


4:label() -- 设置X轴的标签文件
    函数功能：设置x轴的标签文本。
    调用签名： plt.xlabel（string）
    参数说明
        string：标签文本内容。
        平移性：上面的函数功能，调用签名和参数说明同样可以平移到函数ylabel（）上
    ---
    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame
    import matplotlib
    import matplotlib.pyplot as plt

    x = np.linspace(0.05, 10, 1000)
    y = np.sin(x)
    plt.plot(x,y, ls='-.', lw=2, c='c', label="plot figure" )
    plt.legend()
    plt.show()


5:grid() -- 绘制刻度线的网格线
    函数功能：绘制刻度线的望各县
    调用签名：plt.grid(linestyle=":", color="r")
    参数说明
        linestyle：网格线的线条风格
        color：网格线的线条颜色
    ---
    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame
    import matplotlib
    import matplotlib.pyplot as plt

    x = np.linspace(0.05, 10, 1000)
    y = np.sin(x)
    plt.plot(x,y, ls='-.', lw=2, c='c', label="plot figure" )
    plt.legend()
    plt.grid(linestyle=":", color="r")
    plt.show()


6:axhline() -- 绘制平行于 x 轴的水平参考线
    函数功能：绘制平行于x轴的水平参考线
    调用签名： plt.axhline(y=0.0, c='r', ls='--', lw=2)
    参数说明
    y： 水平参考线的出发点。
    c： 参考线的线条颜色。
    ls：参考线的线条风格。
    lw：参考线的线条宽度。
    平移性：.面的函数功能，调用签名和参数说明同样可以平移到函数axvline()上。
    ---
    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame
    import matplotlib
    import matplotlib.pyplot as plt

    x = np.linspace(0.05, 10, 1000)
    y = np.sin(x)
    plt.plot(x,y, ls='-.', lw=2, c='c', label="plot figure" )
    plt.legend()
    plt.axhline(y=0.0, c='r', ls='--', lw=2)
    plt.axvline(x=4.0, c='r', ls='--', lw=2)
    plt.show()


7:axvspan() -- 绘制垂直于x轴的参考区域
    函数功能：绘制垂直于x轴的参考区域。
    调用签名： pltaxvspan（xmin=1.0，xmax =2.0，facecolor="y" ，alpha=0.3）
    参数说明
    xmin： 参考区域的起始位置。
    xmax： 参考区域的终止位置。
    facecolor：参考区域的填充颜色。
    alpha：参考区域的填充颜色的透明度。
    平移性： 上面的函数功能、调用签名和参数说明可以平移到函数axhspan（上。
    ---
    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame
    import matplotlib
    import matplotlib.pyplot as plt

    x = np.linspace(0.05, 10, 1000)
    y = np.sin(x)
    plt.plot(x,y, ls='-.', lw=2, c='c', label="plot figure" )
    plt.legend()
    plt.axvspan(xmin=4.0, xmax=6.0, facecolor='y', alpha=0.3)
    plt.axhspan(ymin=0.0, ymax=0.5, facecolor='y', alpha=0.3)
    plt.show()


8:annotate() -- 添加图形内容细节的指向型注释文本
    函数功能：添加图形内容细节的指向型注释文本
    调用签名：plt.annotate(string, xy=(np.pi/2,1.0), xytext=((np.pi/2)+0.15,1.5), weight="bold", color='b',
            arrowprops=dict(arrowstyle="->", cconnectionstyle="arc3", color="b"))
    参数说明
        string： 图形内容的注释文本。
        xy： 被注释图形内容的位置坐标。
        xytext： 注释文本的位置坐标。
        weight： 注释文本的字体粗细风格。
        color： 注释文本的字体颜色。
        arrowprops：指示被注释内容的箭头的属性字典。
    ---
    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame
    import matplotlib
    import matplotlib.pyplot as plt

    x = np.linspace(0.05, 10, 1000)
    y = np.sin(x)
    plt.plot(x,y, ls='-.', lw=2, c='c', label="plot figure" )
    plt.legend()
    plt.annotate("maximum",
                 xy=(np.pi/2, 1.0),
                 xytext=((np.pi/2)+1.0, .8),
                 weight='bold',
                 color='b',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='b'))
    plt.show()


9:text() -- 添加图形内容细节的无指向型注释文本嗯
    函数功能：添加图形内容细节的指向型注释文本
    调用签名：plt.text(x,y, string, weight='bold', color='b')
    参数说明：
        x：注释文本内容所在位置的横坐标。
        y：注释文本内容所在位置的纵坐标。
        string：注释文本内容。
        weight： 注释文本内容的粗细风格。
        color：注释文本内容的字体颜色。
    ---
    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame
    import matplotlib
    import matplotlib.pyplot as plt

    x = np.linspace(0.05, 10, 1000)
    y = np.sin(x)
    plt.plot(x,y, ls='-.', lw=2, c='c', label="plot figure" )
    plt.legend()
    plt.text(3.10, 0.09, "y=sin(x)", weight="bold", color='b')
    plt.show()


10:title() -- 添加图形内容的标题
    函数功能：添加图形内容的标题
    调用签名：plt.title(string)
    参数说明
        string：图形内容的标题文本
    ---
    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame
    import matplotlib
    import matplotlib.pyplot as plt

    x = np.linspace(0.05, 10, 1000)
    y = np.sin(x)
    plt.plot(x,y, ls='-.', lw=2, c='c', label="plot figure" )
    plt.legend()
    plt.text(3.10, 0.09, "y=sin(x)", weight="bold", color='b')
    plt.show()


11:legend() -- 表示不同图例的文本标签图例
    函数功能：标示不同图形的文本标签图例
    调用签名：plt.legend(loc='lower left')
    参数说明：
        loc：图例在图中的地理位置
    ---
    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame
    import matplotlib
    import matplotlib.pyplot as plt

    x = np.linspace(0.05, 10, 1000)
    y = np.sin(x)
    plt.plot(x,y, ls='-.', lw=2, c='c', label="plot figure" )
    # plt.legend(loc="lower left")
    # plt.legend(loc="lower right")
    # plt.legend(loc="upper left")
    plt.legend(loc="upper right")
    plt.show()



函数组合应用
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm as cm

# define data
x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)
y1 = np.random.randn(100)

# scatter figure
plt.scatter(x, y1, c='0.25', label='scatter figure')

# plot figure
plt.plot(x, y, ls='--', lw=2, label='plot figure')

# some clean up(removing chartjunk)
# turn the top spine and the right spine off
for spine in plt.gca().spines.keys():
    if spine == 'top' or spine == 'right':
        plt.gca().spines[spine].set_color('none')

# turn bottom tick for x-axis on
plt.gca().xaxis.set_ticks_position('bottom')
# set tick_line position of bottom

# leave left ticks for y-axis on
plt.gca().yaxis.set_ticks_position('left')
# set tick_line position of left

# set x,yaxis limit
plt.xlim(0.0, 4.0)
plt.ylim(-3.0, 3.0)

# set axes label
plt.ylabel("y_axis")
plt.xlabel("x_axis")

# set x,yaxis grid
plt.grid(True, ls=":", color="r")

# add a horizontal line across the axis
plt.axhline(y=0.0, c='r', ls='--', lw=2)

# add a vertical span across the axis
plt.axvspan(xmin=1.0, xmax=2.0, facecolor="y", alpha=.3)

# set annotating info
plt.annotate("maximum", xy=(np.pi/2, 1.0), xytext=((np.pi/2)+0.15, 1.5),
             weight='bold', color='r', 
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='r'))
plt.annotate('spines', xy=(0.75, -3), xytext=(0.35, -2.25),
             weight='bold', color='b',
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='b'))
plt.annotate('', xy=(0, -2.78), xytext=(0.4, -2.32),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='b'))
plt.annotate('', xy=(3.5, -2.98), xytext=(3.6, -2.70),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='b'))

# set text info
plt.text(3.6, -2.70, "'|' is tickline", weight='bold', color='b')
plt.text(3.6, -2.95, "3.5 is ticklabel", weight='bold', color='b')

# set title
plt.title("structure of matplotlib")

# set legend
plt.legend()

plt.show()
