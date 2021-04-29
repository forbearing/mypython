import numpy as np
arr = np.array([1,2,3])
arr1 = arr                  # 浅拷贝，共享一块内存
arr1[0] = 5
print(arr)
print(arr1)
print(id(arr), id(arr1))

arr2 = arr.copy()           # 深拷贝，不共享内存
arr2[0] = 10
print(arr)
print(arr2)
print(id(arr), id(arr2))
