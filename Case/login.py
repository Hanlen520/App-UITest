# coding=utf-8
import unittest
import time
from page.login_page.login001 import login001
from page.login_page.login003 import login003
from devices.ad_device import driver

class Test(unittest.TestCase):
    """登录"""
    def test_01(self):
        """手机账号登录"""
        add = login001(driver)
        add.operatepe()
        # add.home()

    def test_02(self):
        """退出账号登录"""
        add = login003(driver)
        add.operatepe()

    def test_close(self):
        driver.quit()
        time.sleep(10)

if __name__ == "__main__":
    unittest.main()
