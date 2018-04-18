# coding=utf-8

import unittest
from page.page_login.page_AccountLogin import AccountLogin
from page.page_login.page_ExitLogin import ExitLogin
from common.getDriver import driver


class LoginTest(unittest.TestCase):
    """登录"""

    @unittest.skip("跳过")
    def test_01(self):
        """手机账号登录"""
        ac = AccountLogin(driver)
        ac.operatepe()

    def test_02(self):
        """退出账号登录"""
        ex = ExitLogin(driver)
        ex.operatepe()
        # ex.home()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(LoginTest('test_02'))
    unittest.TextTestRunner(verbosity=1).run(suite)
