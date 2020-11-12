#coding=utf-8
import unittest,HTMLTestRunner
import Login
import result
from time import sleep,ctime,time,strftime,localtime
from HTMLTestRunner import HTMLTestRunner


# #创建测试套件 无测试报告
# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(Login.loginCase))
# runner = unittest.TextTestRunner() # 实例化
# runner.run(suite)

#加载测试用例到测试套件
#创建测试套件
suite = unittest.TestSuite()
suite.addTest(Login.loginCase('test_login_success'))
suite.addTest(Login.loginCase('test_NoScanEntry_success'))

now = strftime("%Y-%m-%d %H_%M_%S")  # 按照一定格式获取当前时间
fp = open('./' + now + '_result.html', 'wb')  # 定义报告存放路径
runner = HTMLTestRunner(stream=fp,  # 定义测试报告
                        title="Klhealth核心系统测试报告",
                        description='用例执行情况： ')
#创建测试运行程序
runner = unittest.TextTestRunner() #这个要放在后面，不然用例里的print打印不出来
runner.run(suite)
fp.close()  # 关闭报告文件

