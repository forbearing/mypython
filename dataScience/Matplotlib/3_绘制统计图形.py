1:柱状图
    1:应用场景
        柱状图主要是应用在定性数据的可视化场景中，或者是离散型数据的分布展示。例如，
        一个本科班级的学生的籍贯分布，出国旅游人士的职业分布以及下载一款 App 产品的
        操作系统的分布。
    2:通过 mpl.rcParams['font.sans-serif']=['SimHei'] 来完成字体配置任务。
    3:不使用默认的 "Unicode minus" 模式来处理坐标轴轴线的刻度标签是负数的情况，一般可以
      使用 "ASCII hyphen" 模式来处理坐标轴轴线的负刻度值的情况，即通过
      mpl.rcParams['axes.unicode_minus'] = False 语句实现模式的选择
    4:各参数的含义
        x：柱状图中的柱体标签值
        y：柱状图中的柱体高度
        align：柱体对齐方式
        color：柱体颜色
        tick_label：刻度标签值
        alpha：柱体的透明度

    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    x = [1,2,3,4,5]
    y = [6,10,4,5,1]

    plt.bar(x, y, align='center', color='b', alpha=0.6,
            tick_label=['A', 'B', 'C', 'D', 'E'])
    plt.xlabel('测试难度')
    plt.ylabel('试卷份数')
    plt.grid(True, axis='y', ls=':', color='r', alpha=0.3)

    plt.show()


2:条形图
    1:barh(x, y, align='center', color='k', tick_label=['A','B','C','D','E'])
      x 是 y 轴上柱体标签值，
      y 是柱体宽度，在x轴上显示
      tick_label 表示y轴上的柱体标签值

    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    x = [1,2,3,4,5]
    y = [6,10,4,5,1]

    plt.barh(x, y, align='center', color='b', alpha=0.6,
            tick_label=['A', 'B', 'C', 'D', 'E'])
    plt.ylabel('测试难度')
    plt.xlabel('试卷份数')
    plt.grid(True, axis='x', ls=':', color='r', alpha=0.3)

    plt.show()


3:堆积图
    1:堆积柱状图
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    x = [1,2,3,4,5]
    y = [6,10,4,5,1]
    y1 = [2,6,3,8,5]
    plt.bar(x, y, align='center', color='#66c2a5', tick_label=['A','B','C','D','E'], label='班级A')
    plt.bar(x, y1, bottom=y, align='center', color='#8da0cb', label='班级B')
    plt.legend()
    plt.show()

    2:堆积条形图
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    x = [1,2,3,4,5]
    y = [6,10,4,5,1]
    y1 = [2,6,3,8,5]
    plt.barh(x, y, align='center', color='#66c2a5', tick_label=['A','B','C','D','E'], label='班级A')
    plt.barh(x, y1, left=y, align='center', color='#8da0cb', label='班级B')
    plt.legend()
    plt.show()


4:分块图
    1:多数据并列柱状图
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    x = np.arange(5)
    y = [6,10,4,5,1]
    y1 = [2,6,3,8,5]

    bar_width = 0.35
    tick_label = ['A','B','C','D','E']

    plt.bar(x, y, bar_width, align='center', color='c', alpha=0.5, label='班级A')
    plt.bar(x+bar_width, y1, bar_width, align='center', color='b', alpha=0.5, label='班级B')
    plt.xlabel('测试难度')
    plt.ylabel('试卷份数')

    plt.legend()
    plt.show()

    2:多数据平行条形图
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    x = np.arange(5)
    y = [6,10,4,5,1]
    y1 = [2,6,3,8,5]

    bar_width = 0.35
    tick_label = ['A','B','C','D','E']

    plt.barh(x, y, bar_width, align='center', color='c', alpha=0.5, label='班级A')
    plt.barh(x+bar_width, y1, bar_width, align='center', color='b', alpha=0.5, label='班级B')
    plt.xlabel('试卷份数')
    plt.ylabel('测试难度')

    plt.legend()
    plt.show()


参数探索
    在柱体上绘制装饰线或装饰图。也就是设置柱体的填充样式。可以使用关键字 hatch。
    例如："/", "\\", '|', '-'，每种符号字符串都是一种填充柱体的几何样式。符号字符串的
    富豪数量越多，柱体的几何图形的密集程度越高。
    plt.plot(x, y, align='center', color='c', tick_label=['A','B','C','D','E'], hatch='///')


