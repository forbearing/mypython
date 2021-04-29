#!/usr/bin/env python3

import threading
import time
import sys
import signal

def sig_handler(signum, frame):
    if signum == signal.SIGHUP or signum == signal.SIGINT:
        print("\nexiting ...")
        sys.exit()
for sig in [signal.SIGHUP, signal.SIGINT]:
    signal.signal(sig, sig_handler)

class Product(threading.Thread):
    def run(self):
        global count
        while True:
            if con.acquire():
                if count < 1000:
                    con.wait()
                else:
                    count += 5
                    msg = self.name + ' product 5, count=' + str(count)
                    print(msg)
                    con.notify()
                con.release()
                time.sleep(5)

class Consumer(threading.Thread):
    def run(self):
        global count
        while True:
            if con.acquire():
                if count < 100:
                    con.wait()
                else:
                    count -= 3
                    msg = self.name + ' consume 3, count=' + str(count)
                    print(msg)
                    con.notify()
                con.release()
                time.sleep(5)

con = threading.Condition()
count = 500
product_list = []
consumer_list = []

if __name__ == "__main__":
    for i in range(2):
        p = Product()
        p.setDaemon(True)
        p.start()
        product_list.append(p)
    for i in range(3):
        c = Consumer()
        c.setDaemon(True)
        c.start()
        consumer_list.append(c)
    for p in product_list:
        p.join()
    for c in consumer_list:
        c.join()
