# coding=utf-8
import unittest
import time
from page.page_backhome import DemoPage
from devices.ad_device import driver

class DemoTest(unittest.TestCase):
    """调试backhome"""
    def test_01(self):
        """返回首页"""
        ac = DemoPage(driver)
        ac.operatepe()
        ac.home()

    def test_close(self):
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    unittest.main()
