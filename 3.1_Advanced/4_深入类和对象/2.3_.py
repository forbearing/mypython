#!/usr/bin/env python3
# https://www.jianshu.com/p/19ed49293168

# 1:定义抽象类
#   在 abc_base.py 中定义一个抽象基类 PluginBase, 这个基类用于保存和加载数据
#   通过 @abc.abstractmethod 将方法声明为抽象方法
import abc
class PluginBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return
    
    @abc.abstractmethod
    def save(self, output, data):
        """save the data object to the output."""
        return


# 2:注册具体类
#   然后在 abc_registry.py 中定义一个具体的类
import abc
from abc_base import PluginBase
class RegisteredImplementation(object):
    def load(self, input):
        return input.read()
    def save(self, output, data):
        return output.write(data)
PluginBase.register(RegisteredImplet)
