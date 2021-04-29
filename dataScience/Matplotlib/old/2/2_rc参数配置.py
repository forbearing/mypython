Matplotlib 配置文件
    1:在绘制图形时，有许多需要配置的属性，比如颜色，字体，线型。但是在许多情况下，这些
      属性是直接采用了 Matplotlib 的默认配置。Matplotlib 将默认配置保存在 "Matplotlib" 
      配置文件中。通过修改这些配置文件，可修改图标的默认样式。
    2:配置文件搜索路径
        1:当前路径：程序的当前路径
        2:用户配置路径：在用户文件夹的 ".matplotlib" 目录下，可通过环境变量 "MATPLOTLIBRC"
          修改它的位置
        3:系统配置路径：保存在 Matplotlib 的安装目录下
    3:获取用户配置路径和系统配置路径
        import matplotlib
        print(matplotlib.get_configdir())           获取用户配置路径
        print(matplotlib.matplotlib_fname())        获取系统配置路径
    4:读取配置文件中的所有参数及参数值
        print(matplotlib.rc_params())




设置动态 rc 参数
#
1:直接修改 rcParams 变量值
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.rc_params()              # 读取配置文件中的所有参数及其参数值
    plt.rcParams["lines.marker"] = "v"  # 设置标记符 lines.marker为"v" 一角朝下的三角形
    plt.plot([1,2,3])
    plt.show()

2:使用 rc 函数修改参数配置
    matplotlib.rc(group, **kwargs)
        group：为 rc 参数的分组。线条常用的 rc 参数名称解释与取值如下
            lines.linewidth     线条宽度        取 0〜10 之间的数直 默认为 1.5
            lines.linestyle     线条样式        可取实线“-”、长虚线“--”、点线“-·”短虚线":"4 种，默认 为实线“—”
            lines.marker        线条上点的形状  可取“.” o”"v" “^”等 20 多种，默认为 None
            lines.markersize    点的大小        取 0〜10 之间的数值，默认为 1
    lines.marker 参数的 20 种取值及其代表的意义
        参数取值	意义        参数取值	意义
            o	    圆圈            .	    点
            D	    菱形            S	    正方形
            h	    六边形1         *	    星号
            H	    六边形2         d	    小菱形
            -	    水平线          v	    角朝下的三角形
            8	    八边形          <	    角朝左的三角形
            P	    五边形          >	    角朝右的三角形
            ，	    像素            ^	    角朝上的三角形
            +	    加号            \	    竖线
            None	无

---
import matplotlib
import matplotlib.pyplot as plt
import numpy
import pandas
from pandas import Series, DataFrame

# plt.rcParams["lines.marker"] = "v"
matplotlib.rc("lines", marker="o", linewidth=3, linestyle="--")
font = {
    'family': 'monospace',
    'style': 'italic',
    'size': '16'}
matplotlib.rc("font", **font)
plt.title("rc() example")
plt.plot([1,2,3])
plt.show()
