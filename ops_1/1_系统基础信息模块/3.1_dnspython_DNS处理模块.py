#!/usr/bin/env python3

'''
    pip3 install dnspython

    dnspython 模块提供了大量的 DNS 处理方法，最常用的是域名查询。dnspython 提供了一个 
    DNS 解析器类 resolver，使用它的 query 方法来实现域名的查询功能。
    query(self, qname, rdtype=1, rdclass=1, tcp=False, source=None, raise_on_no_answer=True, source_port=0)
        qname 是要查询的域名
        rdtype 参数用来指定 RR 资源的类型
            A、MX、CNAME、NS、PTR、SOA
        rdclass 参数用于指定网络类型，可选 IN、CH、HS。IN 为默认，使用最为广泛
        tcp 参数用于指定查询是否启用 TCP 协议，默认为 False，不启用
        source 和 source_port 参数作为指定查询源地址与端口。
        raise_on_no_answer 参数用于指定当前查询无应答时是否触发异常
'''


'''
    1. 常用解析类型
'''
import dns.resolver

domain = 'www.baidu.com'
#domain = input('please input an domain: ')

A = dns.resolver.resolve(domain, 'A')                   # 查询A记录
print("A 记录:")
for i in A.response.answer:                             # 通过 response.answer 方法获取查询回应信息
    # print(j)
    for j in i.items:
        print(j)
print('\n')

CNAME = dns.resolver.resolve(domain, 'CNAME')
print("CNAME 记录:")
for i in CNAME.response.answer:
    #print(i)
    for j in i.items:
        print(j)
print('\n')

domain = 'baidu.com'
MX = dns.resolver.resolve(domain, 'MX')
print("MX 记录")
for i in MX:
    print("MX preference:", i.preference, "mail exchanger:", i.exchange)
print('\n')

NS = dns.resolver.resolve(domain, 'NS')
print("NS 记录:")
for i in NS.response.answer:
    #print(i)
    for j in i.items:
        print(j)
