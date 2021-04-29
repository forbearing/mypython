1:在 Python2 中,连接 MySQL 的库大多是使用 MySQLdb,但是此库的官方并不支持 Python3,所以
  这里推荐使用的库时 PyMySQL




1:连接数据库
    1:connect() 方法声明一个 MySQL 连接对相关 db.
    2:连接成功后,需要调用 cursor() 方法获得 MySQL 的操作游标,利用游标来执行 SQL 语句
    import pymysql
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print('Database version:', data)
    cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
    db.close()




2:创建表
    import pymysql
    db = pymysql.connect(host='127.0.0.1', user='hyb', password='hyb', 
            port=3306, db='spiders')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS students(id varchar(255) NOT NULLL, \
            name varchar(255) NOT NULL, age INT NOT NULL, PRIMARY KEY(id))'
    cursor.execute(sql)
    db.close()




3:插入数据
    1:需要执行 db 对象的 commit() 方式才可实现数据插入,这个方法才是真正将语句提交到数据库
      执行的方法.对于数据插入,更新,删除操作,都需要调用该方法才能生效.
    2:如果执行失败,则调用 rollback() 执行数据回滚操作,相当于什么也没发生
    3:这里涉及事务的问题,事务机制可以确保数据的一致性,也就是这件事要么发生了,要么没有发生
    import pymysql
    id = '20120001'
    user = 'Bob'
    age = 20
    db = pymysql.connect(host='localhost', user='root', password='123456', 
            port=3306, db='spiders')
    cursor = db.cursor()
    sql = 'INSERT INTO students(id,name,age) values(%s, %s, %s)'
    try:
        cursor.execute(sql, (id, user, age))
        db.commit()
    except:
        db.rollback()
    db.close()
    # sql = 'INSERT INTO students(id, name, age) values('+id+', '+name+','+age+')'
    # 其 values 值没有字符串拼接方式来购招

    4:事务的4个属性:原子性, 一致性, 隔离性, 持久性
        1:原子性(atomicity)
            事务是一个不可分割的工作单元,事务中包括的诸操作要么都做,要么都不做
        2:一致性(consistency)
            事务必须使数据库从一个一致性状态编导另一个一致性状态.一致性与原子性是密切相关的
        3:隔离性(isolation)
            一个事务的执行不能被其他事务干扰,即一个事务内部的操作及使用的数据对并发的其他
            事务时隔离的,并发执行的各个事物之间不能相互干扰
        4:持久性(durability)
            也称永久性(permanence), 指一个事务一旦提交,它对数据库中数据的改变应该时永久的,
            接下来的其他操作或故障不应该对其有任何影响
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    # 这样便可以保持的一致性,这里的 commit() 和 rollback() 方法就为事务的实现提供了支持




4:更新数据
    sql = 'UPDATE students SET age = %s WHERE name = %s'
    try:
        cursor.execute(sql, (25, 'Bob'))
    except:
        db.rollback()
    db.close()



5:删除数据
6:查询数据
    1:fetchone() 方法可以获得结果的第一条数据,返回结果是元组形式.
    2:fetchall() 可以得到结果的所有数据
    sql = 'SELECT * FROM students WHERE age >= 20'
    try:
        cursor.execute(sql)
        print('Count:', cursor.rowcount)
        one = cursor.fetchone()
        print('One:', one)
        results = cursor.fetchall()
        print('Results:' results)
        print('Results Type:', type(results))
        for row in results:
            print(row)
    except:
        print('Error')
