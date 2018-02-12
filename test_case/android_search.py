# coding=utf-8
import unittest
import time
from common import my_swipe

entrance = "com.tudou.android:id/rip2_home_search_rl"
search_text = "com.tudou.android:id/et_widget_search_text"
search_button = "com.tudou.android:id/tv_right"
video_title = "com.tudou.android:id/item_search_result_show_big_info_title"
text = u'火影忍者'

class Test(unittest.TestCase):
    """搜索测试用例"""
    def test_01(self):
        """首页点击搜索按钮，进入搜索页面"""
        my_swipe.resourceid_click(entrance)
        my_swipe.resourceid_assert(u'搜索', search_button)

    def test_02(self):
        """输入内容，点击搜索按钮，进入搜索结果页面"""
        my_swipe.resourceid_sendkeys(search_text, text)
        my_swipe.resourceid_click(search_button)
        time.sleep(3)
        my_swipe.resourceid_assert(u"火影忍者 2002", video_title)

    def test_03(self):
        my_swipe.swipeUp(1000)

#添加要执行的case，需要测试的用例就addTest，不加的就不会运行
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test('test_01'))
    suite.addTest(Test('test_02'))
#    unittest.TextTestRunner(verbosity=2).run(suite)

