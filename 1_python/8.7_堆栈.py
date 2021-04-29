1:栈
    # 先进后出
    li = []
    li.append('A')
    li.append('B')
    li.append('C')
    li.pop()
    print(li)

2:队列
    # 先进先出
    import collections
    queue = collections.deque()
    queue.append('A')
    queue.append('B')
    queue.append('C')
    print(queue)
    queue.pop()
    queue.popleft()
    print(queue)
