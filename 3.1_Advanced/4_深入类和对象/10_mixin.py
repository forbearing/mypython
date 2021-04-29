1:使用 Mixin 类实现多重继承需要注意
    1:首先它必须表示某一种功能,而不是某个物品, 同 Java 中的  Runable 和 Callable
    2:必须责任单一, 如果有多个功能, 那就写多个 Mixin 类
    3:不依赖于子类的实现
    4:自雷即使没有继承这个 Mixin 类, 也照样工作, 即使缺少某个功能

    class Vehicle(object):
        pass
    class PlaneMixin(object):
        def fly(self):
            print("I am flying")
    class AirPlane(Vehicle, PlaneMixin)
        pass

2:
    1:Mixin 模式是一种在 python 里经常使用的模式,适当合理的应用能够达到服用代码,
      合理组织代码结构的目的

    class SimpleItemContainer(object):
        def __init__(self, id, item_containers):
            self.id = id
            self.data = {}
            for item in item_containers:
                self.data[item.id] =  item

    from UseDict import DictMixin
    class BetterSimpleItemContainer(object, DictMixin):
        def __getitem__(self, id):
            return self.data[id]
        def __setitem__(self, id, value):
            self.data[id] = value
        def __delitem__(self, id):
            del self.data[id]
        def keys(self):
            return self.data.keys()

3:
    1:模式单一
    2:不和基类关联, 可以和任意基类组合
    3:在 mixin  中, 不要使用 super() 方法
