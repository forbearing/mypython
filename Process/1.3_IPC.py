1:Pipe 概述
    1:Linux多线程的 IPC 有：管道PIPE和消息队列message queue，multiprocessing 包中有 Pipe
      类和 Queue 类来分别支持这两种IPC机制。Pipe 和 Queue 可以用来传送常见的对象。
    2:Pipe可以是单向(half-duplex)，也可以是双向(duplex)。我们通过 mutiprocessing.Pipe(duplex=False)
      创建单向管道 (默认为双向)。一个进程从PIPE一端输入对象，然后被PIPE另一端的进程接收，
      单向管道只允许管道一端的进程输入，而双向管道则允许从两端输入。
    3:Pipe对象建立的时候，返回一个含有两个元素的表，每个元素代表Pipe的一端(Connection对象)。
      我们对Pipe的某一端调用send()方法来传送对象，在另一端使用recv()来接收

    import multiprocessing

    def proc_1(pipe):
        pipe.send("send hello")
        print("proc_1 recv:", pipe.recv())

    def proc_2(pipe):
        print("proc_2 recv:", pipe.recv())
        pipe.send("send hello")

    pipe = multiprocessing.Pipe()
    if __name__ == "__main__":
        p1 = multiprocessing.Process(target=proc_1, args=(pipe[0],))
        p2 = multiprocessing.Process(target=proc_2, args=(pipe[1],))
        p1.start()
        p2.start()
        p1.join()
        p2.join()



2:Queue 概述
    Queue与Pipe相类似，都是先进先出的结构。但Queue允许多个进程放入，多个进程从队列取出对象。
    Queue使用mutiprocessing.Queue(maxsize)创建，maxsize表示队列中可以存放对象的最大数量。

    import multiprocessing
    import random
    import time
    import os

    def inputQ(queue):
        info = str(os.getpid()) + '(put):' + str(time.time())
        queue.put(info)

    def outputQ(queue, lock):
        info = queue.get()
        lock.acquire()
        print(str(os.getpid()) + '(get):' + info)
        lock.release()


    record_input = []
    record_output = []
    queue = multiprocessing.Queue(3)
    lock = multiprocessing.Lock()

    if __name__ == "__main__":
        for i in range(10):
            process = multiprocessing.Process(target=inputQ, args=(queue,))
            process.start()
            record_input.append(process)

        for i in range(10):
            process = multiprocessing.Process(target=outputQ, args=(queue, lock))
            process.start()
            record_output.append(process)

        for proc in record_input:
            proc.join()

        for proc in record_output:
            proc.join()
        queue.close()



3:共享内存
    def func(v, array):
        v.value = time.time()
        for i in range(len(array)):
            array[i] = i*10

    if __name__ == "__main__":
        v = multiprocessing.Value('d', 1.0)             # d,双精度，并初始化为1
        array = multiprocessing.Array('i', range(5))    # i,整数, 类似 C 中的数组
        process = multiprocessing.Process(target=func, args=(v, array))
        print("before handle: ")
        print("v: %s\tarray: %s" %(v.value, array[:]))
        process.start()
        process.join()
        print("after handle: ")
        print("v: %s\tarray: %s" %(v.value, array[:]))


4:Manager
    1:Manager是通过共享进程的方式共享数据。
    2:Manager管理的共享数据类型有：Value、Array、dict、list、Lock、Semaphore等等，
      同时Manager还可以共享类的实例对象。

    from multiprocessing import Process, Manager

    def func(shareList, shareValue, shareDict, lock):
        with lock:
            shareValue.value += 1
            shareDict[1] = '1'
            shareDict[2] = '2'
            for i in range(len(shareList)):
                shareList[i] += 1

    if __name__ == "__main__":
        manager = Manager()
        list1 = manager.list([1,2,3,4,5])
        dict1 = manager.dict()
        array1 = manager.Array('i', range(10))
        value1 = manager.Value('i', 1)
        lock = manager.Lock()
        proc = [Process(target=func, args=(list1, value1, dict1, lock)) for i in range(20)]
        for p in proc:
            p.start()
        for p in proc:
            p.join()
        print(list1)
        print(dict1)
        print(array1)
        print(value1)
