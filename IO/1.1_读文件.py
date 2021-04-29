#!/usr/bin/env python3

1:有时候文件会产生 IOError，一旦出错，后面的 close() 方法就不会执行
    try:
        f = open('/tmp/file.txt', 'r')
        print(f.read())
    finally:
        if f:
            f.close()
2:with 语句会自动帮我们调用 close 方法
    with open('/tmp/file.txt', 'r') as f:
        print(f.read())
3:如果文件内容非常大，如果20G，内存就会爆。readline 每次只读取一行内容。
  readlines() 一次读取所有内容并返回 list。
  如果文件很小，read() 一次性读取最方便。如果不确定文件大小，反复调用read(size) 
  比较保险。如果是配置文件，调用 readlines() 最方便。
    for line in f.readlines():
        print(line.strip())         # 把末尾的 '\n' 删掉
3:读取二进制文件
    f = open('/tmp/file.txt', 'rb')
    f.read()
4:读取非 UTF-8 编码的文本文件
    f = open('/tmp/file.txt', 'r', encoding='gbk')
    f.read()
5:遇到有些编码不规范的文件，你可能会遇到 UnicodeDecodeError, 因为在文本文件中可能夹杂
  了一些非法编码的字符。直接忽略
  f = open('/tmp/file.txt', 'r', encoding='gbk', errors='ignore')
