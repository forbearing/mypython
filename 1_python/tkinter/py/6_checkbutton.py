#!/usr/bin/env python3

import tkinter
# checkbutton: 多选框控件

win = tkinter.Tk()
win.title("tkinter 图形编程")
win.geometry("400x400+200+20")


def update():
    message = ""
    if hobby1.get() == True:
        message += "money\n"
    if hobby2.get() == True:
        message += "power\n"
    if hobby3.get() == True:
        message += "person\n"
    text.delete(0.0, tkinter.END)           # 清空 text 中所有内容
    text.insert(tkinter.INSERT, message)

hobby1 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win, text="money", variable=hobby1, command=update)
check1.pack()

hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win, text="power", variable=hobby2, command=update)
check2.pack()

hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win, text="person", variable=hobby3, command=update)
check3.pack()

text = tkinter.Text(win, width=50, height=5)
text.pack()


win.mainloop()

