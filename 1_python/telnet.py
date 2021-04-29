#!/usr/bin/env python3

---
# windows 平台下的代码
import telnetlib

def telnetDoSomethingg(ip, user, password, command):
    try:
        telnet = telnetlib.Telnet(ip)           # 连接服务器 
        telnet.set_debuglevel(2)                # 设置调试级别

        rt = telnet.read_until("Login username:".encode("utf-8"))   # 输入用户名信息
        telnet.write((user+"\r\n").encode("utf-8"))                 # 写入 用户名

        rt = telnet.read_until("Login password:".encode("utf-8"))   # 验证密码
        telnet.write((password+"\r\n").encode("utf-8"))

        rt = telnet.read_until("Domain name:".encode("utf-8"))      # 验证ip
        telnet.write((ip+"\r\n").encode("utf-8"))

        rt = telnet.read_until(">".encode("utf-8"))                 # 登录成功
        telnet.write((command+"\r\n").encode("utf-8"))              # 执行命令

        # 如果命令成功,会继续读到 ">"
        rt = telnet.read_until(">".encode("utf-8"))
        telnet.close()                                              # 断开连接
        return True
    except:
        return False

if __name__  == "__main__":
    ip = "192.168.10.10"
    user = "administrator"
    password = "admin"
    command = "tasklist"
    if telnetDoSomethingg(ip, user, password, command):
        print("telnet 执行成功")
    else:
        print("telnet 执行失败")
