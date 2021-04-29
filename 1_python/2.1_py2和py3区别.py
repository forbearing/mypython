1:性能：
    py3.x 比 py2.x 效率低，但是 py3.x 有极大的优化空间，效率正在追赶

2:编码
    py3.x 源码文件默认使用 utf-8 编码，是的变量名更为广阔

3:语法
    1:去除了 <> 改用 !=
    2:加入了 as 和 with 关键字，还有 True，False，None
    3:整型触发返回浮点数，整数请使用 //
    4:加入 nonlocal 语句
    5:去除了 print 语句，加入 print() 函数
    6:去除了 raw_input，加入了 input() 函数
    7:新的 super()，可以不再给 super() 传参数
    8:改变了顺序操作符的行为，例如 x<y，当x和y类型不匹配时抛出 TypeError 而
      不返回随机的 bool 值
    9:新式的八进制字变量
        0o654   八进制
        0x655   十六进制
    10:字符和字符串
        python2 中: 8-bit 存储
        python3 中: 字符串以 16-bit  Unicode 字符串存储,现在字符串只有 str 一种类型
    11:整数类型
        1:python3.x 去除了 long 类型,现在只有一种整型 int, 但它的行为就像 2.x 版本的 long
        2:新增了 bytes 类型, 对应于2.x版本的八位串
            str 和 bytes 对象可以使用 str.encode()(str -> bytes)
            str.decode() (bytes->str) 方法相互转化
    12:面向对象
        引入了基类
    13:异常
        所有的异常都从 BaseException 继承,并删除了 StandardError
        python2
            try:
                pass
            except Exception, e:
                pass
        python3
            try:
                pass
            except Exception as e:
                pass
    14:其他:
        xrange() 改名为 range(), 要想使用 range() 获得一个 list, 必须显式调用
        file 类被废弃
            python2 打开文件
                file(path)
                open(path)
            python3 打开文件
                open(path)
