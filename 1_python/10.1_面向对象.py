概念
    1:面向过程是一件事 “该怎么做“，面向对象是一件事 “该让谁来做”，然后这个谁就是对象，
      它要怎么做是它的事，反正最后一群对象合理能把这事做好就行。
    2:对象是面向对象编程的核心，在使用对象的过程中，为了将具有共同特征和行为的一组对象抽象定义，
      提出了另外一个新的概念 -- 类
    3:面向对象三个特性：继承、封装、多态
定义一个类
    class 类名:
        方法列表

    class Car
        def start(self):
            print("car started")
        def stop(self):
            print("car stoped")
    c = Car()
    c.start()


属性和方法的私有化
    1:如果有一个对象，当需要对其修改属性时，有2种方法
        对象名.属性名 = 数据    （直接修改）
        对象名.方法名()         （间接修改）
    2:为了更好的保护属性安全，不能随意修改，一般的处理方式为
        将属性定义为私有属性
        添加一个可以调用的方法，供调用
    3:Python 中没有像 C++ 只的 public 和 private 这些关键字来区别公有属性和私有属性，它是以
      属性命名方式来区别，如果在属性前面加了2个下划线"__"，则表示该方法或属性是私有的
    class User:
        def __init__(self,passwd):
            if len(passwd) >= 8:
                self.__passwd = passwd
            else:
                print("密码不符合规范，必须大于8位")
    u1 = User('123456789')


继承和单继承
    1:虽然子类没有定义 __init__ 方法，但是父类有，所以在子类继承父类的时候这个方法就被继承了，
      所以子类默认执行了父类中那个继承过来的 __init__() 方法
    2:子类在继承时，在定义类时，小括号中为父类的名字
    3:父类的属性，方法会被继承给子类
    3:私有属性
        1:私有的属性，不能通过对象直接访问，但是可以通过方法访问
        2:私有的方法，不能通过对象直接访问
        3:私有的属性、方法，不会被子类继承，也不能被访问
        4:一般情况下，私有属性、方法都是不对外公布的，往往用来做内部的事，起到安全的作用。
    class Animal:
        def eat(self):
            print("eating")
        def sleep(self):
            print("sleeping")
    class Dog(Animal):
        def fright(self):
            print("flighting")
    class Cat(Animal):
        def miao(self):
            print("miao")
多继承
    1:子类在继承时，在定义类时，小括号() 中卫为父类的名字
    print(多继承类.__mro__)
        # 查看多继承关系
方法的重写
    1:所谓重写，就是子类中，有一个和父类相同名字的方法，在子类中会覆盖掉父类中同名的方法。
    super().__init__()      主动调用父类的 init 方法
多态
    1:定义时的类型和运行时的类型不一样，此时就成为多态。
    2:Python 伪代码实现 Java 或 C# 的多态。



类属性、实例属性
    1:类属性：这个类下的所对象都可以共享这个类属性，相当于 Java 中的静态属性
    class User:
        name = "Tom"
        __age = 18
    u = User()
    print(u.name)           # 正确
    print(User.name)        # 正确
    print(u.__age)          # 错误，不能在类外通过实例对象访问私有的类属性
    print(Usage.__age)      # 错误，不能在类外通过类对象访问私有的类属性
类方法、实例方法
    1:类方法的第一个参数是类对象 cls，通过 cls 引用的必定是类的属性和方法
    2:实例/对象的第一个参数为 self，通过 self 引用的可能是类属性，也有可能是实例属性
    3:在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高
    4:需要修饰器 @classmethod
静态方法
    1:需要修饰器 @staticmethod 来进行修饰，静态方法不需要多定义参数
    2:没有默认传递的参数，可以通过类对象来调用，也可以通过类名来调用。
    4:特殊的类方法：修饰器不同、没有默认传递的参数


__new__() 方法
    1:__new__() 至少要有一个参数 cls，代表要实例化的类，此参数在实例化时由 python 解释器自动提供
    2:__new__() 必须要有返回值，返回实例化出来的实例，可以 reutrn 父类 __new__ 出来的实例，
      或者直接是 object 的 __new__ 出来的实例
    3:__init__() 有一个参数 self，就是这个 __new__() 返回的实例，__init__() 在 __new__() 的基础上
      可以完成一些其他初始化的动作，__init__() 不需要返回值
    class User(object):
        def __new__(cls):
            print("__new__()")
            ret = object.__new__(cls)
            return ret
        def __init__(self):
            print("__init__()")
