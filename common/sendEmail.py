# -*- coding: UTF-8 -*-

import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )

sender = '214941133@qq.com'
receivers = ['314105429@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"
mail_user = "214941133@qq.com"
mail_pass = "glyuoltmezckcbeb"



def get_report():
    report_path = PATH("../report/")
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(report_path+"/"+fn))
    file_new = os.path.join(report_path, lists[-1])
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    return mail_body

def send_email():

    mail = get_report()
    message = MIMEText(mail, 'html', 'utf-8')
    message['From'] = Header("爱学习的圈圈", 'utf-8')
    # message['To'] = Header("圈圈小号", 'utf-8')
    message['Subject'] = Header('UI自动化测试报告', 'utf-8')


    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(mail_user, mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, receivers, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__=='__main__':

    get_report()
    send_email()




