#!/usr/bin/env python3

from view import View
from atm import ATM
import time
import os
import signal
import sys

def ifBank():
    def exitBank(signalnum, frame):
        print("\n真在退出梦想家银行系统 ...")
        time.sleep(1)
        sys.exit(0)
    signal.signal(signal.SIGINT, exitBank)
    signal.signal(signal.SIGTERM, exitBank)
    signal.signal(signal.SIGHUP, exitBank)


def main():

    view = View()
    atm = ATM()
    os.system("clear")
    if view.printAdminView():           # 管理员登录界面
        return -1
    view.adminLogin()                   # 管理员登录验证

    while True:
        os.system("clear")
        view.printSysFunctionView()
        option = input("请输入你的操作: ")
        if option == "1" or option.lower() == "Open":           # 1.开户
            print("正在开户 ...")
            time.sleep(1)
            atm.accountOpen()
            print("开户结束 ...")
            time.sleep(1)
        elif option == "2" or option.lower() == "close":        # 2.销户
            print("正在销户 ...")
            time.sleep(1)
            atm.accountClose()
            print("销户结束 ...")
            time.sleep(1)
        elif option == "3" or option.lower() == "search":       # 3.查询
            print("正在查询 ...")
            time.sleep(1)
            atm.accountSearch()
            print("查询结束 ...")
            time.sleep(1)
        elif option == "4" or option.lower() == "change":       # 4.改密
            print("正在改密 ...")
            time.sleep(1)
            atm.passwdChange()
            print("改密结束 ...")
            time.sleep(1)
        elif option == "5" or option.lower() == "deposit":      # 5.存款
            print("正在存款 ...")
            time.sleep(1)
            atm.moneyDeposit()
            print("存款结束 ...")
            time.sleep(1)
        elif option == "6" or option.lower() == "withdraw":     # 6.取款
            print("正在取款 ...")
            time.sleep(1)
            atm.moneyWithdraw()
            print("取款结束 ...")
            time.sleep(1)
        elif option == "7" or option.lower() == "transfer":     # 7.转账
            print("正在转账 ...")
            time.sleep(1)
            atm.moneyTransfer()
            print("转账结束 ...")
            time.sleep(1)
        elif option == "8" or option.lower() == "recard":       # 8.补卡
            print("正在补卡 ...")
            time.sleep(1)
            atm.accountRecard()
            print("补卡结束 ...")
            time.sleep(1)
        elif option == "9" or option.lower() == "lock":         # 9.锁定
            print("正在锁定 ...")
            time.sleep(1)
            atm.accountLock
            print("锁定结束 ...")
            time.sleep(1)
        elif option == "10" or option.lower() == "unlock":      # 10.解锁
            print("正在解锁 ...")
            time.sleep(1)
            atm.accountUnlock()
            print("解锁结束 ...")
            time.sleep(1)
        else:
            print("输入错误, 请重新输入 ...")
            time.sleep(1)

if __name__ == "__main__":
    ifBank()
    main()
