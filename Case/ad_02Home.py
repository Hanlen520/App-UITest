# coding=utf-8

import unittest
import time
from page.page_backhome import BackPage
from common.getDriver import driver


class HomeTest(unittest.TestCase):

    def test_01(self):
        """返回首页"""
        ac = BackPage(driver)
        ac.operatepe()
        ac.home()

    def test_close(self):
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":

    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(HomeTest('test_01'))
    unittest.TextTestRunner(verbosity=1).run(suite)
