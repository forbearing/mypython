1:JSON, JavaScript Object Notation, JavaScript 对象标记，它通过对象和数组的组合来表示数据，
  构造简洁但是结构化程度非常高
2:是一种轻量级数据交换格式。
3:在 JavaScript 语言中，一切都是对象。因此，任何支持的类型都可以通过 JSON 来表示，
  例如字符串、数字、对象，数组等。但是对象和数组是比较特殊的两种类型。




1:对象和数组
    1:对象：
        1:它在 JavaScript 中使用{} 包裹，{key:value, key:value ....} 的键值对结构。
        2:在面向对象对象的语言中。key 为对象的属性，value为对应的值。
        3:键名可以使用整数和字符串表示，值的类型可以是任意类型。
    2:数组
        1:数组在 JavaScript 中用 [] 包裹。数据结构为 ["java", "javascript", ...] 的索引结构
        2:在 JavaScript 中，数组是一种特殊的数据类型。它也可以像对象那样使用键值对，
          但是还是索引用的多。同样，值的类型可以是任意类型。
    3:一个 JSON 对象可以写为
        [{
            "name": "Bob",
            "gender": "male",
            "birthday": "1992-10-18"
        }, {
            "name": "Selina", 
            "gender": "female",
            "bithday": "1995-10-18"
        }]
        4:JSON 可以由以上两种形式自由组合而成。可以无限次嵌套，结构清晰，是数据交换的极佳方式。



2:读取 JSON
    1:调用 JSON 库的 loads() 方法将 JSON 文本字符串转为 JSON 对象。
    2: dumps() 将 JSON 对象转换为文本字符串。
    3:获取键值有两种方式，一种是中括号加键名，另一种是通过 get() 方法传入键名，
      推荐使用 get() 方法，这样键名不存在就不会报错，会返回 None
      另外 get() 方法还可以传入第二个参数(默认值)。例如：
      data[0].get('age')
      data[0].get('age', 25)
    4:JSON 字符串的表示要用双引号，否则 loads() 方法会解析失败。
    import json
    str = '''
    [{
        "name": "Bob",
        "gender": "male",
        "phone": "3838"
    },{
        "name": "Jim",
        "gender": "female",
        "phone": "4343"
    }]
    '''
    print(type(str))
    data = json.loads(str)
    print(data, type(data))
    print(data[0]['name'])
    print(data[0].get('name'))

    import json
    with open('data.json', 'r') as file:
        str = file.read()
        data = json.loads(str)
        print(data)



3:输出 JSON
    1:dump() 将对象转换成字符串
    2:dump() 的一个参数 indent 代表缩紧字符个数。
    3:输出中文, file.write(json.dumps(data, indent=2, ensure_ascii=False))
    import json
    data = [{
        'name': 'Bob',
        'gender': 'male',
        'birthday': '1992-10-18'
        }]
    with open('data.json', 'w') as file:
        file.write(json.dumps(data))
        #file.write(json.dumps(data, indent=2))
