https://my.oschina.net/wangyunlong/blog/3075265

1:设计表结构
    班级表结构：
        表名：grade
        字段：班级名称(gname)、成立时间(gdate)、女生总数(ggirlnum)、男生总数(gboynum)、是否删除(isDelete)
    学生表结构：
        表名：grade
        字段：名字(sname)、性别(sgender)、年龄(sage)、简介(sintro)、所属班级(sgrade)、是否删除(isDelete)


2:配置数据库
    1:默认使用的是 SQLite
    2:数据库设置
        vi my_project/my_project/settings.py
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'HOST': 'localhost',
                    'PORT': 3306
                    'NAME': 'mydb',
                    'USER': 'root',
                    'PASSWORD': 'toor',
                }
            }
    3:配置 MySQL
        pip3 install PyMySQL
        vi my_project/my_project/__init__.py
            import pymysql
            pymysql.install_as_MySQLdb


3:创建应用
    1:在一个项目中可以创建多个应用，每个应用进行一种业务处理
    2:python manage.py startapp my_app
    3:激活应用
        INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'my_app'
        ]


4:定义模型
    1:有一个数据表，就对应一个模型
    2:在 models.py 文件中定义模型
        # 模型类要继承 models.Model 类
        from django.db import models
        class Grades(models.Model):
            gname = models.CharField(max_length=20)
            gdate = models.DateTimeField()
            ggirlnum = models.IntegerField()
            gboynum = models.IntegerField()
            isDelete = models.BooleanField(default=False)
        class Students(models.Model):
            sname = models.CharField(max_length=20)
            sgender = models.BooleanField(default=True)
            sage = models.IntegerField()
            sintro = models.CharField(max_length=20)
            isDelete = models.BooleanField(default=False)
            #sgrade = models.ForeignKey("Grades")        # 关联外键
            sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)        # 关联外键

    3:说明
        1:不需要自定义主键，在生成时自动添加，并且值为自动添加。


5:在数据库中生成数据表
    1:生成迁移文件
        python manage.py makemigrations
        在 my_app/migration 目录下生成一个迁移文件，此时数据库中还没有生成数据表
    2:执行迁移
        python manage.py migrate
        相当于执行 SQL 语句


6:测试数据操作
    1:进入 shell，引入包
        python3 manage.py shell
        from my_app.models import Grades, Students
        froom django.utils import timezone
        from datetime import *
    2:查询所有数据
        Grades.objects.all()
    3:添加数据
        >>>
        grade1 = Grades()
        grade1.gname = 'python04'
        grade1.gdate = datetime(year=2017, month=7, day=17)
        grade1.ggirlnum = 3
        grade1.gboynum = 70
        grade1.isDelete = False
        grade1.save()
        Grades.objects.all()
        >>>
        grade2 = Grades()
        ...
        grade2.save()
    4:查看某个对象
        Grades.objects.get(pk=2)
    5:修改数据
        grade2.gboynum = 60
        grade2.save()
    6:删除数据
        grade2.delete()     # 物理删除，数据库中表的数据被删除
    7:关联对象
        >>>
        stu = Students()
        stu.sname = 'hyb'
        stu.sgender = False
        stu.sage = 20
        stu.sintro = 'i am hyb'
        stu.sgrade = grade1
        stu.save()
        grade1.students_set.all()       # 获取所有学生
        stu3 = grade1.students_set.create(sname='hybfkuf', sgender=True,
                sintro='i am hybfkuf', sage=24, isDelete=False)


7:启动服务器
    python3 manage.py runserver ip:port
        # 这是一个纯 Python 写的轻量级 web 服务器，仅仅在开发测试中使用


8:Admin 站点管理
    1:概述
        1:内容发布：负责添加、修改、删除内容
        2:公告访问
    2:配置 Admin 应用
        vi settings.py
            INSTALLED_APPS = [
                    'django.contrib.admin'
                    ]
    3:创建管理员用户
        python3 manage.py createsuperuser
    4:进入管理员后台
        127.0.0.1:8000/admin
    5:管理数据表 vi admin.py
        # Register your models
        #from models import Grades,Students          # 失效
        from my_app.models import Grades,Students
        # Register
        admin.site.register(Grades)
        admin.site.register(Students)
    6:自定义管理页面 vi admin.py
        class GradesAdmin(admin.ModelAdmin):
            # 列表页属性
            list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
            list_filter = ['gname']
            search_fields = ['gname']
            list_per_page = 5
            # 添加、修正页属性
            fields = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'pk', 'isDelete']
            fieldsets = []
        admin.site.register(Grades, GradesAdmin)
    7:字段说明
        1:列表页属性
            list_display        显示字段
            list_filter         过滤字段
            search_fields       搜索字段
            list_per_page       分页
        2:添加、修改页属性
            fields              属性的先后顺序
            fieldsets           给属性分组，不能和 fields 同时使用
