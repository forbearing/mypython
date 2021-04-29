#!/usr/bin/env python3

import threading

def ontimer():
    print(threading.current_thread())

def main():
    timer = threading.Timer(2, ontimer)
    timer.start()
    print(threading.current_thread())
    timer.cancel()
    if timer.isAlive():
        print("Timer is still alive")
    if timer.finished:
        print("Timer is finished")

if __name__ == "__main__":
    main()
