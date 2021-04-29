#!/usr/bin/env python3

import os
import threading
import multiprocessing

def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    lock.release()

lock_thread = threading.Lock()
record_thread = []

lock_process = multiprocessing.Lock()
record_process = []


if __name__ == "__main__":
    for i in range(5):
        thread = threading.Thread(target=worker, args=('thread', lock_thread))
        thread.start()
        record_thread.append(thread)
    for thread in record_thread:
        thread.join()

    for i in range(5):
        process = multiprocessing.Process(target=worker, args=('process', lock_process))
        process.start()
        record_process.append(process)
    for process in record_process:
        process.join()
