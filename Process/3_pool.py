#!/usr/bin/env python3
=== 概述
    1:提供指订数量的进程供用户使用，如果池还没有满，就会创建一个新的进程来执行请求，
      如果池满，请求就会告知先等待，直到池中进程结束，才会创建新的进程来执行请求
    2:Pool 类用于需要执行的目标很多，而手动限制进程数量又太繁琐时，如果目标少且不用
      控制进程数量时可以用 Proccess 类


=== 
1:参数 pool = multiprocessing.Pool()
    processes
        要使用的工作进程数，如果不指定或者为 None，那么使用返回的数字os.cpu_count()，
        由本地 cpu 个数来决定。
    initializer
        如果initializer是None，那么每一个工作进程在开始的时候会调用initializer(*initargs)
    maxtasksperchild
        工作进程退出之前可以完成的任务数,完成后用一个新的工作进程来替代原进程,来让闲置
        的资源被释放. maxtasksperchild 默认是None，意味着只要Pool存在工作进程就会一直存活
    context
        指定工作进程启动时的上下文
2:方法
    apply(func, args=(), kwds={})
        该函数用于传递不定参数，主进程会被阻塞直到函数执行结束（不建议使用，并且3.x以后不在出现）
    apply_async(func[, args=()[, kwds={}[, callback=None]]])
        与apply用法一致，但它是非阻塞的且支持结果返回后进行回调
    map(func, iterable, chunksize=None)
        Pool类中的map方法，与内置的map函数用法基本一致，它会使进程阻塞直到结果返回
    map_async(func, iterable, chunksize, callback)
        与map用法一致，但是它是非阻塞的
    close()
        关闭进程池（pool），使其不在接受新的任务
    terminal()
        结束工作进程，不在处理未处理的任务
    join()
        主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用

===
    import time
    import sys
    from multiprocessing import Pool

    def func(msg):
        print("in:", msg)
        time.sleep(3)
        print("out:",msg)

    if __name__ == "__main__":
        pool = Pool(processes = 3)
        p_list = ["p1", "p2", "p3", "p4"]
        for p in p_list:
            msg = "I'm %s" %p
            pool.apply_async(func, (msg,))
        pool.close()
        pool.join()
