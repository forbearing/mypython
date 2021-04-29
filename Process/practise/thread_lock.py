#!/usr/bin/env python3

import threading
import time
import random

# num = 0

# def run(lock):
    # lock.acquire()
    # global num
    # time.sleep(random.random())
    # num += 1
    # time.sleep(random.random())
    # print(num)
    # lock.release()

# lock = threading.RLock()
# thread_list = []

# if __name__ == "__main__":
    # for i in range(10):
        # t = threading.Thread(target=run, args=(lock,))
        # t.start()
        # thread_list.append(t)
    # for t in thread_list:
        # t.join()

class myThread(threading.Thread):
    def run(self):
        global num
        timee.sleep(1)
