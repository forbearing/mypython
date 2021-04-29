#!/usr/bin/env python3
# 点击按钮，输出输入框中的内容

import tkinter

win = tkinter.Tk()
win.title("tkinter 图形编程")
win.geometry("400x200+200+20")


def showInfo():
    print(entry.get())

entry = tkinter.Entry(win)
entry.pack()

button = tkinter.Button(win, text="按钮", command=showInfo)
button.pack()

win.mainloop()

