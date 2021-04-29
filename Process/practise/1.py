#!/usr/bin/env python3
'''
编辑时间: 2020-06-10
'''

from multiprocessing import Process
import os
import time

# pid = os.fork()
# if pid < 0:
    # print("fork 调用失败")
# elif pid == 0:
    # print("我是子进程(%s), 我的父进程是(%s)" %(os.getpid(), os.getppid()))
# elif pid > 0:
    # print("我是父进程(%s), 我的子进程是(%s)" %(os.getpid(), pid))

def run_proc(name):
    print("子进程%s(%s)正在运行..." %(name, os.getpid()))
    time.sleep(1)

if __name__ == "__main__":
    print("父进程(%s)正在运行..." %(os.getpid()))
    child = Process(target=run_proc, args=('child1',))
    child.start()
    print("1.等待子进程结束")
    child.join()
    print("2.子进程结束")

    print("再来一次")
    time.sleep(1)
    child.start()
    print("2.等待子进程结束")
    child.join()
    print("3.子进程结束")