__init__() 方法
    1:__init__() 方法在创建对象时，默认被调用，不需要手动调用
    2:__init__(self) 中，默认有一个参数名字为 self，如果在创建对象时传递了2个参数，那么
      __init__(self) 中的 self 作为第一个形参外还需要2个形参，例如 __init__(self,x,y)
    3:__init__(self) 中的 self 参数，不需要开发者传递，python 解释器会自动把当前的对象
      引用传递进去
    class Person:
        def __init__(self):
            self.name='zhangsan'
            self.age='18'
        def print_info(self):
            print("名字：%s"%self.name)
            print("年龄：%s"%self.age)
    p1 = Person()
    pl.print_info()

    class Person:
        def __init__(self,name,age,height):
            self.name=name
            self.age=age
            self.height=height
        def print_info():
            print("名字：%s"%self.name)
            print("年龄：%s"%self.age)
            print("身高：%s"%self.height)
    p1 = Person('张三','19','172')
    p1.print_info()
__str__ 方法
    1:在 python 中方法名如 __xxx__() 的，那么就有特殊功能，因此叫做 “魔法” 方法
    2:当使用 print 输出对象的时候，只要自己定义了 __str__(self) 方法，那么就会打印
      在这个方法中 return 的数据。
    class P:
        def __init__(self,name,age,height):
            self.name=name
            self.age=age
            self.height=height
        def __str__(self):
            return "姓名：%s、年龄：%s、身高：%s"%(self.name,self.age,self.height)
    p1 = P()
    p1 = P('张三','19','172')
    print(p1)
__del__() 方法
    1:创建对象后，python 解释器默认调用 __init__() 方法，当删除一个对象时，python 解释器也会默认
      调用一个方法，这个方法为 __del__() 方法
    2:当内存中构建一个对象数据时，会调用 __init__() 方法，当内存中销毁（释放）一个对象数据时，
      会调用一个 __del__() 方法。
    3:总结：
        1:当一个变量保存了对象的引用时，此对象的引用计数器就会加1，
        2:当使用 del 删除变量指向的对象时，如果对象的引用计数器不为1，比如3，那么此时只会让这个
          引用计数器减1，即变成2，当再次调用 del 时，变为1，如果再调用1次del，此时会真的
          把对象删除。


单例模式
    1:确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，
      单例模式是一种对象创建型模式。
简单工厂模式
    1:工厂模式是我们最常见的实例化对象模式，是用工厂方法代替 new 操作的一种模式，虽然这样做，
      可能多做一些工作，但会给系统带来更大的扩展性和尽量少的修改量。
    2:Simple Factory 模式不是独立的设计模式，他是 Factory Method 模式的一种简单的、特殊的实现，
      也被称为静态工厂模式，
工厂方法模式
    1:工厂方法去掉了简单工厂模式中工厂方法的静态方法，使得它可以被子类继承，对于 Python 来说，
      就是工厂类被具体工厂继承。
注意
    1:根据业务需求，抽象出你要定义的类
    2:根据业务需求，要知道每个类的职责，根据职责来定义类的属性和方法


为对象动态添加属性
    class Person(object):
        def __init__(self, name=None, age=None):
            self.name = name
            self.age = age
    p = Person('xiaoming', "24")
    p.sex = 'male'
为对象添加实例方法
    import types
    class User:
        def __init__(self):
            self.name = 'zhangsan'
            self.passwd = 'passwd'
    def showInfo(self):     # self 在此可以替换成别的形参
        print(self.name)
        print(self.passwd)
    u1 = User()
    u2 = User()
    u1.myShow = types.MethodType(showInfo, u1)
    u1.myShow()
    u2.myShow = types.MethodType(showInfo, u2)
    u2.myShow()
    var = types.MethodType(showInfo, u2)
    var()
为类添加类方法
    class User:
        name = 'lisi'
        passwd = 'passwd'
    @classmethod
    def func(cls):
        print("classMethod")
        cls.name = 'python'
        cls.passwd = 'python'
    u = User()
    User.func = func
    User.func()
    u.func()
为类添加静态方法
    class User:
        name = 'lisi'
        passwd = 'passwd'
    @staticmethod
    def func():
        print("staticMethod")
    User.func = func

限制类属性的添加
    class Person(object):
        __slots__ = ("name","age")
    p = Person()
    p.name = 'lisi'
    p.age = '18'
    p.score = 10
        # AttributeError 错误
        # __slots__ 定义的属性仅对当前类实例起作用，对继承的子类不起作用
