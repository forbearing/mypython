#!/usr/bin/env python3

import signal
import sys
import time


#signal.SIGINT           # 键盘 Ctrl-C 发出的信号
#signal.SIGHUP           # nohup 守护进程发出的关闭信号
#signal.SIGKILL          # kill 命令发出的信号


#===
# def handler_SIGINT(signum, frame):
    # print("capture SIGINT signal, exit ...")
    # time.sleep(1)
    # sys.exit()

# signal.signal(signal.SIGINT, handler_SIGINT)

# while True:
    # time.sleep(1)


#===
def my_handler(signum, frame):
    if signum == signal.SIGINT:
        print("Capture signal SIGINT, exit ...")
        sys.exit()
    elif signum == signal.SIGHUP:
        print("Capture signal SIGHUP, exit ...")
        sys.exit()
    # elif signum == signal.SIGTERM:
        # print("Capture signal SIGTERM, exit ...")
        # sys.exit()
    elif signum == signal.SIGKILL:
        print("Capture siggnal SIGKILL, exit ...")
        sys.exit()

#for sig in [signal.SIGINT, signal.SIGHUP, signal.SIGTERM, signal.SIGKILL]:
for sig in [signal.SIGINT, signal.SIGHUP, signal.SIGKILL]:
    signal.signal(sig, my_handler)

while True:
    time.sleep(1)
