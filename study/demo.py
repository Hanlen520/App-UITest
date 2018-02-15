# coding=utf-8
from study import click, assertion
from devices.ad_device import driver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

class Test(unittest.TestCase):
    """爱鹿登录"""
    def test_01(self):
        """账号登录"""
        click.resourceid('com.youcai.android:id/home_tab_mine')
        assertion.assertion_resourceid(u'账号登录A', 'com.youcai.android:id/passport_login_type')
        # driver.find_element_by_id('com.youcai.android:id/passport_login_type').text(u'账号登录')
        driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test('test_01'))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = 'D:\\Study-Appium\\report\\' + now + "Myreport.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'测试用例结果', tester=u'宇宙超级无敌大圈圈')
    runner.run(suite)
    fp.close()
