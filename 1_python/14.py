导入模块的路径设置
    1:查看模块搜索路径
        import sys
        sys.path
    2:添加搜索路径
        sys.path.append('/home/sxt/xxx')
        sys.path.insert(0,'/home/sxt/xxx')      可以确保先搜索这个路径
    3:重新导入模块
        from imp import *
        reload(模块名)有
    4:查看已安装的模块
        pydoc modules               # 命令行下使用 pydoc 命令
        help("modules")             # 交互式解释器下使用，等同于 pydoc modules
        import sys
        sys.modules.keys()          # 在python交互是解释器下导入sys模块查看


循环导入
    - 两个模块相互导入
    - 怎样避免循环导入
    - 模块间降低耦合性
    

== 和 is
    is 比较两个引用是否指向了同一个对象（引用比较）
    == 是表两个对象是否相等（值比较）


深拷贝和浅拷贝
    - 浅拷贝是对于一个对象的顶层拷贝，通俗的理解就是：拷贝了引用，并没有拷贝内容
    - 深拷贝是对于一个对象所有层次的拷贝（递归）
    import copy
    copy.deepcopy           # 深拷贝
    copy.copy()             # 浅拷贝
    - 浅拷贝对不可变类型和可变类型的 copy 不同（例如列表和元组）
    - 分片表达式可以赋值一个序列
    - 字典 copy 方法可以拷贝一个字典
    - 有些内置函数可以生成拷（list）


类的数据隐藏（私有化）
    _x              私有化属性或方法
    __x             避免与子类中的属性命名冲突，无法在外部直接访问（名字重整所以访问不到）
    __x__           用户名字空间的魔法对象或属性，例如 __init__，不要自己发明这样的名字
    xx_             用于避免与 Python 关键字的冲突
    1:打印出私有属性
        class User:
            def __init__(self):
                self._passwd = "wokao"
                self.passwd = "nihao"
        u = User()
        print(u.passwd)
        print(dir(u))
        print(u._User__passwd)
    2:通过 name mangling（名字重整）目的就是以防子类意外重写基类的方法或者属性
      通过 _Class_object 机制就可以访问 private 
    3:父类中属性为 __name 的，子类不继承，子类不能访问
    4:如果在子类中向 __name 赋值，那么会在子类中定义的一个与父类相同名字的属性
    5:__name 的变量、函数、类在使用 from xxx import * 时都不会被导入 

property 用法
    - 为私有属性添加 getter 和 setter 方法
    - 使用 property 升级 getter 和 setter 方法
        money = property(getMoney,setMoney)
    - 使用 property 取代 getter 和 setter 方法
        @property
        @money.setter
    1:property 使用
        class User:
            def __init__(self):
                self.__passwd = "wokao"
            def getPasswd(self):
                return self.__passwd
            def setPasswd(self,p):
                self.__passwd = p
            myPasswd = property(getPasswd,setPasswd)
        u = User()
        u.myPasswd = "hello python"             # 设置 passwd
        print(u.myPasswd)                       # 打印 passwd
    2:property 进一步使用
        class User:
            def __init__(self):
                self.__passwd = "wokao"
            @property
            def myPasswd(self):
                return self.__passwd
            @myPasswd.setter
            def myPasswd(self,p):
                self.__passwd = p
        u = User()
        print(u.myPasswd)
        u.myPasswd = "hello python"
        print(u.myPasswd)


进制
    1:有符号和无符号的概念
    2:原码、反码、补码
        正数
            原码 = 反码 = 补码
        负数
            反码 = 符号位不变，其他位取反
            补码 - 反码 + 1
        负数补码转换原码的规则
            原码 = 补码的符号位不变 --> 数据位取反 --> 尾+1
    3:进制间转换
        num = 10
        b = bin(num)        # 转换成二进制，（字符串）
        o = oct(num)        # 转换成八进制
        h = hex(num)        # 转换成十六进制 
        int(b,2)            # 二进制转换成十进制
        int(o,8)            # 八进制转换成十进制
        int(h,16)           # 十六进制转换成十进制 


位运算
    &       按位与
    |       按位或
    ^       按位异或
    <<      按位左移
    >>      按位右移
    用途：直接操作二进制，省内存1
