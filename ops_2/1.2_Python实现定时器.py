#!/usr/bin/env python3

# 定义一个全局变量 t 用来实现 threading 模块的时间间隔，
# 如果不实用 global 关键字的话会造成线程堆积最终程序退出。
import threading
def sayhello():
    print("hello world")
    #global t
    t = threading.Timer(2.0, sayhello)
    t.start()

sayhello()



#==============================================================================================
一: 概述
    * Python 的 apscheduler 提供了非常丰富且方便易用的定时任务接口。apscheduler 使用起来十分方便。
      提供了基于日期、固定时间间隔以及 crontab 类型的任务，我们可以在主程序的运行过程中快速增加新作业
      或删除旧作业，如果把作业存储在数据库中，那么作业的状态会被保存，当调度器重启时，不必重新添加
      作业，作业会恢复愿状态继续执行。
    * apscheduler 可以当作一个跨平台的调度工具来使用。可以作为 Linux 系统 crontab 工具或 windows
      计划任务程序的替换。
    * 它主要是要在现有的应用程序中运行，也就是说，apscheduler 为我们提供了构建专门调度器或调度服务的基础模块
    * pip install apscheduler

二：基本概念介绍
    触发器 (triggers)
        触发器包含调度逻辑，描述一个任务何时被触发，按日期或按时间间隔或按 cronjob 表达式
        三种方式触发。每个作业都有它自己的触发器，除了初始配置之外，触发器是完全无状态的。
    作业存储器 (job stores)
        作业存储器制定了作业被存放的位置，默认情况下作业保存在内存，也可将作业保存在各种数据库中，
        当作业被存在数据库中时，它会被序列化，当被重新加载时会被反序列化。作业存储器充当保存、
        加载、更新和查找作业的中间商。分配器无法共享作业存储。
    执行器 (executors)
        执行器是将指定的作业（调用函数）提交到线程池或进程池中运行，当任务完成时，执行器
        通知调度器触发相应的事件
    调度器 (schedulers)
        任务调度器，属于控制角色，通过它配置作业存储器、执行器和触发器，添加、修改和删除任务。
        调度器协调触发器、作业存储器、执行器的运行，通常只有一个调度程序运行在应用程序中，
        开发人员通常不需要直接处理作业存储器、执行器或触发器，配置作业存储器和执行器是通过
        调度器来完成的。

三：基础概念详解
    * 触发器包含调度逻辑。每个作业都有它自己的触发器，这些触发器可以决定下一次应该什么时候运行作业。
      当然除了初始的配置之外，触发器是完全无状态的。
    * 每一个都存储预定的工作。默认的作业只是简单的讲作业保存在内存中。
    * 而其他的作业则是将它们存储在各种各样的数据库中，作业的数据保存在数据库的时候进行序列话，
      当需要将其加载回来的时候会进行反序列化。
    * 默认存储除外不会将作业数据保存在内存中，而是作为中间商在后台进行数据的保存、加载、更新和搜索
      操作。作业存储永远不会在调度器之间数据共享
    * 调度器和其他的部分是绑定在一起的。在你的应用程序中通常只有一个调度程序在运行。
    * 应用程序开发人员通常不直接处理作业存储器、执行器、触发器，相反，调度器提供适当的接口来处理
      所有这些问题。配置作业存储和执行器是通过调度器完成的，同时添加、修改和删除作业也是调度器来实现的。




#==============================================================================================
一：间隔性任务
    * 需要设置好时区 timedatectl set-timezone Asia/Dubai
    * 导入调度器模块 BlockingScheduler, 这是最简单的调度器，调用 start 方法阻塞当前进程，
      如果你的程序只用于调度，除了调度进程外没有其他后台进程，那么请用 BlockingScheduler
      非常有用，此时调度器进程相当于守护进程。
    * 定义一个 tick 代表我们要调度的作业程序
    * 实例化 blockingScheduler 类，不带参数表明使用默认的作业存储器，最大的默认并发线程为10个
    * scheduler.add_job 用于添加一个作业 tick，触发器威 interval，每隔3秒执行一次。另外的两个
      触发器分别为 date、cron。date 按特定时间点触发，cron 则按固定的时间间隔触发。

    from datetime import datetime
    from apscheduler.schedulers.blocking import BlockingScheduler

    def tick():
        print('现在的时间是：%s' %datetime.now())

    if __name__ == '__main__':
        scheduler = BlockingScheduler()
        scheduler.add_job(tick, 'interval', seconds=3)      # 间隔三秒执行
        try:
            scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass

