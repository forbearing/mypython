1:CSV, Comma-Separated Values



1:写入
    1:修改分隔符 writer = csv.writer(csvfile, delimiter=' ')
    import csv
    with open('data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)     # 调用 csv 库的 writer() 方法初始化写入对象
        writer.writerow(['id', 'name', 'ag'])
        writer.writerow(['1001', 'Mike', '20'])
        writer.writerow(['1002', 'Bob', '22'])
        writer.writerow(['1003', "jordan", '21'])

    2:调用 writerows() 方法写入多行，此时参数为二维列表
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['1001', 'Mike', '20'],['1002', 'Bob', 22],['1003', 'Jordan', 21]])

    3:爬虫爬取的都是结构化数据，一般我们用字典来表示，在 csv 库中也提供了字典的写入方法
    4:如果想要追加写入的话，可以修改文件的打开莫斯，改为 'a'
    with open('data.csv', 'w') as csvfile:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()            # 先写入头部信息
        writer.writerow({'id':'1001', 'nam':'Mike', 'age':20})
        writer.writerow({'id':'1002', 'name':'Jame', 'age':21})

    5:如果要写入中文内容的话，可能会遇到字符编码的问题。需要给 open() 参数传递编码格式
    with open('data.csv', 'a', encoding='utf-8') as csvfile




2:读取
    import csv
    with open('data.csv','r',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
