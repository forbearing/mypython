1:
    1:super 是用来解决多重继承问题的,直接用类名调用父类方法在使用单继承的时候没问题,但是 
      如果使用多继承,会涉及到查找顺序(MRO), 重复调用(钻石继承) 等种种问题.
    2:MRO 就是类的方法解析顺序表,其实也是继承父类方法时的顺序表
    3:当我们调用 super() 的时候,实际上实例化了一个 super 类. super是一个类,既不是关键字
      也不是函数扥其他结构
    4:在大多数情况下, super 包含了两个非常重要的信息: 一个 MRO(Method Resolution Order)
      列表以及 MRO 中的一个类.


2:
