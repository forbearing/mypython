#!/usr/bin/env python3

django-admin startproject my_project
    # 创建一个 my_project 的工程
python3 manage.py startapp my_app
python3 manage.py runserver


1:区别
    1:django-admin 存放在 Python 的 site-packages/django/bin 目录中，manage.py 存在
      项目工程文件夹里。
    2:django-admin 可以对不同的项目进行设置，而 manage.py 只能对当前工程有效

2:语法
    django-admin <sub_cmd> [options]
    manage.py <sub_cmd> [options]

3:常用子命令
    startproject:       创建一个项目（*）
    startapp:           创建一个app（*）
    runserver：         运行开发服务器（*）
    shell：             进入django shell（*）
    dbshell：           进入django dbshell
    check：             检查django项目完整性
    flush：             清空数据库
    compilemessages：   编译语言文件
    makemessages：      创建语言文件
    makemigrations：    生成数据库同步脚本（*）
    migrate：           同步数据库（*）
    showmigrations：    查看生成的数据库同步脚本（*）
    sqlflush：          查看生成清空数据库的脚本（*）
    sqlmigrate：        查看数据库同步的sql语句（*）
    dumpdata:           导出数据
    loaddata:           导入数据
    diffsettings:       查看你的配置和django默认配置的不同之处
    manage.py           特有的一些子命令：
    createsuperuser:    创建超级管理员（*）
    changepassword:     修改密码（*）
    clearsessions：     清除session
