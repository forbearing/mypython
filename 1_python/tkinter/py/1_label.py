#!/usr/bin/env python3

import tkinter

win = tkinter.Tk()
# win.title("tkinter 图形编程")
# win.geometry("400x200+200+20")

# Label: 标签控件，可以显示文本
#   text: 显示的文本内容
#   bg: 背景色
#   fg: 前景色
#   font: 字体
#   width: 窗口宽度
#   wraplength: 指定 text 文本中多宽进行换行
#   justify: 设置 text 文本换行后的对齐方式
#   anchor: text 位置, n, ne, e, se, s, sw, w, nw, or center
# labe.pack 显示出窗口
label = tkinter.Label(win, text="hello python", bg="blue", fg="red", 
        font=("宋体", 20), width=40, height=20, wraplength=100,
        justify="left", anchor="ne")
label.pack()


win.mainloop()
