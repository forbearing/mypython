#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


m, n = (5,3)
x = np.linspace(0,1,m)
y = np.linspace(0,1,n)
X, Y = np.meshgird(x,y)
print(X)
print(Y)
