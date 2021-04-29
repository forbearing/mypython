函数的定义和调用


局部变量、全局变量
	- 在函数中，不使用 global 声明全局变量时，不能修改全局变量的本质是因为，不能修改全局变量的
      指向，即不能将全局变量指向新的数据
	- 对于不可变类型的全局变量，因为其指向的数据不能修改，所以不使用 global 时无法修改全局变量
	- 对于可变类型的全局变量，因为其指向的数据可以修改，所以不使用 global 时也可以修改全局变量
	- 全局变量定义在调用函数之前，不是定义函数之前

	= 可变类型：值可以修改（内存地址不变但所保存的值变化了）引用可以修改（变量的内存地址变化了）
	- 不可变类型：值不可以修改，可以修改变量的引用（= 赋值号）
	- 在函数里面修改全局变量
		1:如果函数变量是可变类型的，所以在函数里面任意修改（值、引用）
		2:如果函数变量是不可变类型的，在函数里面不可以修改值，也不能修改引用，除非加上 global，
          才能修改饮用。
	- 全局变量放在调用函数之前，不是定义函数之前。


函数参数
    1:缺省参数
        1:语法
            def func(a=1,b=2,c=3):
                return a+b+c
            d=func()
            print(d)
        2:带有默认值的参数一定要位于参数列表的最后面
    2:不定长参数
        1:有时候我们需要一个函数能处理比当初声明时更多的参数，这些参数叫做不定长参数，
          声明时不会命名
        2:语法
            def func(x,y,*args):
                print(x,y)
                print(args)
                sum = x+y
                for i in args:
                    sum+=i
                print(sum)

            def func(x,*args,**kwargs):
                print(x)
                print(args)
                print(kwargs)
                sum = x
                for i in args:
                    sum += i
                for i in kwargs.values():
                    sum += i
            func(2,3,4,num1=5,num2=6)
            args=[2,3]
            kwargs{'num1':5,'num2':6}
            func(2,*args,**kwargs)      # 集合的拆包
    3:引用传参
        1:语法
            def func(x,y):
                x=x.replace('a','A')
                y=y.append(10)
                print(x,y)
            a='abcdefg'
            b=[1,2,3]
            func(a,b)
            print(a,b)
            print(id(a),id(b))


函数返回
	1:函数返回多个值
            def func():
                a,b=1,2
                return a,b              # 返回元组
                #return [a,b]           # 返回列表
            x,y=func()                  # x,y 为字符串
            c=func()                    # c 为元组
            # return [a,b]  d=func()    # d 为列表
            print(x)
            print(y)


匿名函数
    1:用 lambda 关键字可以创建小型匿名函数，这种函数得名于省略了 def 声明函数的标准步骤
      lambda 函数能接受任何数量的参数，但只能返回一个表达式的值
      匿名函数不能直接调用 print，因为 lambda 需要一个表达式。
    2:语法
        lambda [arg1 [,arg2, .... argn]]: expression
        sum = lambda arg1, arg2: arg1 + arg2
    3:使用场景
        def func(a,b,func):
            result = func(a,b)
            return result
        print(func(22,33,lambda x,y:x+y))

        stus=[{"name":"zs","age":22},{"name":"lisi","age":33}]


封装函数、递归函数


重难点
    1:局部变量和全局变量的区别
    2:可变类型和不可变类型在函数中使用
#    3:不定长参数、拆包、缺省参数
