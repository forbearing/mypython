#!/usr/bin/env python3

用 asyncio 提供的 @asyncio.coroutine 可以把一个 generator 标记为 coroutine 类型，
然后在 coroutine 内部用 yield from 调用另一个 coroutine 实现异步操作

---
    import asyncio

    @asyncio.coroutine
    def hello():
        print("Hello world!")
        # 异步调用 asyncio.sleep(1)
        r = yield from asyncio.sleep(1)
        print("Hello again!")

    # 获取 EventLoop
    loop = asyncio.get_event_loop()
    # 执行 coroutine
    loop.run_until_complete(hello())
    loop.close()

    1:@asyncio.coroutine 把一个 generator 标记为 coroutine 类型，然后，我们把这个
      coroutine 扔到 EventLoop 中执行。
    2:yield from 语法可以让我们方便的调用另一个 generator。由于 asyncio.sleep() 也是一个
      corotine，所以线程不会等待 asyncio.sleep()，而是直接中断并执行下一消息循环。
      当 asyncio.sleep() 返回时，县城就可以从 yield  from 拿到返回值(此处是 None)，
      然后接着执行下一语句
    3:把 asyncio.sleep(1) 看成一个耗时1秒的IO操作，在此期间，主线程并为等待，而是去执行
      EventLoop 中其他的 coroutine 了，因此实现了并发执行


---
    import asyncio
    import threading

    @asyncio.coroutine
    def hello():
        print("Hello Python! (%s)" %threading.currentThread())
        yield from asyncio.sleep(1)
        print("Hello Again! (%s)" %threading.currentThread())

    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    1:由打印的当前线程名可以看出，两个 coroutine 是由同一个线程并发执行的
    2:如果 asyncio.sleep() 换成真正的 IO 操作，则多个 coroutine 就可以由一个线程并发执行


---
    import asyncio

    @asyncio.coroutine
    def wget(host):
        print("wget %s ..." % host)
        connect = asyncio.open_connection(host, 80)
        reader, writer = yield from connect
        header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
        writer.write(header.encode('utf8'))
        yield from writer.drain()
        while True:
            line = yield from reader.readline()
            if line == b'\r\n':
                break
            print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        writer.close()

    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