5:堆积折线图、间断条形图和阶梯图
    在折线图、柱状图和条形图的绘制原理上衍生出来的统计图形。其分别是：
    堆积折线图、间断条形图、阶梯图

    1:stackplot() -- 绘制堆积折线图
    - 堆积折线图是通过绘制不同数据集的折线图而生成的。堆积折线图是按照垂直方向上彼此
      堆叠且又不互相覆盖的排列顺序，绘制若干条折线图而形成的组合图形
    ---
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.arange(1,6,1)
    y = [0,4,3,5,6]
    y1 = [1,3,4,2,7]
    y2 = [3,4,1,6,5]

    labels = ['BluePlanet', 'BrownPlanet', 'GreenPlanet']
    colors = ['#8da0cb', '#fc8d62', '#66c2a5']

    plt.stackplot(x, y, y1, y2, labels=labels, colors=colors)

    plt.legend(loc='upper left')
    plt.show()

    2:broken_barh() -- 绘制间断条形图
        1:间断条形图是在条形图的基础上绘制的，主要用来可视化定性数据的相同指标在时间维度
          上的指标值的变化情况，实现定性数据的相同指标的变化情况的有效直观比较
        2:[(60,90), (190,20), (230,30), (280,60)] 表示从起点是x轴的数值为60的起始位置起，
          沿着x轴方向移动90个单位。其他元祖的含义类似
        3:参数 (10,8) 表示从起点是y轴的数值为10的位置起，沿y轴正方向移动8个单位，这就是
          每个柱体的高度和垂直起始位置
        3:关键字参数 facecolors 表示每个柱体的填充颜色，这里使用 HEX 模式的颜色表示方法
    ---
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib as mpl

    mpl.rcParams['font.sans-serif'] = ['LiSu']
    mpl.rcParams['axes.unicode_minus'] = False

    bar1 = [(30,100), (180,50), (260,70), (20,8)]
    bar2 = [(60,90), (190,20), (230,30), (280,60)]
    colors1 = '#1f78b4'
    colors2 = ('#7fc97f', '#beaed4', '#fdc086', '#ffff99')

    plt.broken_barh(bar1, (20,8), facecolors=colors1)
    plt.broken_barh(bar2, (10,8), facecolors=colors2)

    plt.xlim(0,360)
    plt.ylim(5,35)
    plt.xlabel('演出时间')
    plt.xticks(np.arange(0,361,60))
    plt.yticks([15,25], ['歌剧院A', '歌剧院B'])
    plt.grid(ls='-', lw=1, color='gray')
    plt.title('不同地区的歌剧院的演出时间比较')

    plt.show()

    3:step() -- 绘制阶梯图
        1:阶梯图从图形本身而言，很想折线图，是反映数据的趋势变化或是周期性的。阶梯图经常使用
          在时间序列数据的可视化任务中，凸显时序数据的波动周期和规律。
        2:plt.step() 起参数的含义与用法与函数 plot() 完全相同
        3:参数 where 默认参数为 "pre", 参数值 "pre" 表示x轴上的每个数据点对应的y轴上的
          数值向左侧绘制水平线直到x轴上的此数据点的左侧相邻数据点为止，也就是说，x轴上
          的相邻数据点的取值是按照左开右闭区间进行数据点选取的。
        4:关键字参数 where 除了可以取值 "pre"，还可以取值 "post" 表示在x轴上的相邻数据点
          的取值是按照左闭右开区间进行数据点选取的，然后用对应的y轴上的数值向右测绘制
          水平线直到x轴上的此数据点的右侧相邻数据点为止。
    ---
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib import cm as cm

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    x = np.linspace(1,10,10)
    y = np.sin(x)

    plt.step(x, y, color='#8dd3c7', where='pre', lw=2)
    plt.xlim(0,11)
    plt.xticks(np.arange(0,11,1))
    plt.ylim(-1.2, 1.2)

    plt.show()


