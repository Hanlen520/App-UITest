# coding=utf-8

import os
from common.operate import Operate

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
yamlpath = PATH("E:\\App-UITest\\test_yaml\\02_ExitLogin.yaml")
# yamlpath = PATH('/Users/xintudoutest/github/Appium/test_yaml/02_ExitLogin.yaml')

class ExitLogin:

    def __init__(self, driver):
        self.path = yamlpath
        self.driver = driver
        self.operate = Operate(self.path, self.driver)

    def operatepe(self):
        self.operate.check_operate_type()

    def home(self):
        self.operate.back_home()
