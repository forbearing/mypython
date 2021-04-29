https://blog.csdn.net/brucewong0516/article/details/85776194

1:概述
    1:multiprocessing类似于threading模块支持生成进程的包，是Python的标准模块，它既可以
      用来编写多进程，也可以用来编写多线程。如果是多线程的话，用 multiprocessing.dummy
      即可，用法与 multiprocessing 基本相同
    2:由于python使用全局解释器锁(GIL)，他会将进程中的线程序列化，也就是多核cpu实际上并
      不能达到并行提高速度的目的，而使用多进程则是不受限的，所以实际应用中都是推荐多进程的
    3:如果每个子进程执行需要消耗的时间非常短（执行+1操作等），这不必使用多进程，
      因为进程的启动关闭也会耗费资源
    4:当然使用多进程往往是用来处理CPU密集型（科学计算）的需求，如果是IO密集型
      （文件读取，爬虫等）则可以使用多线程去处理。
    5:在UNIX平台上，当某个进程终结之后，该进程需要被其父进程调用wait，否则进程成为僵尸
      进程(Zombie)。所以，有必要对每个Process对象调用join()方法 (实际上等同于wait)。
      对于多线程来说，由于只有一个进程，所以不存在此必要性
    6:multiprocessing提供了threading包中没有的IPC(比如Pipe和Queue)，效率上更高。应优先
      考虑Pipe和Queue，避免使用Lock/Event/Semaphore/Condition等同步方式 (因为它们占据的
      不是用户进程的资源)
    7:多进程应该避免共享资源。在多线程中，我们可以比较容易地共享资源，比如使用全局变量
      或者传递参数。在多进程情况下，由于每个进程有自己独立的内存空间，以上方法并不合适。
      此时我们可以通过共享内存和Manager的方法来共享资源。但这样做提高了程序的复杂度，
      并因为同步的需要而降低了程序的效率。

2:multiprocessing 常用组建及功能
    1:管理进程模块
        Process         用于创建进程模块
        Pool            用于创建管理进程池
        Queue           用于进程通信，资源共享
        Value，Array    用于进程通信，资源共享
        Pipe            用于管道通信
        Manager         用于资源共享
    2:同步子进程模块
        Condition
        Event
        Lock
        RLock
        Semaphore

=== Process 类
    class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
    run()
        表示进程运行的方法。可以在子类中重写此方法。标准run() 方法调用传递给对象构造函数
        的可调用对象作为目标参数（如果有），分别使用args和kwargs参数中的顺序和关键字参数
    start()
        进程准备就绪，等待CPU调度
    join(timeout)
        如果可选参数timeout是None，则该方法将阻塞，直到join()调用其方法的进程终止.
        如果timeout是一个正数，它最多会阻塞超时秒
    name
        进程的名称。该名称是一个字符串，仅用于识别目的
    is_active()
        返回进程是否存活。从start() 方法返回到子进程终止的那一刻，进程对象仍处于活动状态。
    daemon
        进程的守护进程标志，一个布尔值。必须在start()调用之前设置，当进程退出时，它会
        尝试终止其所有守护进程子进程
    pid
        返回进程ID。在产生该过程之前，这将是 None。
    exitcode
        子进程的退出代码。None如果流程尚未终止，这将是。负值-N表示孩子被信号N终止。

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
