#!/usr/bin/env python3

# try:
    # f = open('/tmp/passwd', 'r')
    # print(f.read())
# finally:
    # if f:
        # f.close()

# with open('/tmp/passwd', 'ra') as f:
    # f.write('Hello World')

import pickle

# d = dict(name='hybfkuf', age=22, score=88)
# with open('/tmp/dump.txt', 'wb') as f:
    # pickle.dump(d, f)
    # f.close()
# with open('/tmp/dump.txt', 'rb') as f:
    # d = pickle.load(f)
    # print(d)

import json

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
d = json.loads(json_str)
print(d)
print(type(d))