6:直方图
    1:应用场景 - 定量数据的分布展示
        直方图主要是应用在定量数据的可视化场景中，或者是用来进行连续型数据的可视化展示。
        比如，公共英语考试分数的区间分布、抽样调查中的人均寿命的分布特征以及居民可支配
        收入的分布特征。
    2:参数
        plt.hist(x, bins=bins, color='#377eb8', histtype='bar', rwidth=10)
        x:          连续数据输入值
        bins:       用于确定柱体的个数或是柱体边缘范围
        color:      柱体的颜色
        histtype:   柱体类型
        label:      图例内容
        rwidth:     柱体宽度
        - 除了第一个柱体的数据是闭区间，其他柱体的数据范围都是左闭右开区间，例如第一个
          柱体的数据范围是 [0,10) 最后一个柱体的数据范围是 [90,100]

    ---
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    scoresT = np.random.randint(0,100, 100)
    x = scoresT
    bins = range(0,101,10)

    plt.hist(x, bins=bins, color='#377eb8', histtype='bar', rwidth=10)
    plt.show()

    3:直方图和柱状图的关系
        1:直方图描述的是连续型数据的分布，柱状图描述的是离散型数据的分布
        2:直方图描述定量数据，柱状图描述定性数据
        3:直方图的柱体之间没有空隙，柱状图之间柱体有空隙
    4:堆积直方图
        1:关键字参数 stacked 来实现堆积直方图的绘制。
        2:绘制并排防治的直方图，stacked=False
        3:将直方图和阶梯图的特点结合起来即可绘制阶梯型直方图，也可以绘制堆积阶梯型直方图
          调整 hist() 函数的 histtype 参数即可
          histtype=stepfilled, stacked=True
    ---
    import matplotlib as mpl
    import numpy as np
    import matplotlib.pyplot as plt
#
    mpl.rcParams['font.sans-serif'] = 'SimHei'
    mpl.rcParams['axes.unicode_minus'] = 'False'

    scoresT1 = np.random.randint(0,100,100)
    scoresT2 = np.random.randint(0,100,100)
    x = [scoresT1, scoresT2]
    bins = range(0,101,10)
    colors = ['#8dd3c7', '#bebada']
    labels = ['班级A', '班级B']

    plt.hist(x, bins, stacked=True, histtype='bar', rwidth=10,
             color=colors, label=labels)
    plt.xlabel('测试成绩')
    plt.ylabel('学生人数')
    plt.title('不同班级的测试成绩的直方图')

    plt.legend(loc='upper left')
    plt.show()


7:饼图
    1:应用场景 - 定性数据的比例展示
        饼图主要应用在定性数据的可视化场景中，或者是用来进行离散型数据的比例展示。比如
        需要展示参加研究生考试的性别比例、某市一年中四季使用天然气用量的比重以及家庭
        生活开支用途的比例分布，这些场景都是使用饼图进行数据分析的不二之选。通过绘制
        饼图，就可以直观地反映研究对象定性数据的比例分布情况
    2:代码
    plt.pie(student, explode=explode, 
            labels=labels, colors=colors,
            autopct='%3.1f%%', startangle=45, shadow=True)
        student     饼片代表的百分比
        explode     存储每份饼片边缘偏离相邻边缘的半径长度比例值
        labels      标记每份饼片的文本标签内容
        colors      饼片的颜色
        autopct     饼片文本标签内容对应的数值百分比样式
        startangle  从x轴作为起始位置，每一个饼片逆时针选装的角度
        shadow      设定饼片中的每份饼片的投影
    ---
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        import numpy as np

        mpl.rcParams['font.sans-serif'] = ['SimHei']
        mpl.rcParams['axes.unicode_minus'] = False

        labels = 'A难度水平','B难度水平','C难度水平','D难度水平'
        students = [0.35, 0.15, 0.20, 0.30]
        colors = ['#377eb8', '#4daf4a', '#984ea3', '#ff7f00']
        explode = (0.1, 0.1, 0.1, 0.1)

        plt.pie(students, explode=explode,
               labels=labels,
               colors=colors,
               autopct='%3.1f%%',
               startangle=45,
               shadow=True)
        plt.title('选择不同难度测试试卷的学生百分比')

        plt.show()

    3:非分裂式饼图
        去掉参数 explode 即可。另外，我们可以设置参数 pctdistance 和 labeldistance
        的具体取值，这两个参数分别控制百分比数值和标签值的显示位置。他们都是以半径长度
        比例值作为显示位置依据的
    ---
        plt.pie(students,
                labels=labels,
                colors=colors,
                autopct='%3.1f%%',
                pctdistance=0.7,
                labeldistance=1.2,
                startangle=45,
                shadow=True)

    4:绘制内嵌环形饼图
    ---
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        import numpy as np

        mpl.rcParams['font.sans-serif'] = ['SimHei']
        mpl.rcParams['axes.unicode_minus'] = False

        elements = ['面粉', '砂糖', '奶油', '草莓酱', '坚果']

        weight1 = [40,15,20,10,15]
        weight2 = [30,25,15,20,10]

        colormapList = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']
        outer_colors = colormapList
        inner_colors = colormapList

        wedges1, texts1, autotexts1 = plt.pie(weight1,
                                             autopct='%3.1f%%',
                                             pctdistance=0.85,
                                             radius=1,
                                             colors=outer_colors,
                                             textprops=dict(color='w'),
                                             wedgeprops=dict(width=0.3,edgecolor='w'))
        wedges2, texts2, autotexts2 = plt.pie(weight2,
                                             autopct='%3.1f%%',
                                             pctdistance=0.75,
                                             radius=0.7,
                                             colors=inner_colors,
                                             textprops=dict(color='w'),
                                             wedgeprops=dict(width=0.3, edgecolor='w'))
        plt.legend(wedges1,
                   elements,
                   fontsize=12,
                   title='配料表',
                   loc='center left',
                   bbox_to_anchor=(0.91, 0, 3, 1))
        plt.setp(autotexts1, size=15, weight='bold')
        plt.setp(autotexts2, size=15, weight='bold')
        plt.setp(texts1, size=10)
        plt.title('不同果酱面包配料比例表的比较')
        plt.show()


