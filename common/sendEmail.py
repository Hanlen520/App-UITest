# coding=utf-8

import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from common.readConfig import Readconfig
from common.logs import log

PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )

log = log()
conf = Readconfig()
sender = conf.getemailValue('sender')
receiver = conf.getemailValue('receiver')
mail_host = conf.getemailValue('mail_host')
mail_user = conf.getemailValue('mail_user')
mail_pass = conf.getemailValue('mail_pass')


def get_mail():

    report_path = PATH("../report/")
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(report_path+"/"+fn))
    report = os.path.join(report_path, lists[-1])

    file = open(report, 'rb')
    mail_body = file.read()
    file.close()

    return mail_body

def send_email():

    mail = get_mail()
    message = MIMEText(mail, 'html', 'utf-8')
    message['From'] = Header("爱学习的圈圈", 'utf-8')
    # message['To'] = Header("圈圈", 'utf-8')
    message['Subject'] = Header('UI自动化测试报告', 'utf-8')

    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人第三方SMTP服务器，端口是465
        server.login(mail_user, mail_pass)
        server.sendmail(sender, receiver, message.as_string())
        server.quit()
        log.info('邮件发送成功')
        # print("邮件发送成功")
    except smtplib.SMTPException:
        log.error('邮件发送失败')
        # print("Error: 无法发送邮件")


if __name__ == '__main__':

    get_mail()
    send_email()