二：cron 任务
    * hour=11, minute=33 表示每天的 11:33 分执行任务。这里可以填写数字，也可以填写字符串
    * minute='*/5' 每隔5分钟执行一次
    * hour='19-21', minute='23' 表示 19:23 20:23 21:23 各执行一次任务

    from datetime import datetime
    from apscheduler.schedulers.blocking import BlockingScheduler

    def tick():
        print("目前的时间是：%s" %datetime.now())

    if __name__ == '__main__':
        scheduler = BlockingScheduler()
        scheduler.add_job(tick, 'cron', hour=11, minute=33)
        try:
            scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass

三：调度器、存储器、触发器、执行器
    * 使用哪一种调度程序主要取决于你的编程环境以及你使用 APScheduler
        BlockingScheduler：适用于调度程序是进程中唯一运行的进程，调用 start 函数会阻塞当前线程，不能立即返回。
        BackgroundScheduler：适用于调度程序在应用程序的后台运行，调用 start 后主线程不会阻塞。
        AsyncIOScheduler：适用于使用了 asyncio 模块的应用程序。
        GeventScheduler：适用于使用 gevent 模块的应用程序。
        TwistedScheduler：适用于构建 twisted 的应用程序。
        QtScheduler：适用于构建 Qt 的应用程序。
    * 要选择合适的作业存储器，首先你需要确定是否需要作业持久性。如果你总是在应用程序开始时重新创建作业，
      那么你可以使用默认设置 MemoryJobStore。如果需要在调度器重启或应用程序崩溃期间保持作业，那么你的
      选择通常取决于你编程环境使用什么工具。如果可以自由选择，那么建议使用 PostgreSQL 数据库的
      SQLAIchemyJobStore 作为后端存储，因为它具有强大的数据完整性保护功能。
    * 默认的执行器 ThreadPoolExector 应该足以满足大多数目的。如果你的工作涉及到 CPU 密集型操作，那么应该
      考虑 ProcessPoolExector，而不是使用多个 CPU 内核。甚至可以同时使用它们，将 ProcessPoolExector
      作为次要执行器。
    * APScheduler 有三种内置的触发类型
        date        当你希望在某个时间点只运行一次作业的时候使用
        interval    当你希望以固定的时间间隔运行作业时候使用
        cron        当你希望在一天活特定时间段内定期执行作业的时候使用
    * 参考
        https://apscheduler.readthedocs.io/en/stable/modules/triggers/combining.html#module-apscheduler.triggers.combining

