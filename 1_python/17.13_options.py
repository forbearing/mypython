urls
    https://www.jianshu.com/p/820b74a2f113
    https://www.jianshu.com/p/0361cd8b8fec          (python命令行参数解析)
    https://www.jianshu.com/p/6f7078058023

Python 解析命令行
    getopt:     和C中的getopt()等价。
    optparse:   2.7后已不推荐使用。
    argparse:   基于optparse的新库。
    docopt:     根据文档描述，自动生成。另一份参考文档：docopt。


optparse
    介绍:
        * Python 有两个内建的模块用于处理命令行参数。一个是 getopt只能简单处理 命令行参数。
          另一个是 optparse，它功能强大而且易于使用，可以方便地生成标准的、符合 Unix/Posix
          规范的命令行说明。会自动帮你负责 -h 帮助选项

    参数含义
        dest
            用于保存输入的临时变量，其值通过 options 的属性进行访问，存储的内 容是 dest
            之前输入的参数，多个参数用逗号分隔
        type：用于检查命令行参数传入的参数的数据类型是否符合要求，有 string，int ，float 等类型
        help：用于生成帮助信息
        default：给 dest 的默认值，如果用户没有在命令行参数给 dest 分配值，则使用默认值
        metavar：
            设置 add_option 方法中的 metavar 参数，有助于提醒用户，该命令行参数所期待的参数，如 metavar=“mode”
        parse_args() 方法提供了一个 default 参数用于设置默认值
            parser.add_option("-v", action="store_true", dest="verbose")
            parser.add_option("-q", action="store_false", dest="verbose", default=true)
        parse_args() 返回的两个值
            * options，它是一个对象(optpars.Values)，保存有命令行参数值。只要知道命令行参数名，
              如 file，就可以访问其对应的值: options.file 。
            * args，它是一个由 positional arguments 组成的列表
            * action 是 parse_args() 方法的参数之一，它指示 optparse 当解析到一个命令行参数时
              该如何处理。actions 有一组固定的值可供选择，默认是’store ‘，表示将命令行参数值保存在
              options 对象里。
        otparse 另一个方便的功能是自动生成程序的帮助信息。你只需要为 add_opti on() 方法的 help 
            选项指定帮助信息文本

    代码
        from optparse import OptionParser

        parser = OptionParser()
        parser.add_option("-f", "--file", dest="filename", help="write report to file", metavar="FILE")
        parser.add_option("-u", "--user", dest="user", type="string", help="it is user")
        parser.add_option("-p", "--passwd", dest="passwd", help="it is password")

        (options, args) = parser.parse_args()
        print(options.filename)
        print(options.passwd)
        print(options.user)



