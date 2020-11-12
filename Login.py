#coding=utf-8
from selenium import webdriver
from time import sleep,ctime,time,strftime,localtime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv

#HTML测试报告
import unittest

class loginCase(unittest.TestCase):  # 继承 unittest.TestCase
    @classmethod
    def setUpClass(self):
        print("Test Class Start ----->")
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(10)
        self.base_url = "http://10.1.82.39:7001/ui/indexlis.jsp"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):  # 清理的过程
        print("Test Class End ----->")
        sleep(2)
        print("自动测试完毕")
        self.driver.quit()  # 资源释放，不释放下次执行就会报错new session 不能建立，不能建立时需要重启appium

    def setUp(self):
        print("setUp start=========>")

    def tearDown(self):
        print("tearDown end=========>")

    # ====================功能函数：登陆======================
    def login(self, username, psd, agentcom):
        """登陆"""
        print(ctime() + ': ' + '登录开始')
        print(self.driver.title)  # title方法可以获取当前页面的标题显示的字段
        self.driver.switch_to.frame('fraInterface')  # 进入fraInterface框架
        self.driver.find_element_by_id("UserCode").click()
        self.driver.find_element_by_id("UserCode").clear()
        self.driver.find_element_by_id("UserCode").send_keys(username)#填写用户编码

        self.driver.find_element_by_id("PWD").click()
        self.driver.find_element_by_id("PWD").clear()
        self.driver.find_element_by_id("PWD").send_keys(psd)#填写密码

        self.driver.find_element_by_id("StationCode").click()
        self.driver.find_element_by_id("StationCode").clear()
        self.driver.find_element_by_id("StationCode").send_keys(agentcom)#填写机构
        self.driver.find_element_by_id("StationCode").send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_id("StationCode").send_keys(Keys.ENTER)
        # driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/form/table/tbody/tr/td[1]/table/tbody/tr[4]/td/input[1]").click()
        self.driver.switch_to.default_content()  # 退出fraInterface框架
        print(ctime() + ': ' + '登录成功')
        self.driver.get_screenshot_as_file("D:\\pythontest\\test_img.jpg")

        self.driver.switch_to.frame('fraMenuTop')
        # driver.find_element_by_xpath("/html/body/table/tbody/tr/th/font/").text
        linkText = self.driver.find_element_by_xpath("/html/body/table/tbody/tr/th[1]/font")
        sleep(5)
        result = self.driver.find_element_by_xpath("/html/body/table/tbody/tr/th[1]/font").is_displayed()#判断元素是否存在
        print(result)
        print(linkText.text)
        self.assertEqual(linkText.text, '欢迎登陆')
        self.driver.get_screenshot_as_file("D:\\pythontest\\login_success.jpg")
        self.driver.switch_to.default_content()  # 退出fraInterface框架
    # ====================功能函数：无扫描录入======================
    def ChoosePolNO(self, contno, agentcom):
        """无扫描录入"""
        print(ctime() + ': ' + '无扫描录入开始')
        self.driver.switch_to.frame('fraMenu')  # 进入fraMenu框架

        mouse = self.driver.find_element_by_id("MenuTree_link_7")  # 承保处理
        ActionChains(self.driver).move_to_element(mouse).perform()  # 鼠标悬停
        mouse.click()

        mouse = self.driver.find_element_by_id("MenuTree_link_41")  # 个人保单
        ActionChains(self.driver).move_to_element(mouse).perform()  # 鼠标悬停
        mouse.click()

        mouse = self.driver.find_element_by_id("MenuTree_link_53")  # 无扫描录入
        ActionChains(self.driver).move_to_element(mouse).perform()  # 鼠标悬停
        mouse.click()

        self.driver.switch_to.default_content()  # 退出fraMenu框架

        self.driver.switch_to.frame('fraInterface')  # 进入fraInterface框架

        self.driver.find_element_by_css_selector("tr.common>td.input>input.common").clear()
        self.driver.find_element_by_css_selector("tr.common>td.input>input.common").send_keys(contno)  # 投保单号
        self.driver.find_element_by_css_selector("tr.common>td.input>input.codeNo").clear()  # 管理机构
        self.driver.find_element_by_css_selector("tr.common>td.input>input.codeNo").click()
        self.driver.find_element_by_css_selector("tr.common>td.input>input.codeNo").send_keys(agentcom)
        self.driver.find_element_by_css_selector("tr.common>td.input>input.codeNo").send_keys(Keys.ENTER)
        send_date = strftime('%Y-%m-%d', localtime(time()))  # 获取当前时间
        self.driver.find_element_by_css_selector("tr.common>td.input>input.coolDatePicker").clear()  # 申请日期
        self.driver.find_element_by_css_selector("tr.common>td.input>input.coolDatePicker").click()
        self.driver.find_element_by_css_selector("tr.common>td.input>input.coolDatePicker").send_keys(send_date)

        mouse = self.driver.find_element_by_xpath("//html/body/form/input[1]")  # 查询按钮
        print(mouse.get_attribute("value"))
        ActionChains(self.driver).move_to_element(mouse).perform()  # 鼠标悬停
        sleep(2)
        mouse.click()

        result=''
        try:
            mouse = self.driver.find_element_by_xpath("//td[@class='muline']/input[2]")  # 选择记录
            result = mouse.get_attribute("value")
            print(result)
        except Exception as e:
            print(e)
            if result=='on':
                mouse = self.driver.find_element_by_xpath("//td[@class='muline']/input[2]")  # 选择记录
                ActionChains(self.driver).move_to_element(mouse).perform()  # 鼠标悬停
                sleep(2)
                mouse.click()
            else:
                mouse = self.driver.find_element_by_xpath("//html/body/form/input[2]")  # 申请按钮
                print(mouse.get_attribute("value"))
                ActionChains(self.driver).move_to_element(mouse).perform()  # 鼠标悬停
                sleep(2)
                mouse.click()

                mouse = self.driver.find_element_by_xpath("//html/body/form/input[1]")  # 查询按钮
                print(mouse.get_attribute("value"))
                ActionChains(self.driver).move_to_element(mouse).perform()  # 鼠标悬停
                sleep(2)
                mouse.click()

            mouse = self.driver.find_element_by_xpath("//html/body/form/p/input[1]")  # 开始录入
            print(mouse.get_attribute("value"))
            ActionChains(self.driver).move_to_element(mouse).perform()  # 鼠标悬停
            sleep(2)
            mouse.click()
        finally:
            print("不管是否异常，都会执行")

        self.driver.switch_to.default_content()  # 退出fraInterface框架
        print(ctime() + ': ' + '无扫描录入结束')

    # ====================功能函数：无扫描录入======================
    def InfoEntry(self):
        # 进入新窗口
        print("当前窗口：" + self.driver.title)  # title方法可以获取当前页面的标题显示的字段
        new_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles  # 获得所有窗口句柄
        # print(all_handles) #
        print(all_handles[-1])
        # driver.switch_to.window(all_handles[-1])  # 切换至最后一个窗口
        for handle in all_handles:
            if handle != new_windows:
                self.driver.switch_to.window(handle)
                print(self.driver.current_window_handle)
                print("当前窗口：" + self.driver.title)
                self.driver.maximize_window()
                self.driver.implicitly_wait(10)
                break
        # 合同信息
        self.driver.switch_to.frame('fraInterface')
        send_date = strftime('%Y-%m-%d', localtime(time()))  # 获取当前时间
        print(send_date)
        sleep(5)
        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[1]/td[6]/input").clear()  # 收单日期
        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[1]/td[6]/input").click()
        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[1]/td[6]/input").send_keys(send_date)

        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[2]/td[2]/input").clear()  # 投保申请日期
        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[2]/td[2]/input").click()
        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[2]/td[2]/input").send_keys(send_date)

        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[2]/td[4]/input").clear()  # 初审人员
        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[2]/td[4]/input").click()
        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[2]/td[4]/input").send_keys('何磊')

        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[2]/td[6]/input").clear()  # 初审日期
        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[2]/td[6]/input").click()
        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[2]/td[6]/input").send_keys(send_date)

        mouse = self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[3]/td[2]/input[1]")  # 销售渠道
        ActionChains(self.driver).double_click(mouse).perform()
        mouse.send_keys(Keys.ARROW_DOWN)
        mouse.send_keys(Keys.ENTER)

        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[3]/td[10]/input").clear()  # 业务员代码
        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[3]/td[10]/input").click()
        self.driver.find_element_by_xpath("//table[@id='table2']/tbody/tr[3]/td[10]/input").send_keys('110001000159')

        self.driver.switch_to_alert().accept()
        self.driver.switch_to.default_content()

    # test开头的方法被认为是测试用例
    def test_login_success(self):#执行的过程，以test开头的测试用例
        # 用户名、密码正确
        self.login('001', '1', '86')
        sleep(2)

    # test开头的方法被认为是测试用例
    def test_NoScanEntry_success(self):#执行的过程，以test开头的测试用例
        # 投保单号生成正确
        self.ChoosePolNO('160020111102', '86110000')
        sleep(2)

# if __name__ == '__main__':
#     print('----- 测试用例开始 -----')
#     unittest.main()
#     print('----- 测试用例结束 -----')
