#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

plt.scatter(np.arange(5), np.arange(5))
plt.show()

x = np.random.normal(0,1,1000)
y = np.random.normal(0,1,1000)

plt.xlim((-2,2))
plt.ylim((-2,2))
plt.xticks(())
plt.yticks(())

plt.scatter(x, y, s=5, c='b', alpha=0.5)    # s:大小 c:颜色 alpha:透明度

