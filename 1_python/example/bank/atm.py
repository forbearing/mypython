#!/usr/bin/env python3

from card import Card
from user import User
import random
import time

class ATM(object):

    def __init__(self):
        self.users = {}

    def checkPasswd(self, firstPasswd):             # 检查密码是否输入一致
        secondPasswd = input("再次输入密码: ")
        if firstPasswd == secondPasswd:
            return True
        return False

    def randomPasswd(self, length=8):               # 产生随机密码
        passwd = ""
        for i in range(length):
            ty = random.randrange(3)
            if ty == 0:
                ch = chr(random.randrange(ord('A'), ord('Z'+1)))
                passwd += ch
            elif ty == 1:
                ch = chr(random.randrange(ord('a'), ord('z')+1))
                passwd += ch
            else:
                ch = chr(random.randrange(ord('1'), ord('9')+1))
                passwd += ch
        return passwd

    def randomCard(self, length=3):                 #  产生随机卡号
        while True:
            cardStr = random.randrange(100,1000)
            if not self.users.get(cardStr):
                return cardStr



    # 1.开户(open)
    def accountOpen(self):

        name =  input("请输入您的姓名: ")
        idCard = input("请输入您的身份证号码: ")
        phone = input("请输入您的电话号码: ")

        preDeposit  = int(input("请输入预存款金额: "))      # 保存预存款信息
        if  preDeposit < 0:
            print("预存款失败,  开户失败 ...")
            return -1

        firstPasswd = input("请输入您的密码: ")             #  保存密码信息
        if not self.checkPasswd(firstPasswd):
            print("两次输入密码不同, 开户失败")
            return -1

        bankCard = self.randomCard()                        # 生成卡号
        card = Card(bankCard, firstPasswd, preDeposit)
        user = User(name, idCard, phone, card)
        self.users[bankCard] = user
        print("你的卡号为 %s, 请妥善保管, 3秒后关闭" %bankCard)
        time.sleep(3)



    # 2.销户(close)
    def accountClose(self):

        cardNum = input("请输入您的卡号: ")                 # 验证卡号是否存在
        if not self.users.get(cardNum):
            print("该卡号不存在, 查询失败")
            return -1

        if not checkPasswd(users.card.cardPasswd):
            print("密码输入错误, 查询失败")
            return -1

        print("账号: %s  余额: %d" %(self.users.cardID, self.users.card.cardMoney))


    def accountSearch(self):            # 3.查询(search)
        pass
    def passwdChange(self):             # 4.改密(change)
        pass
    def moneyDeposit(self):             # 5.存款(deposit)
        pass
    def moneyWithdraw(self):            # 6.取款(withdraw)
        pass
    def moneyTransfer(self):            # 7.转账(transfer)
        pass
    def accountRecard(self):            # 8.补卡(recard)
        pass
    def accountLock(self):              # 9.锁定(lock)
        pass
    def accountUnlock(self):            # 10.解锁(unlock)
        pass
