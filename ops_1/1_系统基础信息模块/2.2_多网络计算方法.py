#!/usr/bin/env python3

from IPy import IP

'''
    有时候我们需要比较两个网段是否存在包含、重叠等关系，比如同网络不同 prefixlen 会认为是不想等的网段
    比如：10.0.0.0/16 和 10.0.0.0/24，IPy 支持类似于数值型数据的比较，以帮组 IP 对象进行比较
'''

'''
    1: 判断IP地址和网段是否包含于另一个网段中
'''

from IPy import IP
print(IP('192.168.1.100') in IP('192.168.1.0/24'))
print(IP('192.168.2.100') in IP('192.168.1.0/24'))


'''
    2: 判断两个网段是否重叠，采用 IPy 提供的 overlaps 方法
'''
print(IP('192.168.0.0/23').overlaps('192.168.0.0/24'))      # 返回1表示存在重叠，返回0表示不存在重叠
print(IP('192.168.1.0/24').overlaps('192.168.2.0'))
