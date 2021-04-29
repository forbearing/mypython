#!/usr/bin/env python3

# from multiprocessing import Process, Queue
# import os, time, random

# def write(q):
    # print("Process %s is writing" %os.getpid())
    # for value in ['A', 'B', 'C']:
        # q.put(value)
        # time.sleep(random.random())

# def read(q):
    # print("Process %s is reading" %os.getpid())
    # while True:
        # value = q.get(True)
        # print("Get Value %s" %value)

# if __name__ == "__main__":
    # q = Queue()
    # pw = Process(target=write, args=(q,))
    # pr = Process(target=read, args=(q,))
    # pw.start()
    # pr.start()
    # pw.join()
    # pr.join()

import queue
q = queue.Queue(5)
