1:概述
    1:threading.Event可以使一个线程等待其他线程的通知。其内置了一个标志，初始值为 False
    2:线程通过wait()方法进入等待状态，直到另一个线程调用set()方法将内置标志设置为True 时
      Event通知所有等待状态的线程恢复运行
    3:调用clear()时重置为 False。还可以通过isSet()方法查询Envent对象内置状态的当前值。
    4:Event其实就是一个简化版的 Condition。Event没有锁，无法使线程进入同步阻塞状态
        isSet(): 当内置标志为True时返回True
        set(): 将标志设为True，并通知所有处于等待阻塞状态的线程恢复运行状态。
        clear(): 将标志设为False。
        wait([timeout]): 如果标志为True将立即返回，否则阻塞线程至等待阻塞状态，等待其他线程调用set()

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
