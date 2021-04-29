1:分类
    整数,浮点数,复数


2:整数
    1:概述
        1:Python 可以处理任何大小的整数,也包括负数,在程序中表示和数学的写法一样
    2:使用
        1:连续定义多个变量(可读性差,不建议使用过)
            num1 = num2 = num3 = 0
        2:交互式赋值变量
            num1, num2 = 6, 7


3:浮点数
    1:概述: 浮点型由整数部分和小数部分组成, 浮点数运算可能会有四舍五入的误差


4:复数
    1:概述: 实数部分和虚数部分组成 a+bj


5:数字类型转换
    print(int(1.0))         # 向下取整，不是四舍五入
    print(int(var))
    print(int("10"))        # 正确
    print(int("10.1"))      # 错误
    print(int(+123))        # 正确
    print(int(-123))        # 正确
    print(int("string"))    # 错误

    print(float(1))
    print(float(var))
    print(float("10"))      # 正确
    print(float("10.1"))    # 正确
    print(float("string"))  # 错误


6:相关函数
    1:类型转换
        int(x)
        float(y)
        complex(x)
        complex(x,y)
    2:数学运算
        abs(x)          返回数字的绝对值，如abs(-10) 返回 10
        ceil(x)         返回数字的上入整数，如math.ceil(4.1) 返回 5
        exp(x)          返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
        fabs(x)         返回数字的绝对值，如math.fabs(-10) 返回10.0
        floor(x)        返回数字的下舍整数，如math.floor(4.9)返回 4
        log(x)          如math.log(math.e)返回1.0,math.log(100,10)返回2.0
        log10(x)        返回以10为基数的x的对数，如math.log10(100)返回 2.0
        max(x,y)        返回给定参数的最大值，参数可以为序列。
        min(x,y)        返回给定参数的最小值，参数可以为序列。
        modf(x)         返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示
        pow(x,y)        x**y 运算后的值
        round(x [,n])   返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。
                        其实准确的说是保留值将保留到离上一位更近的一端
        sqrt(x)         返回数字x的平方根。
    3:随机函数
        choice(seq)     从序列的元素中随机挑选一个元素，比如random.choice(range(10))，
                        从0到9中随机挑选一个整数。
        randrange([start,] stop [,step])
                        从指定范围内，按指定基数递增的集合中获取一个随机数
                        包含开始值，不包含结束值
                        randrange(100)，开始值默认为0，基数默认为1
        random()        随机生成下一个实数，它在[0,1)范围内。
        seed([x])       改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去
                        设定seed，Python会帮你选择seed。
        shuffle(lst)    将序列的所有元素随机排序
        uniform(x,y)    随机生成下一个实数，它在[x,y]范围内。
    4:三角函数
        acos(x)         返回x的反余弦弧度值。
        asin(x)         返回x的反正弦弧度值。
        atan(x)         返回x的反正切弧度值。
        atan2(y,x)      返回给定的 X 及 Y 坐标值的反正切值。
        cos(x)          返回x的弧度的余弦值。
        hypot(x, y)     返回欧几里德范数 sqrt(x*x + y*y)。
        sin(x)          返回的x弧度的正弦值。
        tan(x)          返回x弧度的正切值。
        degrees(x)      将弧度转换为角度,如degrees(math.pi/2)，返回90.0
        radians(x)      将角度转换为弧度
    5:数学常量
        pi	            数学常量 pi（圆周率，一般以π来表示）
        e	            数学常量 e，e即自然常数（自然常数）
