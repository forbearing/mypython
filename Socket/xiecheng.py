import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' %n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("[PRODUCER] Producing %s..." % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' %r)
    c.close()


c = consumer()
produce(c)

1:首先调用 c.send(None) 启动生成器
2:然后，一旦生产了东西，通过 c.send(n) 切换到 consumer 执行
3:consumer 通过 yield 拿到消息，处理，又通过 yield 把结果传回
4:produce 拿到 consumer 处理的结果，继续生产下一条消息
5:produce 决定不生产了，通过 c.close() 关闭 consumer，整个过程结束。
