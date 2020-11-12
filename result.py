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

