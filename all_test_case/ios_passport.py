# coding=utf-8
import unittest
import common
import click
from time import sleep

close_button = "yc close 20 20 light"
page_close_button = "shut down"
iphone_input = "//XCUIElementTypeApplication[@name=\"爱鹿企业release\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField"


class Test(unittest.TestCase):
    """登录"""
    def test_01(self):
        """登录弹框"""
        click.tap(328, 709)
        sleep(2)
        click.name(close_button)
        #点击登录按钮，进入登录页面
        click.tap(328, 709)
        click.name("更多登录方式")
        sleep(2)
        click.name(page_close_button)


    def test_02(self):
        """账号登录"""
        click.tap(328, 709)
        click.name("更多登录方式")
        click.name("账号登录")
        click.xpath()






if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test("test_01"))
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
