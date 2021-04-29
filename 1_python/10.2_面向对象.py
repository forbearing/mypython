1:概述
    1:目前代码量少，写在一个文件中还体现不出什么，但是随着代码量越来越多，代码就
      越难维护。为了解决难以维护的问题，我们把很多相似功能的函数分组，分别放到不同的
      文件中去。这样每个文件所包含的内容相对减少，而且对于每一个文件的大致功能可用
      文件名来体现，很多编程语言都是这么来组织代码结构的。
    2:一个 .py 文件就是一个模块
    3:优点
        1:提高了代码的可维护性
        2:提高了代码的复用度，当一个模块完毕，可以被多个地方引用
        3:引用其他的模块（内置模块、第三方模块、自定义模块）
        4:避免函数名和变量名的冲突
2:使用自定义模块
    1:一个 .py 文件就是一个模块
    2:import 语句，引入模块
        import module1[,module2]
        from module1 import name1[,name2]       从模块中导入一个或多个指定的部分到当前命名空间
        from module1 import *                   最好不要过多的使用
    3:引入自定义模块，不用加 .py 后缀，自定义模块须和程序文件处在同一目录下
    4:一个模块只会被执行一次，不管你执行了多少次 import
    5:程序内容个的函数可以将模块中的同名函数覆盖

3:__name__ 属性
    1:模块就是一个可执行的 .py文件，一个模块被另一个程序引入，但不想让模块中的某些代码,
      可以用 __name__ 属性来使程序仅调用模块中的一部分
    2:每一个模块都有一个 __name__ 属性，当其值等于 "__main__" 时，表明该模块自身在执行
      当模块被导入时，__name__ 的值为模块名
        if __name__ == "__main__":
            print("模块正在执行 ")
        else:
            # 当模块被引用时，执行下面的程序
            def sayGood():
                print("Good!")
            def sayNice():
                print("Nice!")
            def sayHandsome():
                print("Handsome!")
4:包
    1:如果不同的人编写的模块同名怎么办？为了解决模块命名的冲突，引入了按目录来组织模块
      的方法：称为包。
    2:引入了包之后，只要顶层的包不与其他人发生冲突，那么模块都不会与别人的发生冲突
    3:目录只有包含一个 __init__.py 的文件，才被认作是一个包，主要是为了避免
      一些滥竽充数的名字，基本上目前这个文件中什么也不用写

5:安装第三方包
    pip install --upgrade pip
    pip install pillow



---
import sys
for i in sys.argv:
    print(i)
name = sys.argv[1]
age = sys.argv[2]
hoby = sys.argv[3]
print(name, age, body)
print(sys.path)

---
from PIL import Image
im = Image.open('/home/hybfkuf/Downloads/1.jpg')
print(im.format, im.size, im.mode)
im.thumbnail(150, 100)
im.save("temp.jpg", "JPEG")




===============================================================================



1:什么是面向过程
    1:自上而下顺序执行，逐步求精
    2:其程序结构是按功能划分为若干个基本模块，这是树状结构
    3:各模块之间的关系尽可能简单，在功能上相对独立
    4:每一模块内部都是由顺序、选择和循环三种基本逻辑构成
    5:其模块化实现的具体方式是使用子程序
    6:程序流程在写程序的就已决定了

2:什么是面向对象
    1:把数据和对数据的操作方法放在一起，作为一个项目依赖的整体 -- 对象
    2:对同类对象抽象出其共性，形成类
    3:类中的大多数数据，只能用本类的方法进行处理
    4:类通过一个简单的外部接口与外界发生关系，对象与对象之间通过消息进行通信
    5:程序流程由用户在使用中决定

3:理解面向对象
    1:面向对象是相对面向过程而言
    2:面向对象和面向过程都是一种思想
    3:面向过程
        强调的是功能行为
        关注的是解决问题需要哪些步骤
    4:面向对象
        将功能封装进对象，强调具备了功能的对象
        关注的是解决问题需要哪些对象
    5:面向对象是基于面向过程的

