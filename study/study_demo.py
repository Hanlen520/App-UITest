# coding=utf-8
from study import click
import unittest
import os
from common.getDriver import driver


class Test(unittest.TestCase):
    """爱鹿登录"""
    def test_01(self):
        """账号登录"""
        click.resourceid('com.youcai.android:id/home_tab_mine')
        click.resourceid('com.youcai.android:id/uc_follow_count')
        click.resourceid('com.youcai.android:id/uc_list_item_user_name')
        click.resourceid('com.youcai.android:id/uc_fans_count')

        i = 0
        while i < 10:
            i = i + 1
            try:
                findname = "//*[@text='%s']" % ('推荐')
                driver.find_element_by_xpath(findname)
                driver.implicitly_wait(2)
                break
            except:
                os.popen("adb shell input keyevent 4")
                try:
                    driver.find_element_by_xpath("//*[@text='推荐']")
                    driver.implicitly_wait(2)
                    break
                except:
                    os.popen("adb shell input keyevent 4")

        driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test('test_01'))
    runner = unittest.TextTestRunner(verbosity=1).run(suite)
    runner.run(suite)