8:箱线图
    1:应用场景 - 多组定量数据的分布比较
        箱线图主要应用在一系列测量或观测数据的比较场景中，例如学校间或班级间测试成绩的
        比较，球队中的队员体能对比，产品优化前后的测试数据比较以及同类产品的各项性能的
        比较等。箱线图的应用范围非常广泛，而且实现起来也非常简单。
    2:代码
        1:参数
            testList    绘制箱线图的输入数据
            whis        四分位间距的倍数，用来确定箱须包含数据的范围的大小
            widths      设置箱体的宽度
            sym         离群值的标记样式
            labels      绘制每一个数据集的刻度标签
            path_artist 是否给箱体添加颜色
        - mpl.rcParams['axes.unicode_minus'] = 'False' 语句放弃了 "unicode_minus" 的使用，
          这样图形中的刻度标签值是负数的情况下就可以得到合理解决，即负数可以正确显示。
        - 我们需要对箱线图的返回值进行操作，这个返回值是一个字典结构，由于需要对箱体
          添加颜色，所以使用键 "boxes" 来调出键值 "bplot['boxes']"。最后使用内置函数
          zip() 生成元素列表 zip(bplot['boxes'], colors)，使用for循环对每个箱体进行
          颜色填充。
        - 关键字 notch 的参数值设置为 "True"，同时其他语句保持不变，那么箱体就变成 "V"
          型痕迹的箱体了
    ---
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        import numpy as np

        mpl.rcParams['font.sans-serif'] = 'FangSong'
        mpl.rcParams['axes.unicode_minus'] = 'False'

        testA = np.random.randn(5000)
        testB = np.random.randn(5000)

        testList = [testA, testB]
        labels = ['随机数生成器AlphaRM', '随机数生成器BetaRM']
        colors = ['#1b9e77', '#d95f02']

        whis = 1.6
        width = 0.35

        bplot = plt.boxplot(testList,
                           whis=whis,
                           widths=width,
                           sym='o',
                           labels=labels,
                           patch_artist=True)
        for path, color, in zip(bplot['boxes'], colors):
            path.set_facecolor(color)
        plt.ylabel('随机数')
        plt.title('生成器抗干扰能力的稳定性比较')
        plt.grid(axis='y', ls=':', lw=1, color='gray', alpha=0.4)
        plt.show()
    3:水平方向的箱线图
    ---
        x = np.random.randn(1000)
        plt.boxplot(x, vert=False)
        plt.xlabel('随机数')
        plt.yticks([1], ['随机数AlphaRM'], rotation=90)
        plt.title('随机数生成器抗干扰能力的稳定性')
        plt.grid(axis='x', ls=':', lw=1, color='gray', alpha=0.4)
    4:不绘制离群值的水平放置的箱线图
        - 在大多数情况下都是绘制包含离群值的箱线图。但是，也有很多时候，我们只需要绘制
          数据集的分布结构，也就是说，只需要标记出箱须的长度、上四分位数、下四分位数、
          中位数的位置，即可满足描述数据集的分布特征的目标。离群值不是重点要考虑的对象。
    ---
        x = np.random.randn(1000)
        plt.boxplot(x, vert=False, showfiles=False)
        plt.xlabel('随机数')
        plt.yticks([1], ['随机数AlphaRM'], rotation=90)
        plt.title('随机数生成器抗干扰能力的稳定性')
        plt.grid(axis='x', ls=':', lw=1, color='gray', alpha=0.4)
        plt.show()


