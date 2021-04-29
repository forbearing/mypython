#!/usr/bin/env python3

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
