#!/usr/bin/env python3

1:StringIO 能操作的只能是 str，如果要操作二进制数据，就需要 BytesIO
  BytesIO 实现了在内存中读写 Bytes。
    from io import BytesIO
    f = BytesIO()
    f.write('中文'.encoding('utf-8'))
    print(f.getvalue())
    # 写入的不是 str，而是经过 utf-8 编码过的 bytes

    f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    f.read()

2:StringIO 和 BytesIO 是在内存中操作 str 和 bytes 的方法，使得和读写文件具有一致的接口
