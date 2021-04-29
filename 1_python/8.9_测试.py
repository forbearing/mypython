#!/usr/bin/env python3

1:单元测试
    1:作用: 用来对一个函数,一个类或者一个模块进行正确性校验
    2:结果
        单元测试通过: 说明测试的函数功能正常
        单元测试不通过: 说明函数功能有 BUG, 要么测试条件输入有误

    ---
    # 对函数进行单元测试
    vi func.py
        def myAdd(a, b):
            return a + b
        def mySub(a, b):
            return a - b
        def myMulti(a, b):
            return a * b
        def myDev(a, b):
            if b ==0:
                return 0
            return a/b

    vi test.py
        import unittest
        from func import myAdd, mySub, myMulti, myDev

        class Test(unittest.TestCase):
            # setUp 和 tearDown 相当户初始化,写不写都无所谓
            def setUp(self):
                print("开始测试时自动调用")
            def tearDown(self):
                print("结束测试时自动调用")
            def test_myAdd(self):
                # 在需要测试的函数前面加 test_ 就可以对该函数进行测试
                self.assertEqual(myAdd(1,2), 3, "加法有误")
            def test_mySub(self):
                self.assertEqual(mySub(2,1), 1, "减法有误")
            def test_myMuti(self):
                self.assertEqual(myMulti(2,2), 4, "乘法有误")
            def test_myDev(self):
                self.assertEqual(myDev(4,2), 2, "除法有误")

        if __name__ == "__main__":
            unittest.main()

    ---
    # 对类进行测试
    vi  person.py
        class Person(object):
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def getName(self):
                return self.name

            def getAge(self):
                return self.age

    vi test.py
        import unittest
        from person import Person

        class Test(unittest.TestCase):
            def test_init(self):
                # 测试 __init__ 函数, 注意不要加上 init 之前的 __
                p = Person("hybfkuf", 24)
                self.assertEqual(p.name, "hybfkuf", "属性赋值有误")
            def test_getAge(self):
                p = Person("hybfkuf", 24)
                self.assertEqual(p.getAge(), p.age, "getAge 函数有误")

        if __name__ == "__main__":
            unittest.main()

    ---
    # 一个测试
    vi mydict.py
        class Dict(dict):
            def __init__(self, **kw):
                super().__init__(**kw)
            def __getattr__(self, key):
                try:
                    return self[key]
                except KeyError as e:
                    raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
            def __setattr__(self, key, value):
                self[key] = value

    vi main.py
        import unittest
        from mydict import Dict

        class TestDict(unittest.TestCase):
            def test_init(self):
                d = Dict(a=1, b='test')
                self.assertEqual(d.a, 1)
                self.assertEqual(d.b, 'test')
                self.assertTrue(isinstance(d, dict))

            def test_key(self):
                d = Dict()
                d['key'] = 'value'
                self.assertEqual(d.key, 'value')

            def test_attr(self):
                d = Dict()
                d.key = 'value'
                self.assertTrue('key' in d)
                self.assertEqual(d['key'], 'value')

            def test_keyerror(self):
                d = Dict()
                with self.assertRaises(KeyError):
                    value = d['empty']

            def test_attrerror(self):
                d = Dict()
                with self.assertRaises(AttributeError):
                    value = d.empty

        if __name__ == '__main__':
            unittest.main()






2:文档测试
    ---
    1:Python 内置的 “文档测试”(doctest) 模块可以直接提取注释中的代码并执行测试
    2:doctest 严格按照 Python 交互式命令行的输入和输出来判断测试结果是否正确。
    3:只有异常的时候，可以用 ... 表示中间一大段烦人的输出
    4:doctest 非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具
      就可以自动把包含 doctest 的注释提取出来。用户看文档的时候，同时也看到了 doctest

    ---
    import doctest
    # 这个模块可以提取注释中的代码执行
    # doctest 模块严格按照  python 交互模式的输入提取

    def mySum(x, y):
        '''
        get the sum of two number
        :param x: firstNum
        :param y: secondNum
        :return: sum
        >>> print(mySum(1,2))
        3
        '''
        return  x+y


    print(mySum(1,2))

    # 进程文档测试
    if __name__ == "__main__":
        import doctest
        doctest.testmod()