4:面向对象的特点
    1:是一种符合人们思考习惯的思想
    2:可以将复杂的事情简单化
    3:将程序员从执行者转换成指挥者
    4:完成需求：
        1:先去找具有所需的功能的对象来用
        2:如果该对象不存在，那么创建一个具有所需功能的对象。




1:构造函数
    1:构造函数，__init__()  在使用类创建对象的时候自动调用
    2:如果不显式的写出构造函数，默认认会自动添加一个看空的构造函数
    3:self 代表类的对象，而非类，self.__class__ 代表类名
    4:哪个对象调用方法，那么该方法中的 self 就代表这个对象本身
    5:self 不是关键字，换成其他的标志符也是可以的
        class Person(object):
            def __init__(self, name, age, g):
                self.name = name
                self.age = age
                self.m = m
            def info(wokao):
                print("name: %s age: %s g: %s" %(wokao.name, wokao.age, wokao.g))
    6:self.__class__ 代表类名
        class Person(object):
            def __init__(self, name, age, g):
                self.name = name
                self.age = age
                self.m = m
            def info(self):
                print(self.__class__)
                print("name: %s age: %s g: %s" %(self.name, self.age, self.g))
            def run(self):
                p = self.__class__("hybfkuf", 24, "m")
                p.info()

2:析构函数
    1:析构函数，__del__() 释放对象是自动调用
        class Person(object):
            def __init__(self):
                print("__init__")
            def __del__(self):
                print("__del__")
    2:调用析构函数 __del__() 的场景 
        1:在函数里定义的对象，会在函数结束时自动释放，这样可以减少内存空间的浪费
        2:程序结束，释放对象，调用 __del__()
        3:手动释放，del(youObject)

3:重写 __repr__ 和 __str__ 函数
    1:重写：将函数重新定义写一遍
    2:__str__(), 在 print 打印对象自动调用，是给用户用过的，是一个描述对象的方法
      如果 __str__() 方法不存在，则调用 __repr__()方法
        class Person(object):
            def __str__(self):
                return "__str__"
        p = Person()
        print(p)
    3:__repr__(), 是给机器用的，在 Python 解释器里面直接敲对象名时调用的方法
    4:优点：
        - 当一个对象的属性值很多，并且需要打印时，可以重写 __repr__()

4:访问限制-私有属性
    1:操作私有属性
        1:通过类方法修改私有属性
        2:通过 _类名__属性名 访问，
    2:强烈不建议使用 _类名__属性名 去访问，因为不同的解释器可能存在解释的变量名不一致。
    3:__var__ 不是私有属性，仅仅变量只有前面两个下划线
    4:在 Python 中 __var__ 为特殊变量，特殊变量可以直接访问
    5:在 Python 中，_var 是可以通过外部访问的，但是按照约定的规则，当我们看到这样的
      变量时，意思是：“虽然我可以被访问，但是请把我视为私有变量，不要直接访问

5:继承：
    1:优点
        1:继承的作用
            简化了代码，减少了冗余
        2:提高了代码的健壮性
        3:提高了代码的安全性
        4:是多态的前提
    2:缺点
        1:耦合与与内聚是描述类与类之间的关系的，耦合性越低，内举性越高，代码越好
          继承中，父类和子类的耦合性很高。

6:多继承
    1:父类中方法名相同，默认调用的是在括号中前面的父类中的方法
    vi father.py
        class Father(object):
            def __init__(self, money):
                self.money = money
            def run(self):
                print("Play")
            def func(self):
                print("father")
    vi mother.py
        class Mother(object):
            def __init__(self, faceValue):
                self.faceValue = faceValue
            def eat(self):
                print("eat")
            def func(self):
                print("mother")
    vi child.py
        from father import Father
        from mother import Mother
        class Child(Father, Mother):
            def __init__(self, money, faceValue):
                Father.__init__(self, money)
                Mother.__init__(self, faceValue)
    vi main.py
        from child import Child
        def main():
            c = Child(300, 100)
            print(c.money, c.faceValue)
        if __name__ == "__main__":
            main()

