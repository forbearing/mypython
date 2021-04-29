#!/usr/bin/env python3

import tkinter

win = tkinter.Tk()
win.title("tkinter 图形编程")
win.geometry("800x400+200+20")


# text: 文本控件，用于显示多行文本
#   height: 显示的行数
text = tkinter.Text(win, width=30, height=10, font="苹方")
text.pack()
string='''
If they are successful in their cooperation with Trump, they potentially throw him an
electoral lifeline. But if they fail, the country will suffer.
'''
text.insert(tkinter.INSERT, string)


win.mainloop()
