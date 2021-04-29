#!/usr/bin/env python3

1:如果反复调用 write() 写入文件，务必要调用 close() 方法来关闭文件。当我们写文件时，
  操作系统不会立即把数据写入磁盘，而是放入内存缓存起来。空闲的时候再慢慢写入。只有调用
  close() 方法时，操作系统才保证没有写入的数据全部写入磁盘。
2:with 语句自动调用 close()
    with open('/tmp/file.txt', 'w') as f:
        f.write('Hello World')
