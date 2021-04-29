#!/usr/bin/env python3


'''
一个简单的图形界面，还没有功能
'''
# from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit
# from PySide2.QtWidgets import QMessageBox

# def handlerCalc():
    # info = textEdit.toPlainText()

    # # 薪资 20k 以上的人员名单
    # salary_above_20k = ''
    # salary_below_20k = ''
    # for line in info.splitlines():
        # if not line.strip():
            # continue;
        # parts = line.split(' ')
        # # 去掉列表中的空字符串内容
        # parts = [p for p in parts if p]
        # name,salary,age = parts
        # if int(salary) >= 20000:
            # salary_above_20k += name + '\n'
        # else:
            # salary_below_20k += name + '\n'
    # QMessageBox.about(window,
            # '统计结果',
            # f'''薪资20000 以上的有：\n{salary_above_20k}
              # \n薪资20000 以下的有：\n{salary_below_20k}''')

# app = QApplication([])

# window = QMainWindow()
# window.resize(500, 400)
# window.move(300, 310)
# window.setWindowTitle('薪资统计')

# textEdit = QPlainTextEdit(window)
# textEdit.setPlaceholderText("请输入薪资表")
# textEdit.move(10, 25)
# textEdit.resize(300, 350)

# button = QPushButton('统计', window)
# button.move(380,80)
# button.clicked.connect(handlerCalc)

# window.show()
# app.exec_()



'''
封装到类
'''

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox

class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500,400)
        self.window.move(300,300)
        self.window.setWindowTitle('薪资统计')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入薪资要求")
        self.textEdit.move(10,25)
        self.textEdit.resize(300,350)

        self.button = QPushButton('统计', self.window)
        self.button.move(380, 80)

        self.button.clicked.connect(self.handleCalc)


    def handleCalc(self):
        info = self.textEdit.toPlainText()

        # 薪资 2000 以上和以下的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():      # 处理每一行内容
            if not line.strip():            # 如果有空行，直接跳过处理
                continue
            parts = line.split(' ')
            parts = [p for p in parts if p] # 处理掉列表中的空字符
            name, salary, age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.window,
                '统计结果',
                 f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}''')
app = QApplication()
stats = Stats()
stats.window.show()
app.exec_()
