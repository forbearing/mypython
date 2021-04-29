#!/usr/bin/env python3

import numpy as np
import pandas as pd

file = pd.read_csv(r"C:\Users\jonas\Documents\people.csv", encoding="gbk")
print(file)
file.iloc[2,0] = '深圳'
print(file)
file.to_csv(r"C:\Users\jonas\Documents\people2.csv", encoding="gbk")
file.to_json()
file.to_excel()
