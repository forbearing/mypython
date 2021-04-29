1:概述
    1:Timer（定时器）是Thread的派生类，用于在指定时间后调用一个方法。Timer从Thread派生，没有增加实例方法
    2:Timer(interval, function, args=[ ], kwargs={ })
        interval:   指定时间
        function:   要执行的函数
    3:Timers通过调用它们的start()方法作为线程启动。timer可以通过调用cancel()方法
      （在它的动作开始之前）停止。timer在执行它的动作之前等待的时间间隔可能与用户指定
      的时间间隔不完全相同。
    4:cancel() 只会让 timer 不执行函数，并不会销毁 timer()

    ===
    # timer 在 t 时间后启动
    import threading

    def func(num):
        print("hello {} timer!".format(num))

    timer = threading.Timer(5, func, (1,))
    timer.start()
    timer.join()

    ===
    # cancel
    import threading

    def func(num):
        print("hello {} timer!".format(num))

    timer = threading.Timer(5, func, (1,))
    timer.start()
    timer.cancel()

    ===
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
