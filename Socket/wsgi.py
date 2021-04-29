#!/usr/bin/env python3
---
    vi application.py
        def application(environ, start_reponse):
            start_reponse('200 ok', [('Content-Type', 'text/html')])
            return [b'<h1>Hello, web!</h1>']

    vi server.py
        from wsgiref.simple_server import make_server
        from application import application
        # 创建一个服务器，IP地址为空，端口是8000，处理函数是 application
        httpd = make_server('', 8000, application)
        print('Server HTTP on port 8000...')
        # 开始监听 HTTP 请求
        http.server_forever()

