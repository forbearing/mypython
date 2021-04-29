#!/usr/bin/env python3

import tkinter

win = tkinter.Tk()
win.title("tkinter 图形编程")


string = '''
Democratic leaders have to work with Trump for several distinct reasons. It is the
right thing to do, for starters. Morally, no alternative exists. The country is in
crisis and Trump is the only president Americans have at the moment—even though he
might want people to inject themselves with disinfectants, even though he is bullying
governors and displaying a self-absorption that is pronounced even for him, even though
he is partly responsible for the disaster the country is experiencing.
'''

# scroll: 创建滚动条
scroll = tkinter.Scrollbar()
text = tkinter.Text(win, width=30, height=10, font="宋体")
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)     # side 放到窗体的哪一侧 fill 填满
text.pack(side=tkinter.LEFT, fill=tkinter.Y)
text.insert(tkinter.INSERT, string)
# 关联 scroll 和 text
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
win.mainloop()
