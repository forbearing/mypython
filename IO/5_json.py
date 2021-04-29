#!/usr/bin/env python3

1:JSON 表示出来就是字符串，可以被所有语言读取，也可以方便的存储在磁盘或者通过网络传输。
  JSON 不仅是标准格式，并且比 XML 更快，而且可以直接在 Web 页面中读取，非常方便
2:由于 JSON 标准规定 JSON 编码是 UTF-8，所以总是能正确的在 Python 的 str 与 JSON 
  字符串之间转换。

    import json
    d = dict(name='Bob', age=22, score=88)
    json.dumps(d)
    # dumps 方法返回一个 str，内容是标准的 JSON。

    json_str = '{"age":20, "score":88, "name":"Bob"}'
    d = json.loads(json_str)
    print(d)

3:序列化实例
    import json
    class Student(object):
        def __init__(self, name, age, score):
            self.name = name
            self.age = age
            self.score = socre
    s = Student('Bob', 22, 88)

    def student2dict(std):
        return {
                'name': std.name,
                'age': std.age,
                'score': std.score
                }
    print(json.dumps(s, default=student2dict))

3:反序列化实例
    def dict2student(d):
        return student(d['name'], d['age'], d['score'])

4:把任意实例序列化为 JSON
    print(json.dumps(s, default=lambda obj: obj.__dict__))