四：配置 Scheduler
    * APScheduler提供了许多不同的方法来配置调度器(scheduler)。您可以使用配置字典，也可以将
      选项作为关键字参数传入。还可以先实例化调度器(scheduler)，然后添加作业和配置调度器。
      通过这种方式，您可以为任何环境获得最大的灵活性
    * 调度器子类还可能有其他选项，这些选项被记录在它们各自的API引用中。个别作业存储(job stores)
      和执行器(executors)的配置选项也可以在它们的API参考⻚面中找到。
    * 假设你想在你的应用程序后台运行调度器，并且使用默认的作业存储（job store）和默认的
      执行器(executor)的话，实现的代码如下:
          from apscheduler.schedulers.background import BackgroundScheduler
          scheduler = BackgroundScheduler()
          # 使用默认的存储器 MemoryJobStore，还有默认的 ThreadPoolExector，默认最大的线程数为10

    * 现在，假设你的需求变了。您希望使用两个执行器(executor)拥有两个作业存储(job stores)，
      并更改默认的时区，下面三个例子是完全相同的。

    # code1: -----------------------------------------------------------------------
    # pip3 install PyMongo
    # pip3 install SQLAlchemy
    from pytz import utc
    from apscheduler.schedulers.background import BackgroundScheduler
    from apscheduler.jobstores.mongodb import MongoDBJobStore
    from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
    from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

    jobstores = {
            'mongodb': MongoDBJobStore(),
            'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
            }

    executors = {
            'default': ThreadPoolExecutor(20),
            'processpool': ProcessPoolExector(5)
            }
    job_defaults = {
            'coalesce': False,
            'max_instances': 3
            }

    scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)

    # code2: ----------------------------------------------------------------------
    from pytz import utc
    from apscheduler.schedulers.background import BackgroundScheduler

    scheduler = BackgroundScheduler({
            'apscheduler.jobstores.mongo': {
                    'type': 'mongodb'
                    }
            'apscheduler.jobstores.default': {
                    'type': 'sqlalchemy',
                    'url': 'sqlite:///jobs.sqlite'
                    },
            'apscheduler.exectors.default': {
                    'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
                    'max_workers': '20'
                    },
            'apscheduler.executors.processpool': {
                    'type': 'processpool',
                    'max_workers': '5'
                    },
            'apscheduler.job_defaults.coalesce': 'false',
            'apscheduler.job_defaults.max_instances': '3',
            'apscheduler.timezone': 'UTC',
            }),

    # code3: ----------------------------------------------------------------------
    from pytz import utc
    from apscheduler.schedulers.background import BackgroundScheduler
    from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
    from apscheduler.executors.pool import ProcessPoolExecutor

    jobstores = {
            'mongo': {'type': 'mongodb'},
            'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
            }
    executors = {
            'default': {'type': 'threadpool', 'max_workers': 20},
            'processpool': ProcessPoolExecutor(max_workers=5)
            }
    job_defaults = {
            'coalesce': False,
            'max_instances': 3
            }

    scheduler = BackgroundScheduler()
    scheduler.configure(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)


五：启动调度器
    * 启动调度器只需调用 start() 即可。除了 BlockingScheduler，非阻塞调度器都会立即返回，
      可以继续运行之后的代码，比如添加任务等。
    * 对于 BlockingScheduler，程序则会阻塞在 start() 位置，所以，要运行的代码必须写在 start() 之前
    * 调度器启动后，就不能修改配置。


六：添加任务
    * 添加任务的方法有两种
        通过调用 add_job()
        通过装饰器 scheduled_job()
    * 第一种方法是最常用的，第二种方法最方便，但缺点就是运行时、不能修改任务。第一种 add_job()
      返回返回一个 apscheduler.job.Job 实例，这样就可以在运行时，修改或删除任务
    * 在任何时候你都能配置任务。但是如果调度器还没有启动，此时添加任务，那么任务就处于一个暂停
      状态。只有当调度器启动时，才会开始计算下次运行时间。
    * 还有一点必须注意，如果你的执行器或任务存储器是会序列化任务的，那么这些任务就必须服务：
        回调函数必须全局可用
        回调函数参数必须也是可以被序列化的
    * 内置任务存储器中，只有 MemoryJobStore 不会序列化，内置执行器中，只有 ProcessPoolExector 会序列化
    * 重要提醒：
        如果在程序初始化时，是从数据库读取任务的，那么必须为每个任务定义一 个明确的ID，并且使用
        replace_existing=True，否则每次重启程序，你都会得到一份新的任务拷⻉，也就意味着任务的状态不会保存。
    * 建议
        如果想要立刻运行任务，可以在添加任务时省略 trigger 参数


七：获取任务列表
    * 通过 get_jobs() 就可以获得一个可修改的任务列表。 get_jobs() 第二个参数可以 指定任务储存器名称，
      那么就会获得对应任务储存器的任务列表。
    * print_jobs() 可以快速打印格式化的任务列表，包含触发器，下次运行时间等信息

八：关闭调度器
    * scheduler.shutdown()
    * 默认情况下，调度器会先把正在执行的任务处理完，再关闭任务储存器和执行器。但是如果你
      就直接关闭，你可以添加参数:
         scheduler.shutdown(wait=False)


