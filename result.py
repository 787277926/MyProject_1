#HTML测试报告
import unittest
from HTMLTestRunner import HTMLTestRunner
#发送邮件功能
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr
from email.header import Header

#====================查找测试报告目录，找到最新生成的测试报告文件======================
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new


# ====================定义发送邮件如需发送邮件需要填写下面信息======================
def send_mail(file_new):
    # 发送邮箱服务器
    smtpserver = ''
    # 发送邮箱用户/密码
    mail_user = '15@163.com'
    mail_password = ''
    # 发送邮箱
    sender = ''
    # 接收邮箱
    receiver = 'lili.geng@pactera.com'

    f = open('D:\\pythontest\\2020-08-07 15_18_29_result.html', 'rb')
    mail_body = f.read()
    f.close()
    # print(mail_body)
    textApart = MIMEText(mail_body, 'html', 'utf-8')

    HTMLFile = 'D:\\pythontest\\2020-08-07 15_18_29_result.html'
    HTMLApart = MIMEApplication(open(HTMLFile, 'rb').read())
    HTMLApart.add_header('Content-Disposition', 'attachment', filename=HTMLFile)

    m = MIMEMultipart()
    m.attach(textApart)
    m.attach(HTMLApart)
    m['From'] = formataddr(["Shelly", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    m['To'] = formataddr(["FK", receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    m['Subject'] = Header('自动化测试报告', 'utf-8')

    try:
        server = smtplib.SMTP(smtpserver)
        server.login(mail_user, mail_password)
        server.sendmail(sender, [receiver], m.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误
