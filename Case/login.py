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
        testone = login001(driver)
        testone.operatepe()
        testone.home()
    @unittest.skip("跳过")
    def test_02(self):
        """退出账号登录"""
        testtwo = login003(driver)
        testtwo.operatepe()
        testtwo.home()

    def test_close(self):
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    unittest.main()
