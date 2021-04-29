#!/usr/bin/env python3

1:概述
    1:在 django 中，视图对 web 请求进行回应
    2:视图就是一个 python 函数，在 views.py 文件中定义

2:定义视图
    vi my_project/my_app/views.py
        from django.http import HttpReponse
        def index(request):
            return HttpReponse("hello python")

3:配置 url
    touch my_project/my_app/urls.py
    vi my_project/my_app/urls.py
