1:概念
    1:递归调用：一个函数，调用了自身
    2:递归函数：一个会调用自身的函数
    3:凡事 循环能干的事，递归都能干
    4:写递归函数的方法
        1:写出临界条件
        2:找出这一次和上一次的关系
        3:假设当前函数已经能用，调用自身计算上一次的结果。再求出这一次的结果


---
def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n-1) + n

--- 递归遍历目录
    import os
    def getAllDir(path, sp=""):
        fileList = os.listdir(path)
        sp += "  "
        for fileName in fileList:
            fileAbsPath = os.path.join(path, fileName)
            if os.path.isdir(fileAbsPath):
                print(sp + "dir:  " %fileName)
                getAllDir(fileAbsPath, sp)
            else:
                print(sp + "file: " %fileName)
