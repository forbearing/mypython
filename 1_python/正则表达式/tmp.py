#!/usr/bin/env python3

# 检查手机号码
def checkPhone(string):
    if len(string) != 11:
        return False

    for i in string:
        if i < "0" or i > "9":
            return False

    if string[0] != "1":
        return False
    elif int(string[1]) > 8:
        return False

    return True

print(checkPhone("13912345678"))
print(checkPhone("139123456781"))
print(checkPhone("139123r5678"))
print(checkPhone("19912345678"))
