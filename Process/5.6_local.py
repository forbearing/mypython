#!/usr/bin/env python3

# import threading

# local_school = threading.local()

# def process_student():
    # std = local_school.student
    # print('Hello, %s (in %s)' %(std, threading.current_thread().name))

# def process_thread(name):
    # local_school.student = name
    # process_student()

# t1 = threading.Thread(target=process_thread, args=('Alice',), name="Thread-A")
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

import threading

global_val = threading.local()

def func(name):
    global_val.student = name
    local_val = global_val.student
    print("%s in %s" %(local_val, threading.current_thread().name))

t1 = threading.Thread(target=func, args=('hybfkuf',), name="thread-A")
t2 = threading.Thread(target=func, args=('jonas',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

1:全局变量 global_val 是一个 ThreadLocal 对象，每个 Thread 对它都可以读写 student 属性
  但互不影响。你可以把 global_val 看成一个全局变量，但每个属性，比如 global_val.student
  都是线程的局部变量。可以任意读写互不干扰。也不用管锁的问题。ThreadLocal 内部 会处理
2:可以 理解为全局变量 global_val 是一个 dict，不但可以用 global_val.student, 还可以绑定
  其他变量。比如 global_val.teacher 等等。
3:ThreadLocal 最常用的地方是为每个线程绑定一个数据库连接，HTTP 请求，用户身份信息等。
  这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
4:一个 ThreadLocal 变量虽然是全局变量。但每个线程只能读写自己线程的独立副本。互不干扰。
  ThreadLocal 解决了参数在一个线程中各个函数之间的互相传递的问题。
