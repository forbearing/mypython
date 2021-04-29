#!/usr/bin/env python3

import multiprocessing
import random
import time
import os

# import multiprocessing
# import random
# import time
# import os

# def inputQ(queue):
    # info = str(os.getpid()) + '(put):' + str(time.time())
    # queue.put(info)

# def outputQ(queue, lock):
    # info = queue.get()
    # lock.acquire()
    # print(str(os.getpid()) + '(get):' + info)
    # lock.release()


# record_input = []
# record_output = []
# queue = multiprocessing.Queue(3)
# lock = multiprocessing.Lock()

# if __name__ == "__main__":
    # for i in range(10):
        # process = multiprocessing.Process(target=inputQ, args=(queue,))
        # process.start()
        # record_input.append(process)

    # for i in range(10):
        # process = multiprocessing.Process(target=outputQ, args=(queue, lock))
        # process.start()
        # record_output.append(process)

    # for proc in record_input:
        # proc.join()

    # for proc in record_output:
        # proc.join()

# import multiprocessing
# import time
# import os
# import random

# def inputQ(queue):
    # info = str(os.getpid()) + str(time.time())
    # queue.put(info)

# def outputQ(queu, lock):
    # info = queue.get()
    # lock.acquire()
    # print(str(os.getpid()) + '(get):' + info)
    # lock.release

# record_input = []
# record_output = []
# lock = multiprocessing.Lock()
# queue = multiprocessing.Queue()

# if __name__ == "__main__":
    # for i in range(10):
        # process = multiprocessing.Process(target=inputQ, args=(queue,))
        # process.start()
        # record_input.append(process)
    # for i in range(10):
        # process = multiprocessing.Process(target=outputQ, args=(queue, lock))
        # process.start()
        # record_output.append(process)

    # for process  in record_input:
        # process.join()
    # for process in record_output:
        # process.join()

# import multiprocessing
# import os
# import time
# import random

# def input_Q(queue):
    # info = str(os.getpid) + str(time.time())
    # queue.put(info)

# def output_Q(queue, lock):
    # info = queue.get()
    # lock.acquire()
    # print(info)
    # lock.release()

# record_input = []
# record_output = []
# lock = multiprocessing.Lock()
# queue = multiprocessing.Queue()

# if __name__ == "__main__":
    # for i in range(10):
        # process = multiprocessing.Process(target=input_Q, args=(queue,))
        # process.start()
        # record_input.append(process)
    # for i in range(10):
        # process = multiprocessing.Process(target=output_Q, args=(queue,lock))
        # process.start()
        # record_output.append(process)

    # for input_ in reccord_input:
        # input_.join()
    # for output in record_output:
        # output.join()


def func(v, array):
    v.value = time.time()
    for i in range(len(array)):
        array[i] = i*10

if __name__ == "__main__":
    v = multiprocessing.Value('d', 1.0)
    array = multiprocessing.Array('i', range(5))
    process = multiprocessing.Process(target=func, args=(v, array))
    print("before handle: ")
    print("v: %s\tarray: %s" %(v.value, array[:]))
    process.start()
    process.join()
    print("after handle: ")
    print("v: %s\tarray: %s" %(v.value, array[:]))
