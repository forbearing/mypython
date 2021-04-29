1:导入模块
    import module1,module2
    from random import *
        不符合 python 规范，如果导入的两个模块中的函数又相同，后导入的函数就会覆盖前面导入的函数
    from random import randint,module2
    import random as r
    print(random.__file__)      # 打印模块的路径

2:自定义模块
    1:根据 __name__ 变量的结果能够判断出，是直接执行的 python 脚本还是被引入执行的，
      从而能够选择性的执行测试代码。
    if __name__ == '__main__':          # 由 python 解释器主动执行该模块代码为了测试
        print("测试代码")

3:包
    1:python3 中
        1:包就是一个目录
        2:把多个 py 文件放到同一个文件夹下
        3:使用 import 文件夹.模块的方式导入
    2:python2 中
        1:在 python2 中，有一个目录，并且目录下有一个 __init__.py 的文件，才叫包
        2:需要在包的文件夹下创建 __init__.py 文件（虽然文件内容没有，但是 python2 可以用了）
        3:在 __init__.py 文件中写入
            from . import module1
            from . import module2
            那么就可以使用 import 文件夹 导入
    3:from 包 import 模块
    4:在 __init__.py 在 python3 中没有错，以后都在包的目录下新建一个 __init__ 文件。
    5:__init__.py
        1:__init__.py 控制着包的导入行为
        2:__init__.py 为空，仅仅是把这个包导入，不会导入包中的模块
        模块.func

4:模块的发布
    1:在包的同级目录下写两行代码
        vim setup.py
            from distutils.core import setup
            setup(name="压缩包的名字", version="1.0", description="描述", author="作者",
                    py_modules=['package.module1', 'package.module2'])
        setup.py build              # 构建模块
        setup.py sdist              # 生成发布压缩包

5:模块的安装
    1:找到模块的压缩包（拷贝到其他地方）
    2:解压缩并进入文件夹
    3:执行命令 python setup install
    python setup 安装时，可以使用 --prefix 指定安装目录
        python setup.py install --prefix=install_path
    模块的导入
        import myPackage
        myPackage.module1.pr1()
        from myPackage import moudle1
        module1.pr()

6:其他

1:给程序传递参数
    import sys
    print(sys.argv)
2:列表推导式
    a = [1 for x in range(1,10)]
    a = [x for x in range(1,10)]
    a = [x for x in range(1,10) for y in range(0,2)]
    a = [x for x in range(1,10) if x%2==1]
    a = [(x,y) for x in range(1,10) for y in range(0,2)]
3:
