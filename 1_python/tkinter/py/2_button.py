#!/usr/bin/env python3

import tkinter

def func():
    print("你喜欢我吗")

win = tkinter.Tk()
win.title("tkinter 图形编程")
win.geometry("400x200+200+20")

# button: 创建按钮
#   command: 执行函数
button1 = tkinter.Button(win, text="按钮1", command=func, width=10, height=5)
button1.pack()

button2 = tkinter.Button(win, text="按钮2", 
            command=lambda:print("我喜欢你"), width=10, height=5)
button2.pack()

button3 = tkinter.Button(win, text="退出", 
        command=win.quit, bg="black", fg="white")
button3.pack()

win.mainloop()
