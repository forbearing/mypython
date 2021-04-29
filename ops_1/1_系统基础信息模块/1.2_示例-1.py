#!/usr/bin/env python3


loopTime = 1

import psutil
import re
propertyList = dir(psutil)
pList = []
fList = []

for x in propertyList:
    if(re.match(r'[a-zA-Z]{1,100}$', x)):
        pList.append(x)
    else:
        fList.append(x)

# print("psutil属性: ", pList, "\n\n")
# print("psutil方法: ", fList)


cpuLogical = psutil.cpu_count()
'''
    1. 获取 CPU 信息
'''
print("逻辑CPU数量: ", cpuLogical)
cpuPhysical = psutil.cpu_count(logical=False)
print("物理CPU数量: ", cpuPhysical)
for x in range(loopTime):
    cpuPercent = psutil.cpu_percent(interval=1, percpu=False)
    print("CPU使用率: ", cpuPercent)
for x in range(loopTime):
    cpuTime = psutil.cpu_times_percent(interval=1 )
    print("CPU时间:", "User:", cpuTime.user, "System:", cpuTime.system, "Idle:", cpuTime.idle)
print("\n")


'''
    2. 获取内存信息
'''

memory = psutil.virtual_memory()
swap = psutil.swap_memory()
print("内存信息:","percent:", memory.percent, "total:", memory.total, \
        "used:", memory.used, "free:", memory.free, "available:", memory.available)
print("swap信息:", "percent:", swap.percent, "total:", swap.total, \
        "used:", swap.used, "free:", swap.free)
print("\n")


'''
    3. 获取磁盘信息
'''
diskPartitions = psutil.disk_partitions()
print("磁盘分区信息:")
for partition in diskPartitions:
    if re.match(r'(\/dev\/sd|\/dev\/vd|\/dev\/disk)', partition[0]):
        print("\t",partition)

print("磁盘信息:")
for partition in diskPartitions:
    if re.match(r'(\/dev\/sd|\/dev\/vd|\/dev\/disk)', partition[0]):
        diskUsage = psutil.disk_usage(partition[0])
        print("\t", partition[0], "percent:", diskUsage.percent, "total:", diskUsage.total, \
                "used:", diskUsage.used, "free:", diskUsage.free)
# diskUsage = psutil.disk_usage('/')
# print("磁盘根目录信息:", "percent:", diskUsage.percent, "total:", diskUsage.total, \
        # "used:", diskUsage.used, "free:", diskUsage.free)
print("\n")


'''
    4. 获取网络信息
'''
netCounters = psutil.net_io_counters()
# 网络数据包信息
print("网络数据包信息:")
print("\t", "Bytes Sent:", netCounters.bytes_sent, "Bytes Recv:", netCounters.bytes_recv, "\n"\
        "\t", "Packets Sent:", netCounters.packets_sent, "Packets Recv:", netCounters.packets_recv, "\n"\
        "\t", "Error In:", netCounters.errin, "Error Out:", netCounters.errout, "\n"\
        "\t", "Drop In:", netCounters.dropin, "Drop Out:", netCounters.dropout)

# 网卡信息
netIfaddr = psutil.net_if_addrs()
for key,value in netIfaddr.items():
    if re.match(r'^(eth|en)', key) and re.match(r'^[0-9]{3}', value[0].address):
        print("网卡:", key, "IP地址:", value[0].address, "子网掩码:", value[0].netmask)
netStats = psutil.net_if_stats()

# 网卡状态
print("网卡状态:")
for key,value in netStats.items():
    print("\t", key, "speed:", value.speed, "mtu:", value.mtu)
print("\n")

# 网络连接状态
print("网络连接状态:")
netConnections = psutil.net_connections()
for connection in netConnections:
    print("\t", "local", connection.laddr, "remote:", connection.raddr, "status:", connection.status, "pid:", connection.pid)

