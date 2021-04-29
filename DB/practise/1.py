#!/usr/bin/env python3

import pymysql

conn = pymysql.connect('localhost', 'hybfkuf', 'hybfkuf', 'testdb')
cursor = conn.cursor()

sql = "SELECT * FROM users WHERE age > %s" %(20)

try:
    cursor.execute(sql)
    res = cursor.fetchall()
    for row in res:
        name = row[0]
        age = row[1]
        print("name: %s age: %s" %(name, age))
except:
    print("Error, unable to fetch data")
finally:
    cursor.close()
    conn.close()
