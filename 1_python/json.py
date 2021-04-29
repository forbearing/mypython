#!/usr/bin/env python3
'''
概念：一种保存数据的格式
作用：通常将 json 称为轻量级的传输方式
'''

===
import json
# Python 字典转换成 Json 对象
data = {
        'name': 'hybfkuf',
        'age': 24,
        'gender': 'm'
        }

json_str = json.dumps(data)
print("python 原始数据:", data)
print("JSON 对象:", json_str)

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)
# 读取 JSON 数据
with open('data.json', 'r') as f:
    json.load(f)
