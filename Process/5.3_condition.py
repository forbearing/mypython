#!/usr/bin/env python3
1:概述
    1:Python提供的Condition对象提供了对复杂线程同步问题的支持
    2:Condition被称为条件变量，除了提供与Lock类似的acquire和release方法外，还提供了
      wait 和 notify 方法
    3:Condition 的处理流程
        1:首先acquire一个条件变量，然后判断一些条件
        2:如果条件不满足则wait
        3:如果条件满足，进行一些处理改变条件后，通过notify方法通知其他线程，
          其他处于wait状态的线程接到通知后会重新判断条件
        4:不断的重复这一过程，从而解决复杂的同步问题
    4:基本原理
        1:可以认为 Condition 对象维护了一个锁（Lock/RLock)和一个 waiting 池。线程通过 acquire
          获得 Condition 对象，当调用wait方法时，线程会释放 Condition 内部的锁并进入 blocked
          状态，同时在 waiting 池中记录这个线程。当调用 notify 方法时，Condition 对象会从
          waiting 池中挑选一个线程，通知其调用 acquire 方法尝试取到锁。
        2:Condition 对象的构造函数可以接受一个 Lock/RLock 对象作为参数，如果没有指定，
          则 Condition 对象会在内部自行创建一个 RLock
    5:除了 notify 方法外，Condition 对象还提供了 notifyAll 方法，可以通知 waiting 池中
      的所有线程尝试 acquire 内部锁。由于上述机制，处于 waiting 状态的线程只能通过
      notify 方法唤醒，所以 notifyAll 的作用在于防止有的线程永远处于沉默状态。

import threading
import time
import signal
import sys
import os

def sig_handler(signum, frame):
    if signum == signal.SIGHUP or signum == signal.SIGINT:
        print("exiting ...")
        os._exit()

for sig in [signal.SIGINT, signal.SIGHUP]:
    signal.signal(sig, sig_handler)


class Product(threading.Thread):
    # 生产者函数
    def run(self):
        global count
        while True:
            if con.acquire():
                # 当count 小于等于1000 的时候进行生产
                if count > 1000:
                    con.wait()
                else:
                    count = count + 5
                    msg = self.name + ' product 5, count=' + str(count)
                    print(msg)
                    # 完成后唤醒 waiting 状态的线程，
                    # 从 waiting 池中挑选一个线程，通知其调用 acquire 方法尝试取得锁
                    con.notify()
                con.release()
                time.sleep(5)

class Consumer(threading.Thread):
    # 消费者函数
    def run(self):
        global count
        while True:
            if con.acquire():
                if count < 100:
                    con.wait()
                else:
                    count = count - 3
                    msg = self.name + ' consume 3, count=' + str(count)
                    print(msg)
                    con.notify()
                    # 完成生成后唤醒 waiting 状态的线程
                    # 从waiting池中挑选一个线程，通知其调用 acquire 方法尝试取到锁
                con.release()
                time.sleep(5)

count = 500
con = threading.Condition()
product_list = []
consumer_list = []

def main():
    for i in range(2):
        p = Product()
        p.setDaemon(True)
        p.start()
        product_list.append(p)
    for i in range(4):
        c = Consumer()
        c.setDaemon(True)
        c.start()
        consumer_list.append(c)
    for p in  product_list:
        p.join()
    for c in consumer_list:
        c.join()

if __name__ == "__main__":
    main()

