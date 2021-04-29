#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,100)
y1 = 2*x + 1
y2 = x**2

plt.xlim((-1,2))
plt.ylim((-2,3))

plt.xlabel('x axis')
plt.ylabel('y axis')

L1 = plt.plot(x,y1, color='red', linewidth=1.0, linestyle='--')
L2 = plt.plot(x,y2, color='blue', linewidth=5.0, linestyle='-')

new_ticks = np.linspace(-2,2,11)
plt.xticks(new_ticks)
plt.yticks([-1, 0, 1, 2, 3],
          ['level1', 'level2', 'level3', 'lenvel4', 'level5'])

plt.legend(handles=[L1, L2], labels=['test1', 'test2'], loc='best')

plt.show()
