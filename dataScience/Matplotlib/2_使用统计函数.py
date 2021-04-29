1:bar() -- 用于绘制柱状图
    函数功能：在 x 轴上绘制定性数据的分布特征
    调用签名：plt.bar(x)
    参数说明：
        x：标示x轴上的定性数据的类别
        y：每种定性数据的类别的数量
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    # some sample data
    x = [1,2,3,4,5,6,7,8]
    y = [3,1,4,5,8,9,7,2]

    plt.bar(x,y, align='center', color='c', hatch='/',
            tick_label=['one','two','three','four','five','six','seven','eight'])
    plt.xlabel('箱子编号')
    plt.ylabel('箱子重量(kg)')
    plt.show()


2:barh() -- 用于绘制条形图
    函数功能：在y轴上绘制定性数据的分布特征
    调用签名：plt.barh(x,y)
    参数说明：
        x：标示在y轴上的的定性数据的类别
        y：每种定性数据的类别的数量
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    # some sample data
    x = [1,2,3,4,5,6,7,8]
    y = [3,1,4,5,8,9,7,2]

    plt.barh(x,y, align='center', color='c', hatch='/',
            tick_label=['one','two','three','four','five','six','seven','eight'])
    plt.xlabel('箱子编号')
    plt.ylabel('箱子重量(kg)')
    plt.show()


3:hist() -- 用于绘制直方图
    函数功能：在x轴上绘制定量数据的分布特征
    调用签名：plt.hist(x)
    参数说明：
        x：在x轴上绘制箱体的定量数据输入值
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    # set test scores
    boxWeight = np.random.randint(0,10,100)
    x = boxWeight

    # plot histogram
    bins = range(0,11,1)
    plt.hist(x, bins=bins, color='g', histtype='bar', rwidth=1, alpha=0.6)

    plt.xlabel('箱子重量(kg)')
    plt.ylabel('销售个数(个)')
    plt.show()


4:pie() -- 用于绘制饼图
    函数功能：绘制定性数据的不同类别的百分比
    调用签名：plt.pie()
    参数说明：
        x：定性数据的不同类别的百分比
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    kinds = "简易箱","保温箱","行李箱","密封箱"
    #colors = ['#e41a1c','#377eb8','4daf4a','#984ea3']
    colors = ['red', 'green', 'blue', 'yellow']
    soldNums = [0.05, 0.45, 0.15, 0.35]

    plt.pie(soldNums, labels=kinds, colors=colors, autopct="%3.1f%%", startangle=60)
    plt.title('不同类型箱子的销售数量占比')
    plt.show()


5:polar() -- 用于绘制极线图
    函数功能：在极坐标轴上绘制折线图
    调用签名：plt.polar(theta, r)
    参数签名：
        theta：每个标记所在射线与极径的夹角
        r：每个标记到原点的距离
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    barSlices = 12
    theta = np.linspace(0.0, 2*np.pi, barSlices, endpoint=False)
    r = 30*np.random.rand(barSlices)

    plt.polar(theta, r,
              color='chartreuse',
              linewidth=2,
              marker='*',
              mfc='b',
              ms=10)

    plt.show()


6:scatter() -- 用于绘制气泡图
    函数功能：二维数据借助气泡大小展示三维数据
    调用签名：plt.scatter(x,y)
    参数说明：
        x：x轴上的数值
        y：y轴上的数值
        s：散点标记的大小
        c：散掂标记的颜色
        cmap：将浮点数映射成颜色的颜色映射表
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    a = np.random.randn(100)
    b = np.random.randn(100)

    # colormap:BdYlBu
    plt.scatter(a,b, s=np.power(10*a+20*b, 2),
                c=np.random.rand(100),
                marker='o')
    plt.scatter(a,b, s=np.power(10*a+20*b, 2),
                c=np.random.rand(100),
                cmap=mpl.cm.RdYlBu,   
                marker='o')


7:stem() -- 用于绘制棉棒图
    函数功能：绘制离散有序数据
    调用签名：plt.stem(x,y)
    参数说明：
        x：指定棉棒的x轴基线的位置
        y：绘制棉棒的长度
        linefmt：棉棒的样式
        markerfmt：棉棒末端的样式
        basefmt：指定基线的样式
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    x = np.linspace(0.5, 2*np.pi, 20)
    y = np.random.randn(20)

    plt.stem(x,y, linefmt='-.', markerfmt='o', basefmt='-')
    plt.show()


8:boxplot() -- 用于绘制箱线图
    函数功能：绘制箱线图
    调用签名：plt.boxplot(x)
    参数说明：
        x：绘制箱线图的输入数据
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    x = np.random.randn(1000)
    plt.boxplot(x)

    plt.xticks([1], ['随机数生成器AlphaRM'])
    plt.ylabel('随机数值')
    plt.title('随机数生成器抗干扰能力的稳定性')
    plt.grid(axis='y', ls=':', lw=1, color='gray', alpha=0.4)

    plt.show()


9:errorbar() -- 用于绘制误差棒图
    函数功能：绘制y轴方向或是x轴方向的误差范围
    调用签名：plt.errorbar(x,y, yerr=a, xerr=b)
    参数说明：
        x：数据点的水平位置
        y：数据点的垂直位置
        yerr：y轴方向的数据点的误差计算方法
        xerr：x轴方向的数据点的误差计算方法
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    # mpl.rcParams['font.sans-serif'] = ['SimHei']
    # mpl.rcParams['axes.unicode_minus'] = False

    x = np.linspace(0.1, 0.6, 6)
    y = np.exp(x)

    plt.errorbar(x,y, fmt='bo:', yerr=0.2, xerr=0.02)
    plt.xlim(0, 0.7)
    plt.show()
