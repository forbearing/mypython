#!/usr/bin/env python3

from multiprocessing import Process
import time
import os

def info():
    print('module name:', __name__)
    print("parent proccess:", os.getppid())
    print('process id:', os.getpid())

def f(name):
    info()
    time.sleep(3)
    print("hello", name)


if __name__ == "__main__":
    p = Process(target=f, args=('hybfkuf',))
    # p.daemon = False
    p.daemon = True
    print(p.daemon)
    p.start()
    p.join()
    print('name:', p.name)
    print("is_active:", p.is_alive())
    print("exitcode:", p.exitcode)
