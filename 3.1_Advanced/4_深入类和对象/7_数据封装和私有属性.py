1:私有属性的封装
    1:私有属性的含义是外部不能直接用 实例名.私有属性名进行访问, 子类同样也是一样不能
      访问, 这样就对数据进行封装. 只能用公共的方法里调用私有属性, 例如
    2:如果想通过私有属性就在属性名前面加上 __
    3:只能通过方法来返回私有属性的值.
    4:同理,方法名也有私有属性,在方法名前面加 __ 即可,同样也不能访问
    5:只是相对安全,不是绝对安全


    class Date:
        def __init__(self, birth):
            self.__birth = birth
    date = Date(1996)
    print(date.__birth)

    class Date:
        def __init__(self, birth):
            self.__birth = birth
        def get_birth(self):
            return self.__birth
    date = Date(1996)
    print(date.get_birth())



2:私有属性封装原理
    
    class Date:
    def __init__(self,birthday):
        self.__birthday=birthday
    def __get_birthday(self):
        return self.__birthday
    date=Date(1960)
    print(date._Date__birthday)
    print(date._Date__get_birthday())
