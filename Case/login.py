# coding=utf-8

import unittest
import time
from page.login.login_page_01 import login_001
from devices.ad_device import driver

class Test(unittest.TestCase):
    """登录"""
    def test_01(self):
        """账号登录"""
        add = login_001(driver)
        add.operateap()
        add.home()

    def test_close(self):
        driver.quit()
        time.sleep(10)

if __name__ == "__main__":
    unittest.main()