9:误差棒图
    1:应用场景 - 定量数据的误差范围
        通过抽样获得样本，对总体参数进行估计会由于样本的随机性导致参数估计值出现波动，
        因此需要用误差棒图置信区间来表示对总体参数估计的可靠范围。误差棒就可以很好地
        实现充当总体参数估计的置信区间的角色。误差棒图的计算方法可以有很多种：单一数值、
        置信区间、标准差、标准误等。误差棒的可视化展示效果有很多种样式：
        水平误差棒图、垂直误差棒图、对称误差棒图和非堆成误差棒图等
    2:绘制原理
        plt.errorbar(x, y, yerr=error_limit, fmt=':o',
                ecolor='y', elinewidth=4,
                ms=5, mfc='c', mec='r',
                capthick=1, capsize=2)
        采用单一数值的非对称形式的误差棒，参数含义
            x,y         数据点的位置
            yerror      单一数值的非对称形式误差范围
            fmt         数据点的标记样式和数据点标记的连接线样式
            ecolor      误差棒的线条颜色
            elinewidth  误差棒的线条粗细
            ms          数据点的大小
            mfc         数据点的标记颜色
            mec         数据点的标记边缘颜色
            capthick    误差棒边界横杠的厚度
            capsize     误差棒边界横杠的大小
        1:关键字参数 xerr 也可以使用类似的误差范围
        2:关键字 fmt 如果取 "none" 时，数据点的连线，数据点的标记样式和颜色都不显示
        3:关键字 capthick 也可以用关键字参数 mew 代替
    ---
        x = np.linspace(0.1, 0.6, 10)
        y = np.exp(x)

        error = 0.05 + 0.15*x
        lower_error = error
        upper_error = 0.3*error
        error_limit = [lower_error, upper_error]

        plt.errorbar(x, y, yerr=error_limit,
                     fmt=':o',
                     ecolor='y', elinewidth=4,
                     ms=5, mfc='c', mec='r',
                     capthick=1, capsize=2)
        plt.xlim(0,0.7)
        plt.show()
    3:带误差棒的柱状图
        1:绘制误差棒的柱状图的关键要点，就是函数 bar() 中关键字参数 yerr 的使用。
        2:同时，误差棒的属性和属性值的控制都由关键字 error_kw 实现。
    ---
        x = np.arange(5)
        y = [100,68,79,91,82]
        std_err = [7,2,6,10,5]
        error_attri = dict(elinewidth=2, ecolor='black', capsize=3)

        plt.bar(x,y, 
                color='c',
                width=0.6,
                align='center',
                yerr=std_err,
                error_kw=error_attri,
                tick_label=['园区1','园区2','园区3','园区4','园区5'])

        plt.xlabel('芒果种植区')
        plt.ylabel('收割量')

        plt.title('不同芒果种植区的单次收割量')
        plt.grid(True, axis='y', ls=':', color='gray', alpha=0.2)

        plt.show()
    4:带误差棒的条形图
        1:带误差的条形图的绘制是通过 barh() 函数中的关键字参数 xerr 来实现的，
          其他关键字和用法相同
    ---
        x = np.arange(5)
        y = [1200, 2400, 1800, 2200, 1600]
        std_err = [150,100,180,130,80]

        bar_width = 0.6
        colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

        plt.barh(x, y,
                 bar_width,
                 color=colors,
                 align='center',
                 xerr=std_err,
                 tick_label=['家庭','小说','心理','科技','儿童'])
        plt.xlabel('订购数量')
        plt.ylabel('图书种类')
        plt.title('大型图书展销会的不同书种类的采购情况')

        plt.grid(True, axis='x', ls=':', color='gray', alpha=0.2)
        plt.xlim(0, 2600)
        plt.show()
