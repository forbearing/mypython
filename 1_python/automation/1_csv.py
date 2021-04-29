1:写入
    ---
    import csv
    with open('data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'name', 'age'])
        writer.writerow(['1001', 'Mike', 20])
        writer.writerow(['1002', 'Bob', 22])
        writer.writerow(['1003', 'Jordan', 21])

    ---
    # 修改行与行之间的分隔符，可以传入 delimiter 参数
    import csv
    with open('data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerow(['id', 'name', 'age'])
        writer.writerow(['1001', 'Mike', 20])
        writer.writerow(['1002', 'Bob', 22])
        writer.writerow(['1003', 'Jordan', 21])

    ---
    # writerow 方法可以同时写入多行
    with open('data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'name', 'age'])
        writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])

    ---
    # 1:一般情况下，怕虫爬去的都是结构化数据，我们一般用字典来表示，在 csv 库中提供了
    #   字典的写入方式
    # 2:先定义3个字段，用 fieldnames 表示，然后将其传给 DictWriter 来初始化一个字典对象
    #   接着调用 writeheader() 方法来写入头信息，然后再调用 writerow 方法来传入相应字典
    #   即可。最终写入的结果完全相同
    import csv
    with open('data.csv', 'w') as csvfile:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        write.writeheader()
        writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
        writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
        writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

    ---
    # 如果写入中文，会遇到编码问题，需要指定编码格式
    import csv
    with open('data.csv', 'a', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'id': '10005', 'name': '王伟', 'age': 22})



2:读取

    ---
    # 如果 csv 文件中包含中文的话，需要指定文件编码
    import csv
    with open('data.csv', 'r', encoding='utf-8')  as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

