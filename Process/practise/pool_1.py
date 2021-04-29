#!/usr/bin/env python3

import time
import sys
from multiprocessing import Pool

def func(msg):
    print("in:", msg)
    time.sleep(3)
    print("out:",msg)

if __name__ == "__main__":
    pool = Pool(processes = 3)
    p_list = ["p1", "p2", "p3", "p4"]
    for p in p_list:
        msg = "I'm %s" %p
        pool.apply_async(func, (msg,))
    pool.close()
    pool.join()

