=== 概述
    1:元素进put(arg)，元素出get(arg)
    2:队列都是在内存中操作，进程退出，队列清空，队列也是一个阻塞的状态
=== 队列分类
    queue.Queue             先进先出队列
    queue.LifoQueue         后进先出队列
    queue.PriorityQueue     优先级队列
    queue.deque             双线队列
=== 队列方法
    put
        放数据，Queue.put() 默认有 block=True，和 timeout 两个参数。当 block=True 时，
        写入是阻塞的，阻塞时间由 timeout 确定。当队列 q 被其他线程写满后，这段代码就会
        阻塞，直到其他线程取走数据。Queue.put() 方法加上 block=False 的参数，即可解决
        这个隐蔽的问题。但是注意，当非阻塞方式写队列时，当队列满时会抛出 
        Exception  Queue Full 的异常
    get
        取数据（默认阻塞），Queue.get([block[, timeout]])获取队列，timeout等待时间
    empty           如果队列为空，返回 True，反之 False
    qsize           显示队列中真实存在的元素长度
    maxsize         最大支持的队列长度,使用时无括号
    join            等到队列为空，再执行别的操作
    task_done       在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
    full            如果队列满了，返回True,反之False




=== 单向队列
    import queue
    q = queue.Queue(5)          # 如果不设置长度，默认为无限长
    print(q.maxsize)
    q.put(10)
    q.put(20)
    q.put(30)
    q.put(40)
    q.put(50)
    q.put(60)                   # put 第6个时会阻塞
    print(q.get())              # get 第6个时会阻塞

=== 后进后出队列
    q = queue.LifoQueue()
    q.put(10)
    q.put(20)
    q.put(30)
    q.get()                     # 返回30，后进后出

=== 优先级队列
    q = queue.PriorityQueue()
    q.put(3, 'a')
    q.put(1, 'b')
    q.put(2, 'c')
    q.put(4, 'd')

=== 双线队列
    q = queue.deque()
    q.append(123)
    q.append(456)
    q.appendleft(780)
    print(q.pop())
    print(q.popleft())

