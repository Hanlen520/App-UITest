# coding=utf-8

import unittest
import time
import HTMLTestRunner

all_case = '/Users/xintudoutest/appium/AppiumUI/study'

# 使用discover查找出study文件夹下的所有iOS开头的.py文件
def CreateSuite():
    test_suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(all_case,
    pattern ='ios_*.py', top_level_dir=None)

    # 使用for循环出suite,再循环出case
    for suite in discover:
        for case in suite:
            test_suite.addTests(case)
            print(test_suite)
    return test_suite


all_case_names = CreateSuite()
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
filename = '/Users/xintudoutest/appium/AppiumUI/report/'+now+"Myreport.html"
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'测试用例结果', tester=u'宇宙超级无敌大圈圈')
runner.run(all_case_names)
fp.close()