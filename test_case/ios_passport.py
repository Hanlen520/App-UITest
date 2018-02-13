# coding=utf-8
import unittest
from common import click
from study import Swipe
from time import sleep

close_button = "yc close 20 20 light"
page_close_button = "shut down"
iphone_input = "//XCUIElementTypeApplication[@name=\"爱鹿release\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField"
password_input = "//XCUIElementTypeApplication[@name=\"爱鹿release\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeSecureTextField"

class Test(unittest.TestCase):
    """登录"""
    @unittest.skip('跳过')
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
        sleep(2)
        click.name("账号登录")
        Swipe.xpath_sendkeys(iphone_input, '18810948950')
        Swipe.xpath_sendkeys(password_input, 'youcai123')
        click.name("登录")
        sleep(3)
        Swipe.assertion_name('me message')
        Swipe.quit()






if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test("test_02"))
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
