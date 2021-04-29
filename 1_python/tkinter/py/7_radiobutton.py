#!/usr/bin/env python3

import tkinter

win = tkinter.Tk()
win.titl("tkinter 图形编程")
win.geometry("400x200+200+20")

radio1 = tkinter.Radiobutton(win, text="one", value=1)
radio1.pack()

radio2 = tkinter.Radiobutton(win, text="two", value=2)
radio2.pack()

radio3 = tkinter.Radiobutton(win, text="threee", value=3)
radio3.pack()

win.mainloop()
