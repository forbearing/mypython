1:django目录结构
    1:目录结构
        Message/: 项目文件
        apps/: 应用目录
            apps/message_form/: 应用
        media/: 用户上传
        extra_apps/: 存放第三方源码
        static/: 静态文件
        templates/: HTML 文件
        requirements.txt: 项目依赖的第三方包
        manager.py
    2:配置 app: vi settings.py
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',   
            'message_form.apps.MessageFormConfig',
        ]

2:django 快速配置settings
    1:配置一个 html 页面显示的步骤
        1:配置 urls
        2:配置对应的 views 逻辑
        3:拆分静态(css, js, images) 放入 static, html 放入 template 下
            1:可以放到对应的 app 下面
            2:也可以放入到全局的 template 和 static 目录之下
        4:配置全局的 static 文件访问路径的配置 STATICFILES_DIRS

3:models 数据表设计
4:url 设计
5:views 业务逻辑代码
6:template html 生成
