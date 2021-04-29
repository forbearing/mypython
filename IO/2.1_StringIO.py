#!/usr/bin/env python3

1:StringIO 数据读写在内存中进行
from io import StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World')
print(f.getvalue())
f.close()
