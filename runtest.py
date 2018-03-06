# coding=utf-8

import time
import unittest
import HTMLTestRunner
from common.sendEmail import send_email

all_case = '/Users/xintudoutest/github/Appium/Case'


# 使用discover查找出Case文件夹下的所有ad开头的.py文件
def CreateSuite():
    test_suite = unittest.TestSuite()  # 创建测试套件
    discover = unittest.defaultTestLoader.discover(all_case,
    pattern ='ad_*.py', top_level_dir=None)

    # 使用for循环出suite,再循环出case
    for suite in discover:
        for case in suite:
            test_suite.addTests(case)
            print(test_suite)
    return test_suite


def runtest():
    case = CreateSuite()
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # filename = 'D:\\Study-Appium\\report\\' + now + "Myreport.html"
    filename = '/Users/xintudoutest/github/Appium/report/' + now + "Myreport.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'测试用例结果', tester=u'宇宙超级无敌大圈圈')
    runner.run(case)
    fp.close()


def email():
    send_email()


if __name__ == "__main__":

    runtest()
    email()

