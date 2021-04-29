1:概述
    1:利用 urllib 的 robotparser 模块，我们可以实现网站 Robots 协议的分析
    2:爬虫名称
        BaiduSpider
        Googlebot
        360Spider
        YodaoBot
        ia_archiver     www.alexa.cn
        Scooter         www.altavista.com




1:robotparser
    1:该模块提供了一个类 RobotFileParser, 它可以根据某网站的 robots.txt 文件来判断一个爬虫是否
      权限来爬取这个网页

    urllib.robotparser.RobotFileParser(url='')

    类方法
    set_url()
        用来设置 robots.txt 文件的链接。如果在创建 RobotFileParser 对象时传入了链接，那么就
        不需要再使用这个方法设置饿了
    read()
        读取 robots.txt 文件并进行分析。注意，这个方法执行一个读取和分析操作，如果不调用这个方法，
        接下来的判断都会为 False，所以一定要记得调用这个方法。这个方法不会返回任何内容，
    parse()
        用来解析 robots.txt 文件，传入的参数是 robots.txt 某行的内容，它会按照 robots.txt 的语法
        规则来分析这些内容
    can_fetch()
        该方法传入两个参数，第一个是 User-agent, 第二个是要抓取的 URL。返回的内容是该搜索引擎是否
        可以抓取这个 URL，返回结果是 True 和 False
    mtime()
        返回的是上次抓取和分析 robots.txt 的时间，者对于长时间分析和抓取的搜索爬虫是很有必要的，
        你可能需要定期检查来抓取最新的 robots.txt
    modified()
        它同样对长时间分析和抓取的搜索爬虫很有帮助，将当前时间设置为上次抓取和分析 robots.txt 时间

    from urllib.robotparser import RobotFileParser
    rp = RobotFileParser()
    rp.set_url('http://www.jianshu.com/robots.txt')
    print(rp.can_fetch('*',’ http://www.jianshu.com/p/b67554025d7d’))

    from urllib.robotparser import RobotFileParser
    from urllib.request import urlopen
    rp = RobotFileParser()
    rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
    print(rp.can_fetch('*',’ http://www.jianshu.com/p/b67554025d7d’))
