#!/usr/bin/env python3
#https://blog.csdn.net/liuchunming033/article/details/39080457
1:日志等级
    日志分为5个等级：DEBUG、INFO、WARNING、ERROR、CRITICAL


2:日志输出
    两种输出方式：输出控制台、记录到文件

    1:将日志输出到控制台
    import logging
    logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    logging.debug('logging debug message')
    logging.info("logging info message")
    logging.warning('logging warning message')
    logging.error('logging error message')
    logging.critical('logging critical messsage')

    2:将日志输出到文件
    logging.basicConfig(level=logging.WARNING,
                        filename='./log/log.txt',
                        filemode='w',
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    logging.debug('logging debug message')
    logging.info("logging info message")
    logging.warning('logging warning message')
    logging.error('logging error message')
    logging.critical('logging critical messsage')

    3:同时输出到控制台和日志文件
    import logging

    # 第一步，创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)    # Log等级总开关

    # 第二步，创建一个handler，用于写入日志文件
    logfile = './log/logger.txt'
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.DEBUG)   # 输出到file的log等级的开关

    # 第三步，再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)   # 输出到console的log等级的开关

    # 第四步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 第五步，将logger添加到handler里面
    logger.addHandler(fh)
    logger.addHandler(ch)

    # 日志
    logger.debug('this is a logger debug message')
    logger.info('this is a logger info message')
    logger.warning('this is a logger warning message')
    logger.error('this is a logger error message')
    logger.critical('this is a logger critical message')



3:多个模块中日志输出顺序
    vi util.py
        import logging
        def func():
            logging.info('this is a log in util module')

    vi main.py
        import logging
        import util
        logging.basicConfig(level=logging.INFO,
                            filename='./log/log.txt',
                            filemode='w',
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        def main():
            logging.info('main module start')
            util.func()
            logging.info('main module stop')
        if __name__ == "__main__":
            main()



4:日志格式说明
    %(levelno)s: 打印日志级别的数值
    %(levelname)s: 打印日志级别名称
    %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s: 打印当前执行程序名
    %(funcName)s: 打印日志的当前函数
    %(lineno)d: 打印日志的当前行号
    %(asctime)s: 打印日志的时间
    %(thread)d: 打印线程ID
    %(threadName)s: 打印线程名称
    %(process)d: 打印进程ID
    %(message)s: 打印日志信息
