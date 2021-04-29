#!/usr/bin/env python3

import time

class View():
    admin = "1"
    passwd = "1"

    def printAdminView(self):
        print("*********************************************************************")
        print("*                                                                   *")
        print("*                                                                   *")
        print("*                                                                   *")
        print("*                                                                   *")
        print("*                        欢迎登录梦想家银行                         *")
        print("*                                                                   *")
        print("*                                                                   *")
        print("*                                                                   *")
        print("*                                                                   *")
        print("*********************************************************************")

    def printSysFunctionView(self):
        print("*********************************************************************")
        print("*                                                                   *")
        print("*          1.开户(Open)                  2.销户(close)              *")
        print("*                                                                   *")
        print("*          3.查询(search)                4.改密(change)             *")
        print("*                                                                   *")
        print("*          5.存款(deposit)               6.取款(withdraw)           *")
        print("*                                                                   *")
        print("*          7.转账(transfer)              8.补卡(recard)             *")
        print("*                                                                   *")
        print("*          9.锁定(lock)                  10.解锁(unlock)            *")
        print("*                                                                   *")
        print("*********************************************************************")

    def adminLogin(self):
        inputAdmin = input("请输入管理员账号: ")
        inputPasswd = input("请输入管理员密码: ")
        if inputAdmin != self.admin:
            print("账号或密码有误! ")
            return -1
        if inputPasswd != self.passwd:
            print("账号或密码有误! ")
            return -1
        print("管理员登录成功, 请稍后 ...... ")
        time.sleep(2)
        return 0
