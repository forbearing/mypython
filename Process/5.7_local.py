1:概述
    1:一半我们都会对多线程中的全局变量进行加锁，这种变量是共享变量，每个线程都可以
      读写变量，为了保护同步，都会进行加锁处理
    2:但是有些变量初始化以后，我们只想让他们在每个线程中一直存在，相当于一个线程内的
      共享变量，线程之间又是隔离的。python threading模块中就提供了这么一个类，叫做local
      local是一个小写字母开头的类，用于管理 thread-local（线程局部的）数据。对于同一个
      local，线程无法访问其他线程设置的属性；线程设置的属性不会被其他线程设置的同名属性替换。
    3:可以把local看成是一个“线程-属性字典”的字典，local封装了从自身使用线程作为 key
      检索对应的属性字典、再使用属性名作为key检索属性值的细节


    import threading

    # Threading.local对象
    localManager = threading.local()
    lock = threading.RLock()

    class MyThead(threading.Thread):
        def __init__(self, threadName, name):
            super(MyThead, self).__init__(name=threadName)
            self.__name = name

        def run(self):
            global localManager
            localManager.ThreadName = self.name
            localManager.Name = self.__name
            MyThead.ThreadPoc()
        # 线程处理函数
        @staticmethod
        def ThreadPoc():
            lock.acquire()
            try:
                print('Thread={id}'.format(id=localManager.ThreadName))
                print('Name={name}'.format(name=localManager.Name))
            finally:
                lock.release()

    if __name__ == '__main__':
        bb = {'Name': 'bb'}
        aa = {'Name': 'aa'}
        xx = (aa, bb)
        threads = [MyThead(threadName='id_{0}'.format(i), name=xx[i]['Name']) for i in range(len(xx))]
        for i in range(len(threads)):
            threads[i].start()
        for i in range(len(threads)):
            threads[i].join()

