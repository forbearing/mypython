#!/usr/bin/env python3

import tkinter
win = tkinter.Tk()
win.title("tkinter 图形编程")
win.geometry("400x200+200+20")


# entry: 输入控件,用于显示简单的文本内容
#   show="*"
e = tkinter.Variable()      # 绑定变量
entry = tkinter.Entry(win, textvariable=e)
entry.pack()

# e 就代表输入框这个对象
e.set("hello python")           # 设置值
print(e.get())                  # 取值
print(entry.get())              # 取值


win.mainloop()
