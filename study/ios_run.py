# coding=utf-8
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

#注意使用套件时，在单个py文件中下的多个用例用  (类名（"方法名")),
#导入多个py的类下，用（py名.类名）

all_case = '/Users/xintudoutest/appium/AppiumUI/test_case'

def CreateSuite():                                                      # 产生测试套件
    test_suite = unittest.TestSuite()                                     # 使用discover找出用例文件夹下all_test_case的所有用例
    discover = unittest.defaultTestLoader.discover(all_case,              # 查找的文件夹路径
    pattern ='ios_*.py', top_level_dir=None)                             # 要测试的模块名，以ios开头的.py文件

    for suite in discover:  #使用for循环出suite,再循环出case
        for case in suite:
            test_suite.addTests(case)
            print(test_suite)
    return test_suite


#下面语句用来生成测试报告
