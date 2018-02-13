# coding=utf-8
from study import Swipe
import unittest
import time

tab_sub = "com.tudou.android:id/tab_subscribe"
sub_tab_container = "com.tudou.android:id/rip2_tab_container"
sub_user_list = "com.tudou.android:id/sub_user_list_img"
list_empty = "com.tudou.android:id/title"
list_empty_button = "com.tudou.android:id/btn_retry"
list_subject_title = "com.tudou.android:id/subscribe_user_item_layout"
list_subscribe_button = "com.tudou.android:id/subscribe_user_item_btn_subscribe"
list_subscribe_state = "com.tudou.android:id/tv_widget_subscriber_button_states"
list_subject = "com.tudou.android:id/subscribe_user_subject_item_rl_root"
list_back = "android.widget.FrameLayout"
subject_detail_title = "com.tudou.android:id/t7_tv_infotitle"
subject_detail_back = "com.tudou.android:id/rl_back"
subject_guide_view = "com.tudou.android:id/subject_guide_view"
subject_title = "com.tudou.android:id/subscribe_subject_username"
subject_video = "com.tudou.android:id/fragment_subscribe_item_ll_video"
sub_button = "com.tudou.android:id/subject_subscribe_btn"
home = "com.tudou.android:id/tab_homepage"

class Test(unittest.TestCase):
    """订阅主题"""
    def test_01(self):
        """首页点击底部tab导航栏，进入订阅-主题页面"""
        Swipe.resourceid_click(tab_sub)
        time.sleep(3)

    def test_02(self):
        """点击进入主题管理页，点击看看推荐"""
        Swipe.resourceid_click(sub_user_list)
        Swipe.resourceid_assert(u"还没有订阅过主题哦~", list_empty)
        Swipe.resourceid_click(list_empty_button)

    def test_03(self):
        """主题管理页，点击除订阅按钮外的区域，进入主题详情页"""
        Swipe.resourceid_click(sub_button)
        Swipe.resourceid_click(sub_user_list)
        Swipe.resourceid_click(list_subject_title)
        Swipe.resourceid_click(subject_detail_back)

    def test_04(self):
        """主题管理页，点击已订阅按钮，取消订阅，下拉刷新后在列表中移除"""
        Swipe.resourceid_click(list_subscribe_button)
        Swipe.resourceid_assert(u"订阅", list_subscribe_state)
        Swipe.swipeDown(1000)
        Swipe.resourceid_assert(u"还没有订阅过主题哦~", list_empty)
        Swipe.classname_click(list_back)

    def test_quit(self):
        Swipe.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test('test_01'))
    suite.addTest(Test('test_02'))
    suite.addTest(Test('test_03'))
    suite.addTest(Test('test_04'))
    suite.addTest(Test('test_quit'))
