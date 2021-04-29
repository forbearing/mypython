#!/usr/bin/env python3

class DictDemo:
    def __init__(self, key, value):
        self.dict = {}
        self.dict[key] = value
    def __getitem__(self, key):
        return self.dict[key]
    def __setitem__(self, key, value):
        self.dict[key] = value
    def __len__(self):
        return len(self.dict)

dictDemo = DictDemo('key0', 'value0')
print(dictDemo['key0'])
dictDemo['key1'] = "value1"
print(dictDemo['key1'])
print(len(dictDemo))
