#!/usr/bin/env python3

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接受结果的队列
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

# 把两个 Queue 都注册到网上，callable 参数关联了 Queue 对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

