#!/usr/bin/env python3

# from multiprocessing import Queue, Process
# import os,time,random

# def write(q):
    # print("%s is writing" % os.getpid())
    # for value in ['A', 'B', 'C']:
        # q.put(value)
        # time.sleep(random.random()*5)

# def read(q):
    # print("%s is reading" %os.getpid())
    # while True:
        # value = q.get(True)
        # print("value is %s" % value)


# if __name__ == "__main__":
    # q = Queue()
    # pw = Process(target=write, args=(q,))
    # pr = Process(target=read, args=(q,))
    # pw.start()
    # pr.start()
    # pw.join()
    # pr.terminate()

# import threading
# import time

# def loop():
    # print("Thread %s is running" % threading.current_thread().name)
    # n = 0
    # while n < 5:
        # n = n + 1
        # print("Thread %s >>> %s" %(threading.current_thread().name, n))
        # time.sleep(1)
    # print("Thread %s is end" % threading.current_thread().name)

# print("Main Thread %s is running..." % threading.current_thread().name)
# t = threading.Thread(target=loop, name="LoopThread")
# t.start()
# t.join()
# print("Main Thread %s is end" % threading.current_thread().name)

# import threading
# lock = threading.Lock()
# balance = 0
# def change_it(n):
    # global balance
    # lock.acquire()
    # balance = balance + n
    # balance = balance - n
    # lock.release()

# def run_func(n):
    # for i in range(1000000):
        # change_it(n)

# t1 = threading.Thread(target=run_func, args=(5,))
# t2 = threading.Thread(target=run_func, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)


import threading
local_thread = threading.local()

def run_func(name):
    local_thread.student = name
    std = local_thread.student
    print("%s in %s" %(std, threading.current_thread().name))

t1 = threading.Thread(target=run_func, args=('hybfkuf',), name="Thread-hybfkuf")
t2 = threading.Thread(target=run_func, args=('jonas',), name="Thread-jonas")
t1.start()
t2.start()
t1.join()
t2.join()
