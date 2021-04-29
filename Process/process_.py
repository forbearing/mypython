#!/usr/bin/env python3

#!/usr/bin/env python3

# from multiprocessing import Process
# import os

# def run_func(name):
    # print("Run child process %s (%s)" %(name, os.getpid()))

# if __name__ == '__main__':
    # print("Parent process %s" % os.getpid())
    # p = Process(target=run_func, args=('hello',))
    # print('Child process will start.')
    # p.start()
    # p.join()
    # print('Child process end.')

# from multiprocessing import Process
# import os

# def run_func(name):
    # print("I'm child %s (%s), my parent is %s" %(name, os.getpid(),os.getppid()))

# if __name__ == '__main__':
    # print("I'm parent %s" % os.getpid())
    # p = Process(target=run_func, args=('hybfkuf',))
    # print('child is running.')
    # p.start()
    # p.join()
    # print('child is end.')

from multiprocessing import Process
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    start = time.time()
    time.sleep(random.random() * 6)
    end = time.time()
    print('Task %s (%s) is running, spend time %0.2f'
            %(name, os.getpid(),(end-start)))

if __name__ == '__main__':
    print("Parent process %s." % os.getpid())
    p = Pool(4)
    for i in range(6):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done ...')
    p.close()
    p.join()
    print('All subprocesses done.')
