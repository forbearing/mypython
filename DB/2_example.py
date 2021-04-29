#!/usr/bin/env python3

import pymysql

conn = pymysql.connect('localhost', 'hybfkuf', 'hybfkuf', 'testdb')
cursor = conn.cursor()
sql = '''INSERT INTO users(name, age) VALUES('zhangshan', 20)'''
sql = "INSERT INTO \
        users(name, age) \
        VALUES('%s', '%s')" %('lisi', 20)
sql = "INSERT INTO users(name, age) VALUES('%s', '%s')" %('wangwu', 22)

try:
    cursor.execute(sql)
    conn.commit()
except:
    print("INSERT INTO ERROR")
    conn.rollback()
finally:
    cursor.close()
    conn.close()


===

effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", 
        [("u1","u1pass","11111"),("u2","u2pass","22222")])
