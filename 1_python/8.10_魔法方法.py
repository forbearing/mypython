#!/usr/bin/env python3

总结：
    1:__getattr__, __getattribute__ 实例对象属性寻找顺序
        1:首先访问 __getattribute__() 魔法方法(隐含默认调用,无论何种情况,均会调用此方法)
        2:去实例对象 object.__dict__ 中查找是否具备该属性. 每个类和实例对象都有一个 __dict__ 的属性
        3:若在 object.__dict__ 中找不到对应的属性,则去该实例的类中寻找 object.__class__.__dict__
        4:若在实例中也找不到该属性, 则去该实例的父类中寻找 object.__class__.__bases__.__dict__
        5:若以上均无法找到, 则会调用 __getattr__ 方法, 执行内部的命令. 
          若未重载 __getattr__ 方法，则直接报错：AttributeError

=== __getattr__
object._getattr_(self, name)
    --- 概述
    1:拦截点号运算。当对未定义的属性名称和实例进行点号运算时，就会用属性名作为字符串
      调用这个方法。如果继承树可以找到该属性，则不调用此方法
      当属性 name 可以通过正常机制追溯到时，__getattr__是不会被调用的
    2:实例 instance 通过 instance.name 访问属性 name，只有当属性 name 没有在实例的
      __dict__ 或它构造类的 __dict__ 或基类的 __dict__ 中没有找到，才会调用 __getattr__
    3:如果在 __getattr__(self, attr) 存在通过 self.attr 访问属性，会出现无限递归错误。
      正确做法是 self.__dict__.attr

    --- 一段代码
    class Cat
        class_level = '贵族'
        def __init__(self, name, age):
            self.name = name
            self.age = self.age
        def run(self):
            print("%s age is %s and is running" %(self.name, self.age))
        def __getattr__(self, item):
            print("正在 __getattr__ 属性")
        def __setattr__(self, key, value):
            # print("正在 __setattr__ 属性")
            self.__dict__[key] = value
        def __delattr__(self, item):
            # print("正在 __delattr__ 属性")
            self.__dict__.pop(item)

    --- 一个示例
    class ClassA(object):
        def __init__(self, classname):
            self.classname = classname
        def __getattr__(self, attr):
            return('invoke __getattr__', attr)
    insA = ClassA('ClassA')
    print(insA.__dict__) # 实例insA已经有classname属性了
    print(insA.classname) # 不会调用__getattr__
    print(insA.grade) # grade属性没有找到，调用__getattr__



=== __getattribute__
object.__getattribute__(self, name)
    ---
    1:实例 instance 通过 instance.name 访问属性 name，__getattribute__ 方法一直会被调用，
      无论属性name是否追溯到
    2:如果类还定义了 __getattr__ 方法，除非通过 __getattribute__ 显式的调用它，或者
      __getattribute__ 方法出现 AttributeError 错误，否则 __getattr__ 方法不会被调用了
    3:如果在__getattribute__(self, attr)方法下存在通过self.attr访问属性，会出现无限递归错误

    ---
    class ClassA(object):
        def __init__(self, classname):
            self.classname = classname
        def __getattr__(self, attr):
            return('invoke __getattr__', attr)
        def __getattribute__(self, attr):
            return('invoke __getattribute__', attr)
    insA = ClassA('ClassA')
    print(insA.__dict__)
    print(insA.classname)       # 调用 __getattribute__
    print(insA.grade)           # 调用 __getattribute__



=== __setattr__
object.__setattr__(self, name, value)
    ---
    1:会拦截所有属性的的赋值语句，如果定义了这个方法，self.arrt = value 就会变成
      self.__setattr__("attr", value)
    2:当在 __setattr__ 方法内对属性进行赋值时，不可使用 self.attr = value, 因为他会
      再次调用 self.__setattr__("attr", value), 则会形成无穷递归循环，最后导致堆栈溢出异常
      应该通过对属性字典做索引运算来赋值任何实例属性：self.__dict__['name'] = value



=== __call__
object.__call__(self[, args...])
    ---
    定义类的时候，实现了 __call__ 函数，这个类型就可以成为可调用。换句话说，我们可以把
    这个类的对象当作函数来使用，相当于重载了括号运算符

    ---
    class Student(object):
        def __init__(self, name):
            self.name = name
        def __call__(self):
            print("My name is %s." %self.name)
    s = Student('Michael')
    s()

    ---
    class Dict(dict):
        def __init__(self, **kw):
            super().__init__(**kw)

        def __getattr__(self, key):
            try:
                print("In '__getattr__'")
                return self[key]
            except KeyError as k:
                return None

        def __setattr__(self, key, value):
            print("In '__setattr__'")
            self[key] = value

        def __delattr__(self, key):
            try:
                del self[key]
            except KeyError as k:
                return None

        def __call__(self, key):
            try:
                print("In '__call__'")
                return self(key)
            except KeyError as k:
                return "In '__call__' error"

    d = Dict()
    d.name = 'hello'
    print(d.name)
