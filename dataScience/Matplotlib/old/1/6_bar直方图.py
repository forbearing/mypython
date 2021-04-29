#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = 2**x + 10
plt.bar(x,y)
plt.bar(x, y, facecolor='#9999ff', edgecolor='white')
for x,y in zip(x,y):
    plt.text(x, y, '%.2f' %y, ha='center', va='bottom')
    plt.text(x, y, '%.2f' %y, ha='center', va='top')
plt.show()
