#!/usr/bin/env python3

- os.name 如果是 posix，说明系统是 Linux、Unix、MacOS，如果是 nt，则是 windows
  获取详细信息 os.uname()

1:环境变量
    os.environ
    os.environ.gget('PATH')                     # 获取某个环境变量的值

2:操作文件和目录
    - 操作文件和目录的函数一部分放在 os 模块中，一部分放在 os.path 模块中。
    - 两个路径合成不要直接拼接字符串，而是通过 os.path.join() 函数，这样就可以正确处理
      不同操作系统之间的路径分隔符。
    - os 模块没有复制文件的函数，原因是复制文件并非由操作系统提供的系统调用。
      shutil 模块提供了 copyfile() 函数，shutil 模块可以看作 os 模块的补充
    os.path.abspath('.')                        # 查看当前目录的绝对路径
    os.path.join('/Users/hybfkuf', 'testdir')
    os.mkdir('/Users/hybfkuf/testdir')
    os.rmdir('/Users/hybfkuf/testdir')
    os.path.splitext('/path/to/file.txt')          # 拆分获得文件名扩展
    os.rename('test.txt', 'test.py')
    os.remove('test.py')                        # 删除文件
