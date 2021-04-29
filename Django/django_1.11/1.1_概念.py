#!/usr/bin/env python3

1:概述
    1:是一个开放源代码的 Web 应用框架，由 Python 编写。初次发布于 2005年7月，
      并于 2008年9月发布了第一个正式版1.0

2:MVC
    1:一种软件设计典范，用一种业务逻辑、数据、界面显示分离的方法组织代码，将逻辑聚集到
      一个部件里面，在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑。
      MVC 被独特的发展起来用于映射传统的输入、处理和输出功能在一个逻辑的图形化用户界面
      的结构中
    2:核心思想：解藕
    3:编程模式
        Model(模型):
            1:是应用程序用于处理应用程序数据逻辑的部分
            2:通常模型对象负责在数据库中存取数据
        View(视图):
            1:是应用程序处理数据显示的部分
            2:通常视图是依据模型数据创建的
        Controller(控制器):
            1:是应用程序处理用户交互的部分
            2:通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据
    4:优点: 降低各个功能模块之间的耦合性，方便变更，更容易重构代码，最大程度上实现代码的重用

3:MTV
    1:概述：
        本质上于 MVC 模式没有什么差别，也是各组件之间为了保持松耦合关系，只是定义上有些不同
    2:编程模式
        1:Model(模型): 负责业务对象与数据库的对象(ORM)
        2:Template(模版): 负责如何把页面展示给用户
        3:View(视图): 负责业务逻辑，并在适当的时候调用 Model 和 Template
    3:注意
        Django 还有一个 url 分发器，它的作用是将一个个 URL 的页面请求分发给不同的
        View 处理，View 再调用相应的 Model 和 Template

3:项目目录结构
    django-admin startproject my_project
    cd my_project
    python manage.py start_app my_app
    tree my_project

    my_project/
    ├── manage.py
    ├── my_app
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── my_project
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-37.pyc
        │   └── settings.cpython-37.pyc
        ├── settings.py
        ├── urls.py
        └── wsgi.py

        my_project/manage.py:
            一个命令行工具，可以使我们用多种方式对 Django 项目进行交互
        my_project/my_project/__init__.py
            一个空文件，它告诉 Python 这个目录应该被看成一个 Python 包
        my_project/my_project/settings.py
            项目的配置文件
        my_project/my_project/urls.py
            项目的 URL 声明
        my_project/my_project/wsgi.py
            项目与 wsgi 兼容的 Web 服务器入口

        my_project/my_app/admin.py          站点配置
        my_project/my_app/models.py         模型
        my_project/my_app/views.py          视图
