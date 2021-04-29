目录
    1:Python 已经有了哪些 GUI 框架
    2:GUI 框架的显示效果，运行平台
    3:GUI 框架的学习成本比较
    4:GUI 框架的开发效率比较
    5:选定 GUI 框架，制定学习计划

1:Python GUI 框架介绍
    Tkinter
        1:Python 内嵌的 gui 环境，使用 TCL 实现。Python IDLE 由 Tkinter 实现
        2:历史悠久，perl 中有对应的 perlTk。Python 标准安装包中包含 Tkinter，易学易用，
          方便创建简单 GUI
        3:跨平台
        4:布局全靠代码实现，15种常见部件，效果简陋
    Wxpython
        1:跨平台，由 C++ 编写
        2:Python 的扩展模块，使用前需要安装
        3:遵循 LGPL 协议，自由软件，商用许可
        4:文档少，遇到问题不容易解决
        5:代码布局控件，不直观
    Pygtk
        1:Python 对 GTK+GUI/库的封装
        2:Python 的扩展模块，使用前需要安装
        3:Gnome 下应用多
        4:GTK 在 Windows 下兼容性会有一定问题
    Pyqt
        1:Python 对 QT 的包装，QT 源码为 C++
        2:跨平台性好，本地显示效果
        3:Pyqt 与 QT 的函数接口一致，由于 QT 开发文档丰富，间接导致 pyqt 的开发文档
          也比较丰富
        4:控件丰富，函数/方法多，拖拽布局
        5:方便打包成二进制文件
        6:GPL 协议，商业程序需要购买商业版授权
    Pyside
        1:Python 对 QT 的封装
        2:扩展模块，使用前需要安装
        3:跨平台特性好
        4:与 pyqt 的 API 一致
        5:诺基亚的亲儿子
        6:LGPL 协议，新软件可以是私有的而不需要是自由软件
    Kivy
        1:使用 python 和 cython 编写，100% 开源免费
        2:针对多点触摸应用
        3:全平台支持（Linux、Widnows、Mac OS X、Android、iOS、Raspberry）
        4:布局使用专用语言 kivy language，代码布局，GUI 布局环境尚不成熟
        5:中文支持差

2:为什么使用 Pyqt
    1:API 与 QT 一致，学习 PyQT，可以等效于学会了 QT，一劳多得
    2:文档丰富，遇到问题不用憋很久
    3:学习成本低
    4:开发迅速，Qt designer 实现 GUI 拖拽布局，所见即所得
    5:学习经验容易迁移到 pyside，开发商业应用
    6:方便打包发布软件
