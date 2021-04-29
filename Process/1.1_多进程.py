1:fork
    1:在 Unix/Linux 操作系统中，提供了一个 fork() 函数，它非常特殊
    1:普通的函数调用一次，返回一次，但是 fork() 调用一次，返回两次，因为操作系统自动把当前
      进程（父进程）复制了一份（子进程），然后分别在父进程和子进程内返回
    2:子进程永远返回0，父进程返回子进程的进程 ID
    3:一个父进程可以 fork 出很多子进程，所以父进程要记下每个子进程的 ID，而子进程只需要调用
      getpid() 就可以拿到父进程的 ID
    4:父进程、子进程执行顺序没有规律，完全取决于操作系统的调度算法
        import os
        pid = os.fork()
        if pid < 0:
            print("fork 调用失败")
        elif pid == 0:
            print("我是子进程(%s)，我的父进程为(%s)"%(os.getpid(),osgetppid()))
        else:
            print("我是父进程(%s)，我的子进程为(%s)"%(os.getpid(),pid))
        print("父子进程都执行的代码")
        =================================================================================
        import os
        pid = fork()
        if(pid < 0):
            print("fork error")
        elif pid != 0:
             print("我是父进程(%s), 我的子进程为(%s)"%(os.getpid(), pid))
        else:
             print("我是子进程(%s), 我的父进程为(%s)"%(os.getpid(), os.getppid()))
        =================================================================================
    1:由于 Python 时跨平台的，自然也应该提供一个跨平台的多进程支持
    2:multiprocessing 模块就是跨平台的多进程模块
    3:multiprocessing 模块提供了一个 Process 类来代表一个进程对象
        from multiprocessing import Process
        import os
        def run_proc(name):
            print("子进程运行中, name=%s, pid=%d"%(name,os.getpid()))
        if __name__ == '__main__':
            print("父进程 %d" %s(os.getpid()))
            p = Process(target=run_process, args=('test',))
            print("子进程将要执行")
            p.start()
            p.join()
            print("子进程已结束")
            p.start()
            p.join()
            print("子进程结束")



