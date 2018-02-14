# coding=utf-8

import unittest
import time
from page.ad_login.login_page_001 import login_001
from devices.ad_device import driver

class login(unittest.TestCase):
    """登录"""
    def test_001(self):
        """账号登录"""
        add = login_001(driver)
        add.operateap()
        add.home()

    def test_999close(self):
        driver.quit()
        time.sleep(10)

if __name__ == "__main__":
    unittest.main()
