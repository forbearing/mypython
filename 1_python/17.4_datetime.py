时间
    UTC，世界协调时间：格林尼治天文时间，世界标准时间，在中国是  UTC+8
    DST，夏令时：是一种节约能源而认为规定时间制度

时间的表示形式
    时间戳: 
        以整形或浮点型表示时间的一个以秒为单位的时间间隔。这个时间间隔的基础值是从
        1970 年1月1日凌晨开始算起
    元组
        一种 Python 的数据结构表示，这个元组有9个整形内容
    格式化字符串

时间元组
    tm_yer      年
    tm_mon      月
    tm_mday     日
    tm_hour     时
    tm_min      分
    tm_sec      秒
    tm_wday     0-6,0是周一
    tm_yday     一年中的第几天, 1-366
    tm_isdst    是否为夏令时, 1(夏令时), 0(不是夏令时) -1(未知) 默认-1

格式化字符串
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身


1:time 模块
    time.time()                 # 返回当前时间戳

    time.gmtime()               # 将时间戳转换为 UTC 时间元组
    time.localtime()            # 将时间戳转换为本地时间元组
    time.localtime(time.time())

    time.mktime(time.gmtime())  # 本地时间元组转换成时间戳
    time.mktime(time.localtime())

    time.ctime()                # 时间戳转换成字符串
    time.ctime(time.time())
    time.asctime()              # 时间元组转换成字符串
    time.asctime(time.localtime())
    time.asctime(time.localtime(time.time()))

    time.strftime(format[, t])  
        # 将时间元组转换成给定格式的字符串，参数2为时间元组，如果没有参数2，
        #   默认当前时间, time.localtime()
    time.strftime("%Y-%m-%d %H:%M:%S")
    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    time.strftime('%Y-%m-%d', time.localtime())
        # strptime 第一个参数是字符串形式的日期，第二个参数是自定义的日期转换格式
        # strftime 第一个参数想要转化成的日期格式，第二个参数是一个 strcut_time,
        #   此函数将元组形式的 struct_time 转化成第一个参数指定的格式的样子
    time.strptime('2017/7/6', '%Y/%m/%d')
        # 将时间字符串转换成时间元组

    time.sleep(4)
    time.clock()
        # 返回当前程序的 cpu 执行时间，Unix 系统始终返回全部的运行时间,
        #   windows 第二次开始，都是以第一个调用此函数的开始时间戳作为基数
    time.perf_counter()
    time.process_time()

    import calendar
    cal = calendar.month(2016, 1)               # 获取日历

    ---
    import time
    time.process_time()
    sum = 0
    for i in range(1000000):
        sum += i
    print(time.process_time())

    ---
    import time
    time.perf_counter()
    sum = 0
    for i in range(1000000):
        sum += i
    print(time.perf_counter())



2:datetime 模块
    1:datetime 比 time 高级了很多，可以理解为 datetime 对 time 进行了封装，
    2:datetime 模块的接口更直观，更容易使用
    3:模块中的类：
        datetime    同时有时间和日期
        timedelta   主要用于计算时间的跨度
        tzinfo      时区相关
        time        只关注时间
        date        只关注日期

    d1 = datetime.datetime.now()            # 获取当前时间
    d2 = datetime.datetime(1999,10,1,10,28,25,123456)       # 获取指定时间
    print(d2)


    # datetime 用来管理日期和时间，其中有三个子模块，分别是 time, date, datetime,
    ---
    # datetime 接受7个参数，分别对应：年、月、日、时、分、秒、微秒，分别保存在
    #   datetime 的 year、month、day、hour、minute、second、microsecond 属性中
    from datetime import datetime
    now = datetime.now()
    print(now.year, now.month, now.day, now.hour, now.minute, now.second,
            now.microsecond)

    ---
    # datetime 对象可以使用比较运算符(<>>=!=)来比较两个日期的前后，也可以进行加减运算，
    #   表示两个时刻的差值
    from datetime import datetime
    dt1 = datetime(2017, 5, 31)
    dt2 = datetime(2017, 4, 1)
    dt3 = dt2 - dt1
    print(dt1 - dt2)
    print(dt1 > dt2)
    print(dt3.days, d3.seconds, d3.microseconds)

    ---
    # timedelta 表示一段时间,而不是一个时刻
    # timedelta的接受的参数有weeks、days、hours、minutes、seconds、microseconds，但是
    #   其属性却只有days、seconds、microseconds。并且除了像datetime一样支持大小比较、
    #   减法运算外，还可以进行加法运算，表示两个时间段的差值
    import datetime
    delta = datetime.timedelta(weeks=2, days=7, hours=1,
            seconds=59,microseconds=234353)
    delta1 = datetime.timedelta(days=5, hours=2)
    print(delta.seconds)  # 返回属性hours和seconds的和
    print(delta.total_seconds()) # 只是以秒来表示这段时间
    print(delta > delta1)
    print(delta + delta1)



3:日历模块
    import calendar
    print(calendar.month(2017,7))       # 返回指定某年某月的日历
    print(calendar.isleap(2018))        # 判断是否为闰年
    calendar.monthrange(2017,7)         # 返回某个月的weekday的第一天和这个月所有的天数
    calendar.monthcalendar(2017,7)      # 返回某个月以每一周为一个元素的列表
