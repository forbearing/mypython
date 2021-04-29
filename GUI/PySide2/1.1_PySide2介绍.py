    from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit

    app = QApplication([])

    window = QMainWindow()
    window.resize(500, 400)
    window.move(300, 310)
    window.setWindowTitle('薪资统计')

    textEdit = QPlainTextEdit(window)
    textEdit.setPlaceholderText("请输入薪资表")
    textEdit.move(10, 25)
    textEdit.resize(300, 350)

    button = QPushButton('统计', window)
    button.move(380,80)

    window.show()
    app.exec_()

1:概述
    1:QApplication 提供了整个图形界面的底层管理功能：初始化、程序入口参数的处理、
      用户事件（对界面的点击、输入、拖拽）分发给各个对应的控件，等等。
    2:必须在任何控件对象创建前，创建它
    3:QMainWindow：主窗口、QPlainTextEdit：文本框、QPushButton：按钮，他们都是
      控件基类 QWidge 的子类
    4:要在界面上创建一个控件，就需要在程序代码中创建这个空间对应类的一个实例对象
    5:在 Qt 系统中，控件（widget）是层层嵌套的，除了最顶层的控件，其他的控件都有父控件
    6:QPlainTextEdit、QPushButton 实例化时都有一个参数 Window
        QPlainTextEdit(window)
        QPushButton("统计", window)
        就是指定它的父控件对象是 window 对应的 QMainWindow 窗口
    7:控件对象的 move 方法决定了这个控件显示的位置
        1:window.move(300, 310) 就决定了 主窗口的 左上角坐标在 相对屏幕的左上角
          的X横坐标300像素, Y纵坐标310像素这个位置
        2:textEdit.move(10,25) 就决定了文本框的 左上角坐标在 相对父窗口的左上角
          的X横坐标10像素, Y纵坐标25像素这个位置
    8:控件对象的 resize 方法决定了这个控件显示的大小
        1:window.resize(500, 400) 就决定了 主窗口的 宽度为500像素，高度为400像素。
#        2:textEdit.resize(300,350) 就决定了文本框的 宽度为300像素，高度为350像素
    9:放在主窗口的控件，要能全部显示在界面上， 必须加上下面这行代码
        windows.show()
    10:app.exec_() 进入QApplication的事件处理循环，接收用户的输入事件（），
      并且分配给相应的对象去处理

2:Qt Designer
    pip3 install pyside2 安装完后，有如下几个程序
        pyside2-designer        # 窗口设计
        pyside2-uic             # 根据窗口设计生成 python 代码
        pyside-rcc              # 根据窗口设计生成 c++ 代码
    单独安装 uic
        pip3 install  pyqode-uic


3:发布程序
    pip3 install pyinstaller
    pyinstaller main.py --noconsole --hidden-import PySide2
