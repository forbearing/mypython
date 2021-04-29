import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,100)
y1 = 2*x + 1
y2 = x**2

# 设置 x、y轴的范围
plt.xlim((-1,2))
plt.ylim((-2,3))

# x、y轴描述
plt.xlabel('x label')
plt.ylabel('y label')

# 设置 x、y 轴的刻度
new_ticks = np.linspace(-2,2,11)
plt.xticks(new_ticks)
plt.yticks([-1, 0, 1, 2, 3],
        ['level1', 'level2', 'level3', 'level4', 'level5'])

# gca 获取当前坐标轴
ax = plt.gca()
ax.spines['right'].set_color('none')        # 去掉右边的边框
ax.spines['top'].set_color('none')          # 去掉顶部的边框
# 把 x 轴的刻度设置为 botton
# 把 y 轴的刻度设置为 left
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 设置 bottom 对应到0点
# 设置 left 对应到0点
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')     # linestyle='--' 代表虚线
plt.plot(x, y2, color='blue', linewidth=3.0, linestyle='-')     # linestyle='-' 代表实线
plt.show()



