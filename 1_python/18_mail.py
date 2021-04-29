#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText

smtpServer = "smtp.163.com"
sender = "fredjoseph863@163.com"
passwd = "abc123.com"

message = "明天有个会议"
msg = MIMEText(message)
msg["Subject"] = "会议通知"
msg["From"] = sender

mailServer = smtplib.SMTP(smtpServer, 25)
mailServer.login(sender, passwd)
mailServer.sendmail(sender,
        ["fredjoseph863@163.com", "fredjoseph863@gmail.com"], msg.as_string)
mailServer.quit()
