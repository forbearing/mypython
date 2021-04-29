1:基本使用
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.linspace(-1,1,100)           # 生成100个-1到1的数据
    y = 2*x + 1
    plt.plot(x,y)
    plt.show()


2:figure
    # 在不同的 figure 中显示
    # 如果没有指定 figure，则曲线会在同一个 figure 中显示
    x = np.linspace(-1,1,100)
    y1 = 2*x + 1
    y2 = x**2
    plt.figure()
    plt.plot(x,y1)
    plt.figure()
    plt.plot(x,y2)

    # 线条属性
    plt.figure(figsize=(4,3))       # 指定 figure 大小
    plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')     # linestyle='--' 代表虚线
    plt.plot(x, y2, color='blue', linewidth=3.0, linestyle='-')     # linestyle='-' 代表实线
    plt.show()
