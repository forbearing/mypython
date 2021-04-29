1:概述
    1:在使用多线程的应用下，如何保证线程安全，以及线程之间的同步，或者访问共享变量等问题
      是十分棘手的问题，也是使用多线程下面临的问题，如果处理不好，会带来较严重的后果，
      使用python多线程中提供Lock 、Rlock 、Semaphore 、Event 、Condition 用来保证线程之间
      的同步，后者保证访问共享变量的互斥问题
    2:Lock & RLock: 互斥锁，用来保证多线程访问共享变量的问题
    3:Semaphore 对象：Lock互斥锁的加强版，可以被多个线程同时拥有，而Lock
      只能被某一个线程同时拥有。
    4:Event 对象：它是线程间通信的方式，相当于信号，一个线程可以给另外一个线程发送信号
      后让其执行操作。
    5:Condition 对象：其可以在某些事件触发或者达到特定的条件后才处理数据

2:Lock
    1:请求锁定 — 进入锁定池等待 — — 获取锁 — 已锁定— — 释放锁
    2:Lock（指令锁）是可用的最低级的同步指令。Lock处于锁定状态时，不被特定的线程拥有。
      Lock 包含两种状态——锁定和非锁定，以及两个基本的方法
    3:可以认为 Lock 有一个锁定池，当线程请求锁定时，将线程至于池中，直到获得锁定后出池。
      池中的线程处于状态图中的同步阻塞状态
      lock.acquire
      lock.timeout
    4:对于Lock对象而言，如果一个线程连续两次release，使得线程死锁。所以Lock不常用，
      一般采用Rlock进行线程锁的设定
    5:RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。RLock 使用了“拥有的线程”
      和“递归等级”的概念，处于锁定状态时，RLock 被某个线程拥有。拥有 RLock 的线程可以
      再次调用 acquire()，释放锁时需要调用 release() 相同次数。可以认为RLock包含一个
      锁定池和一个初始值为0的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，
      为0时锁处于未锁定状态

    ===
    import threading
    import  time

    num = 0
    lock = threading.Rlock()

    def show(arg):
        lock.acquire()
        global num
        time.sleep(1)
        print(num)
        lock.release()
    for i in range(10)
        t = threading.Thread(target=Func)
        t.start()

    ===
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
