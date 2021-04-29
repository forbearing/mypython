#!/usr/bin/env python3

#pip installl ipy

'''
    1:通过 version 方法来区分 IPv4 和 IPv6
'''
from IPy import IP
print(IP('10.0.0.0/8').version())
print(IP('::1').version())


'''
    2:输出该网段的IP个数及所有 IP 地址清单
'''
from IPy import IP
ip = IP('10.240.0.0/16')
print(ip.len())
# for x in ip:
    # print(x)


'''
    3:IP类几个常见的方法，包括反向解析名称、IP类型、IP转换等。
'''
from IPy import IP
ip = IP('8.8.8.8')
print("反向解析地址格式:", ip.reverseNames())
#print("反向解析地址格式:", ip.reverseName())
print("IP类型:", ip.iptype())
print("转换成整型格式:", ip.int())
print("转换成十六进制格式:", ip.strHex())
print("转换成二进制格式:", ip.strBin())


'''
    4:IP方法也支持网络地址转换，例如根据 IP 与掩码生成网段格式
'''
from IPy import IP
print(IP('192.168.1.0').make_net('255.255.255.0'))
print(IP('192.168.1.0/255.255.255.0', make_net=True))
print(IP('192.168.1.0-192.168.1.255', make_net=True))


'''
    5. 通过 strNormal 方法指定不同 wantprefixlen 参数值以定制不同输出类型的网段。
        wantprefixlen = 0 无返回，如 192.168.1.0
        wantprefixlen = 1 prefix 格式，如 192.168.1.0/24
        wantprefixlen = 2 decimalnetmask 格式，如 192.168.1.0/255.255.255.0
        wantprefixlen = 3 lastIP 格式，如 192.168.1.0-192.168.1.255
'''
from IPy import IP
print(IP('192.168.1.0/24').strNormal(0))
print(IP('192.168.1.0/24').strNormal(1))
print(IP('192.168.1.0/24').strNormal(2))
print(IP('192.168.1.0/24').strNormal(3))
