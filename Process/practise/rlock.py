#!/usr/bin/env python3

import threading

mylocck = threading.Rlock()
num = 0

class WorkThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name
    def run(self):
        global num
        while True:
            mylock.acquire()
            print('\n%s locked, number: %d' %(self.t_name, num))
            if num >=2:
                mylock.relese()
                print('\n%s released, number: %d' %(self.t_name, num))
                break
            num += 1
            print('\n%s released, number: %d' % (self.t_name, num))
            mylock = release()
def test():
    thread1 = WorkThread('A-Worker')
    thread2 = WorkThread('B-Worker')
    thread1.start()
    thread2.start()

if __name__ == '__main__':
    test()
