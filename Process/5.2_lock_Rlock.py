#!/usr/bin/env python3
1:概述
    1:多线程面临的问题：保证线程安全、线程之间的同步、访问共享变量(内存)
    2:提供 Lock、Rlock、Semaphore、Event、Condition 用来保证线程之间的同步和访问
      共享变量的互斥问题。
    2:Lock & RLock：互斥锁，用来保证多线程访问共享变量的问题
    3:Semaphore对象：Lock互斥锁的加强版，可以被多个线程同时拥有，而Lock只能被某一个线程同时拥有。
    4:Event对象：它是线程间通信的方式，相当于信号，一个线程可以给另外一个线程发送信号后让其执行操作
    5:Condition对象：其可以在某些事件触发或者达到特定的条件后才处理数据
    6:对于Lock对象而言，如果一个线程连续两次release，使得线程死锁。所以Lock不常用，一般采用Rlock进行线程锁的设定
    7:RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。RLock使用了“拥有的线程”
      和“递归等级”的概念，处于锁定状态时，RLock被某个线程拥有。拥有RLock的线程可以再次调用
      acquire()，释放锁时需要调用release()相同次数。可以认为RLock包含一个锁定池和一个初始值为0
      的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态
      构造方法：mylock = Threading.RLock()
      实例方法：acquire([timeout])/release()

    import threading
    import time
    import random

    num = 0

    def run(lock):
        lock.acquire()
        global num
        time.sleep(random.random())
        num += 1
        time.sleep(random.random())
        print(num)
        lock.release()

    lock = threading.RLock()
    thread_list = []

    if __name__ == "__main__":
        for i in range(10):
            t = threading.Thread(target=run, args=(lock,))
            t.start()
            thread_list.append(t)
        for t in thread_list:
            t.join()

    # RLock 多次调用 acquire 和 release

