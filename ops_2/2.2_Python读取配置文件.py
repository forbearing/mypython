配置文件格式
    test.ini
        [protocol]
        version = 6;
        [user]
        name = hybfkuf;
        email = admin@admin.admin;
        active = true;
        pi = 3.14159

    test.properties
        com.neo.title=hybfkuf
        com.neo.description=hybfkuf
        # 日志设置
        logging.path=/path/to/file
        # mysql 设置
        spring.datasource.url=jdbc:mysql://192.168.100.11:3306/db_java
        spring.datasource.username=java
        spring.datasource.password=java_password
        spring.datasource.driver-class-name=com.mysql.jdbc.Driver




# ====================================================================================
1:读取 ini 配置文件
    test.ini
         [DEFAULT]
         ServerAliveInterval = 45
         Compression = yes
         CompressionLevel = 9
         ForwardX11 = yes
         [hybfkuf.com]
         User = knight
         [ip.yeyese.club]
         Port = 50022
         ForwardX11 = no

    from configparser import ConfigParser
    cfg = ConfigParser()
    cfg.read('test.ini')
    print(cfg.sections())
    print(cfg.get("hybfkuf.com", "User"))
    print(cfg.getboolean('DEFAULT', 'Compression'))
    print(cfg.getint('ip.yeyese.club', 'Port'))

    # cfg.sections() 用于将配置文件中的每个节段读取出来。
    # cfg.get 用于获取对应节段后的键的value值。
    # cfg.getboolean 用于是否能获取键值的bool返回类型。
    # cfg.getint() 用于获取节段后的键值的整型值

2:写入 ini 配置文件
    # code1: -----------------------------------------------------------------------
    from configparser import ConfigParser
    cfg = ConfigParser()
    cfg.read('test.ini')
    cfg.set('ip.yeyese.club', "IP", "10.0.0.1")
    with open('test.ini', 'w') as f:
        cfg.write(f)

    # code2: -----------------------------------------------------------------------
    from configparser import ConfigParser
    cfg = ConfigParser()
    cfg.read('test.ini')
    cfg.add_section('mysection')                    # 增加节段
    cfg.set('mysection', 'city', 'beijing')         # 删除一个配置项
    with open('test.ini', 'w') as f:
        cfg.write(f)

3:删除 ini 字段
    from configparser import ConfigParser
    cfg = ConfigParser()
    cfg.read('test.ini')
    cfg.remove_section('ip.yeyese.club')
    cfg.remove_option('hybfkuf.com',"user")
    with open('test.ini', 'w') as f:
        cfg.write(f)

4:读取写入 conf 结尾的文件，和操作 ini 配置文件一样




# ====================================================================================
* JSON 在 Python 中分别由 list 和 dict 组成，用于序列化的两个模块
    * json: 用于字符串和 python 数据类型之间进行转换（用的相对较多）
    * pickle: 用于 python 特有的类型和 python 的数据类型之间进行转换
* Json模块提供了四个功能：dumps、dump、loads、load。
* Json 是可以在不同语言之间交换数据的，而 pickle 只在 python 之间使用
* json 只能序列化最基本的数据类型，josn 只能把常用的数据类型序列化(列表、字典 、列表、字符串、数字)，
  比如日期格式、类对象!josn就不行了。而pickle可以 序列化所有的数据类型，包括类，函数都可以序列化

1:读取 Josn
    import json
    with open('test.json', 'r') as f:
        load_res = json.load(f)         # 输出结果为列表
        print(load_res)
        print(type(load_res))



# ====================================================================================

1:读取 yaml
    # pip install pyyaml
    import yaml
    import os

    curPath = os.path.dirname(os.path.realpath(__file__))
    yamlPath = os.path.join(curPath, 'test.yaml')

    with open(yamlPath, 'r', encoding='utf8') as f:
        d = yaml.load(f, Loader=yaml.FullLoader)
        print(d)
        print(d['nb']['user'])
    # d = yaml.load(f, Loader=yaml.FullLoader) 如果不加 Loader=yaml.FullLoader 会抛出警告如下:
    #    YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated,
    # yaml 5.1版本后弃用了yaml.load(file)这个用法，因为觉得很不安全，5.1版本之后就修改了需要指定
    #   Loader，通过默认加载器(FullLoader)禁止执行任意函数