7:多态
    1:一种事物的多种形态
    2:思考: 100种动物都有 name 属性和 eat 动作。定义了一个有 name 属性和 eat 方法的
      Animal 类，让所有的动物类都继承自 Animal
        vi animal.py
            class Animal(object):
                def __init__(self, name):
                    self.name = name
                def eat(self):
                    print("%s is eating" %self.name)
        vi cat.py
            from animal import Animal
            class Cat(Animal):
                def __init__(self, name):
                    super(Cat, self).__init__(name)
        vi mouse.py
            from animal import Animal
            class Mouse(Animal):
                def __init__(self, name):
                    super().__init__(name)
            tom = Mouse('tom')
            tom.eat()
    3:定义一个人类，可以喂猫和老鼠吃东西
        vi  person.py
            class Person(object):
                # def __init__(self, animal):
                    # self.animal = animal
                def feedAnimal(self, ani)
                    print("给你吃的")
                    ani.eat()
                # def feedCat(self, cat):
                    # print("给你吃的")
                    # cat.eat()
                # def feedMouse(self, mouse):
                    # print("给你吃的")
                    # mouse.eat()
        vi main.py
            from person import Person
            from cat import Cat
            from mouse import Mouse
            tom = Mouse('tom')
            p = Person(tom)
            p.feedMouse()

8:对象属性和类属性
    class Person(object):
        name = "person"
        def __init__(self, name):
            self.name = name
    p = Person('hybfkuf')
    print(p.name)
    print(Persono.name)
    1:在这里的 name 属于类属性，需要用类名来调用
      self.name 是对象属性
    2:对象属性的优先级高于类属性，不要将对象属性与类属性重名，因为对象属性会屏蔽类
      属性，但是当删除对象属性时，再使用又能使用类类属性。

9:动态给实例添加属性和方法
    1:动态给对象添加对象属性，只针对当前对象生效，对于类创建的其他对象没有作用
    2:动态添加属性体现了动态语言的特点，灵活
    3:动态添加方法
        from types import MethodType
        person.speak = MethodType(say, per)
    4:只允许给对象添加特定的属性：在定义一个类的时候，定义一个特殊的属性 __slots__，
      其可以限制动态添加的属性。
        __slots__ = ("name", "age")         # 不允许添加的属性

10:property 属性
    1:Python 内置的 @property 装饰器就是负责把一个方法变成属性调用
    2:@property 实现比较复杂，其把一个 getter 方法变成属性，只需要加上 @property 就可以
      此时，@property 本身又创建了另一个装饰器 @score.setter，负责把一个 setter 方法
      变成属性赋值，于是，我们就拥有了一个可控的属性操作

        class Student(object):
            @property
            def score(self):
                return self.__score
            @score.setter
            def score(self, value):
                if not isinstance(value, int):
                    raise ValueError("score must be a integer!")
                if value < 0 or value > 100:
                    raise ValueError("Score must between 0-100!")
                self.__score = value
        s = Student()
        s.score = 60
        print(s.score)
 
    3:定义只读属性：只定义 getter 方法，不定义 setter 方法就是一个只读属性

        class Student(object):
            @property
            def birth(self):
                return self.__birth
            @birth.setter(self, value):
                self.__birth = value

            @property
            def age(self):
                return self.__age

        # birth 是可读写属性，而 age 是一个只读属性
    4:@property 广泛应用在类的定义中，可以让调用者写出剪短的代码，同时保证对参数进行
      必要的检查，这样，程序可以减少出错的可能性

11:运算符重载
    __init__            构造函数                X=class(args);
