#!/usr/bin/env python3

import sys
import psutil
import re

if len(sys.argv) < 2:
    print("Usage:", sys.argv[0], "[pid]")
    sys.exit(1)

if not str.isdigit(sys.argv[1]):
    print("pid 必须是数字 ")
    sys.exit(1)


# try:
    # proc = psutil.Process(int(sys.argv[1]))
# except ProcessLookupError as e:
    # print("你输入的 pid 不存在")
    # sys.exit(1)

proc = psutil.Process(int(sys.argv[1]))
print("进程名称:", proc.name())
print("进程工作目录:", proc.cwd())
print("进程启动的命令行:", proc.cmdline())
print("进程父进程ID:", proc.ppid())
print("进程父进程:", proc.parent())
#print("进程的子进程列表:", proc.children())
print("进程状态:", proc.status())
print("进程用户名:", proc.username())
print("进程创建时间:", proc.create_time())
print("进程终端:", proc.terminal())
print("进程使用的CPU时间:", proc.cpu_times())
print("进程使用的内存:", proc.memory_info())
print("进程打开的文件:", proc.open_files())
print("进程相关网络连接:", proc.connections())
print("进程的线程数量:", proc.num_threads())
