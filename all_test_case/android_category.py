# coding=utf-8
from public import my_swipe
import unittest

entrance = "com.tudou.android:id/tab_category"
drawer_title = "com.tudou.android:id/dis_tv_vedio_name"
home = "com.tudou.android:id/tab_homepage"

class Test(unittest.TestCase):
    """发现测试用例"""
    def test_01(self):
        """首页点击tab导航栏，进入发现页面"""
        my_swipe.resourceid_click(entrance)
        my_swipe.resourceid_assert(u"火爆主题", drawer_title)

    def test_02(self):
        my_swipe.resourceid_click(home)

    def test_03(self):
        my_swipe.swipeDown(1000)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test('test_01'))
    suite.addTest(Test('test_02'))