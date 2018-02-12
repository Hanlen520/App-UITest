import unittest
from devices.ios_device import driver

class Test(unittest.TestCase):
    """小视频首页"""
    def test_01(self):
        driver.find_element_by_name()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test('test_01'))