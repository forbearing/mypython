#!/usr/bin/env python3
=== 概述
1:多线程
    1:线程是操作系统直接操作的执行单元，高级语言通常都内置多线程的支持
    2:Python 的线程是真正的 Posix Thread，而不是模拟出来的线程
    3:Python 的标准库提供了两个模块，_thread 和 threadingg, _thread 是低级模块，
      threadingg 是高级模块，对 _thread 进行了封装。绝大多数情况下只需要使用 threading
      高级模块。
2:threading
    1:threading 的 current_thread 函数返回当前线程的实例
    2:主线程的名字为 MainThread，子线程的名字在创建时指定，此次使用了 LoopThread
    3:子线程名字仅用于打印，没有其他意义。不起名字，默认为 Thread-1, Thread-2
lock
    - 同一变量，各自拷贝一份在每个进程中，互不影响。而在多线程中，所有变量都由所有线程
      共享，所以，任何一个变量都可以被任何一个线程修改

    join 有一个 timeout 参数
        1:当设置守护线程时(setDaemon(True))，主线程对于子线程等待 timeout 的时间会杀死
          该子线程，最后退出程序。如果有多个子线程，全部的等待时间为每个 timeout 
          的时间总和，时间一到，不管任务是否完成，直接杀死。
        2:如果为线程实例添加 t.setDaemon(True) 守护进程之后，如果不加 join 语句，那么当
          主线程结束之后，会杀死子线程。如果加上 join 并设置等待时间，就会等待线程一段
          时间就再退出。


import time, threading
def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s >>> %s" %(threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s end" % threading.current_thread().name)

print("main thread %s is running" % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('main thread %s is end' % threading.current_thread().name)



#多个线程同时操作一个变量
import threading,time
balance = 0
def change_it(n):
    # 先存后取，结果不变
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(1000000):
        change_it(n)
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)



# 加锁
# - 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为
# - 死线程。所以使用 try finally 来 确保锁一定会被释放
lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it()
        finally:
            lock.release()
