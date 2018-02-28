# coding=utf-8
import unittest
import time
from page.page_login.page_AccountLogin import AccountLogin
from page.page_login.page_ExitLogin import ExitLogin
from devices.ad_device import driver

class LoginTest(unittest.TestCase):
    """登录"""
    def test_01(self):
        """手机账号登录"""
        ac = AccountLogin(driver)
        ac.operatepe()

    @unittest.skip("跳过")
    def test_02(self):
        """退出账号登录"""
        ex = ExitLogin(driver)
        ex.operatepe()
        ex.home()


if __name__ == "__main__":
    unittest.main()
