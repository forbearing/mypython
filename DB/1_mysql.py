#!/usr/bin/env python3

# import mysql.connector

# conn = myysql.connector.connect(user='root', host='localhost', 
        # password='toor', database='mydb')
# cursor = conn.cursor()
# cursor.execute('create table user (id varchar(10)  primary key,
        # name varchar(20))')
# cursor.execute('insert into user (id,name) values(%s,%s)', ['1','Michael'])
# cursor.rowcount

# # 提交事务
# conn.commit()
# cursor.close()

===
报错
    '''cryptography is required for sha256_password or caching_sha2_password'''
    解决：pip install cryptography

    ''' (3719, "'utf8' is currently an alias for the character set UTF8MB3, but will be 
    an alias for UTF8MB4 in a future release. Please consider using UTF8MB4 in order 
    to be unambiguous.") '''
    解决：数据库连接和创建表的的时候的时候，指定 charset 为 utf8mb4




=== 参数列表
    host                数据库服务器地址，默认 localhost
    user                用户名，默认为当前程序运行用户
    password            登录密码，默认为空字符串
    database            默认操作的数据库
    port                数据库端口，默认为 3306
    bind_address        当客户端有多个网络接口时，指定连接到主机的接口。参数可以是主机名或IP地址。
    unix_socket	unix    套接字地址，区别于 host 连接
    read_timeout        读取数据超时时间，单位秒，默认无限制
    write_timeout       写入数据超时时间，单位秒，默认无限制
    charset             数据库编码,需要和数据库的编码方式一致，否则失败
    connect_timeout     连接超时时间，默认 10，最小 1，最大 31536000
    db                  参数 database 的别名
    passwd              参数 password 的别名
    cursorclass         设置默认的游标类型



=== 执行单条 SQL
    1:INSERT、UPDATE、DELETE 等修改数据的语句需手动执行connection.commit()完成对数据修改的提交

    import pymysql

    connection = pymysql.connect(host='localhost', port=3306,
            user='hybfkuf', password='hybfkuf', db='testdb', charset='utf8mb4')

    cursor = connection.cursor()
    cursor.execute('''
            CREATE TABLE if not exists users(
                name varchar(32) NOT NULL,
                age int NOT NULL DEFAULT 0,
                PRIMARY KEY (name)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ''')

    # 插入数据（元祖或列表）
    effect_row = cursor.execute('INSERT INTO users (name, age) VALUES (%s, %s) \
            ON DUPLICATE KEY UPDATE age=18', ('mary', 18))

    # 插入数据（字典）
    info = {'name': 'jonas', 'age': 18}
    #effect_row = cursor.execute('INSERT IGNORE INTO users(name, age) VALUES(%(name)s, %(age)s)', info)
    effect_row = cursor.execute('INSERT INTO users(name, age) VALUES(%(name)s, %(age)s) \
            ON DUPLICATE KEY UPDATE age=18', info)
    connection.commit()
    cursor.close()              # 关闭游标
    connection.close()          # 关闭连接



=== 批量执行 SQL
    import pymysql

    connection = pymysql.connect(host='localhost', port=3306,
            user='hybfkuf', password='hybfkuf', db='testdb', charset='utf8mb4')

    cursor = connection.cursor()
    cursor.execute('''
            CREATE TABLE if not exists users(
                name varchar(32) NOT NULL,
                age int NOT NULL DEFAULT 0,
                PRIMARY KEY (name)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    ''')

    cursor.executemany( 'INSERT INTO users(name, age) VALUES(%s %s) \
            ON DUPLICATE KEY UPDATE age=20',
            [('hyb', 20), ('hybfkuf', 22)])
    connection.commit()



=== 查询数据
    cursor.execute('SELECT * FROM users')           # 执行查询 SQL
    cursor.fetchone()                               # 或去单条数据
    cursor.fetchmany(3)                             # 获取 N 条数据
    cursor.fetchall()                               # 获取所有数据

    cursor.execute('select * from users')
    row_1 = cursor.fetchone()           # 获取剩余结果的第一行数据
    print(row_1)
    row_3 = cursor.fetchmany(3)         # 获取剩余结果前n行数据
    row_3 = cursor.fetchall()           # 获取剩余结果所有数据
    connection.commit()
    cursor.close()
    connection.close()



=== 获取新创建数据自增 ID
    1:可以获取到最新自增的ID，也就是最后插入的一条数据ID
    new_id = cursor.lastrowid
    print(new_id)



=== 移动游标
    1:所有的数据查询操作均基于游标，我们可以通过cursor.scroll(num, mode)控制游标的位置
    cursor.scroll(1, mode='relative')               # 相对当前位置移动
    cursor.scroll(2, mode='absolute')               # 相对绝对位置移动



=== 设置游标类型
    1:查询时，默认返回的数据类型是为元祖，可以自定义设置返回类型，支持5种游标类型
    2:无缓冲游标类型，适用于数据量很大，一次性返回太慢，或者服务端带宽较小时
    Cursor:             默认，元祖类型
    DictCursor          字典类型
    DictCursorMixin     支持自定义的游标类型，需先自定义才可使用
    SSCursor            无缓冲元组类型
    SSDictCursor        无缓冲字典类型

    # 创建连接时，通过 cursorclass 参数指定类型
    connection = pymysql.connect(host='localhost', user='root', 
            password='toor', db='demo', charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    # 也可以在创建游标时指定类型
    cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)



=== 事务处理
    开启事务 connection.begin()
    提交修改 connection.commit()
    回滚事务 connection.rollback()
    
    === 调用无参存储过程
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.callproc('p2')           # 等价于cursor.execute("call p2()")
    row_1 = cursor.fetchone()
    print(row_1)
    conn.commit()
    cursor.close()
    conn.close()
    
    === 调用有参存储过程
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.callproc('p1', args=(1, 22, 3, 4))
    cursor.execute("select @p1,@_p1_1,@_p1_2,@_p1_3")
    row_1 = cursor.fetchone()
    print row_1
    conn.commit()
    cursor.close()
    conn.close()



=== 上下文管理
    1:在 python 的文件操作中支持上下文管理，在操作数据库的时候也可以使用

    import pymysql
    config = {
            "host": "127.0.0.1",
            "user": "hybfkuf",
            "password": "hybfkuf",
            "database": "testdb"
            }
    db = pymysql.connect(**config)
    with db.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM userinfo"
        cursor.execute(sql)
        res = cursor.fetchone()
        print(res)
        cursor.close()
    db.close()
