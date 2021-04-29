#!/usr/bin/env python3

import threading
import time

event = threading.Event()

def func():
    print("%s wait for event ..." % threading.current_thread().getName())
    event.wait()
    print("%s recv event." % threading.current_thread().getName())

if __name__ == "__main__":
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func)
    t1.start()
    t2.start()
    time.sleep(2)
    print("MainThread set event.")
    event.set()
