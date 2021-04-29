#!/usr/bin/env python3

1:序列化
    1:把变量从内存变成可存储或传输的过程。序列化之后，可以把序列化后的内容写入磁盘，
      或者通过网络传输到别的机器上。
    2:pickling, unpickling
    3:Pickle 的问题和所有编程语言特有的序列化问题一样。他只能用于 Python，并且可能
      不同版本的 Python 批次不兼容，因此，只能用 Pick 保存那些不重要的数据，不能成功
      反序列化也没关系。

import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps()

import pickle
with open('/tmp/dump.txt', 'wb') as f:
    pickle.dump(d, f)

with open('/tmp/dump.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)
