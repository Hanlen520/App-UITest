# coding=utf-8
from study import Swipe, click, assertion
import unittest
import time
from devices.ad_device import driver

enter = "com.tudou.android:id/tab_upload"
back = "com.tudou.android:id/imgBack"
back_msg = "com.tudou.android:id/dialog_title_msg"
cancel = "com.tudou.android:id/dialog_btn_cancel_root"
sure = "com.tudou.android:id/dialog_btn_sure_root"
more = "com.tudou.android:id/imgMoreSet"
count = "com.tudou.android:id/countDownText"
count3s = "com.tudou.android:id/countDown1"
count5s = "com.tudou.android:id/countDown2"
count10s = "com.tudou.android:id/countDown3"
count_none = "com.tudou.android:id/noneCountDown"
screen_view = "com.tudou.android:id/otherView"
timelength10s = "com.tudou.android:id/timeLength1"
timelength20s = "com.tudou.android:id/timeLength2"
light = "com.tudou.android:id/imgFlashlight"
speed = "com.tudou.android:id/imgSpeed"
fair = "com.tudou.android:id/imgFair"
camera = "com.tudou.android:id/imgReturn"
tabname = "com.tudou.android:id/tv_tab_name"

class Test(unittest.TestCase):
    """拍摄"""
    def test_01(self):
        """拍摄页面，点击返回按钮"""
        click.resourceid(enter)
        click.resourceid(back)
        #拍摄一段视频后点击返回按钮，提示框测试
        click.resourceid(enter)
        driver.tap(510, 1610).release().perform()
        time.sleep(5)
        driver.tap(510, 1610).release().perform()
        click.resourceid(back)
        assertion.assertion_resourceid(u'确定放弃已经录制好的视频吗？', back_msg)
        #提示框点击取消按钮
        click.resourceid(cancel)
        click.resourceid(back)
        #提示框点击确定按钮，返回精选页
        click.resourceid(sure)
        assertion.assertion_resourceid(u"小视频", tabname)


    def test_02(self):
        """拍摄页面，设置倒计时"""
        click.resourceid(enter)
        click.resourceid(more)
        #设置倒计时3s
        click.resourceid(count3s)
        click.resourceid(screen_view)
        assertion.assertion_resourceid("3", count)
        #设置倒计时5s
        click.resourceid(more)
        click.resourceid(count5s)
        click.resourceid(screen_view)
        assertion.assertion_resourceid("5", count)
        #设置倒计时10s
        click.resourceid(more)
        click.resourceid(count10s)
        click.resourceid(screen_view)
        #验证设置倒计时10S成功
        assertion.assertion_resourceid("10", count)

    def test_03(self):
        """拍摄页面，设置拍摄时长"""
        click.resourceid(more)
        #取消倒计时
        click.resourceid(count_none)
        #设置拍摄时长20s
        click.resourceid(timelength20s)
        click.resourceid(screen_view)
        #点击拍摄按钮，拍摄15s的视频，验证20s设置成功
        driver.tap(510, 1610).release().perform()
        time.sleep(15)
        driver.tap(510, 1610).release().perform()

    def test_04(self):
        """拍摄页面，设置闪光灯"""
        #打开闪光灯
        click.resourceid(light)
        #关闭闪光灯
        click.resourceid(light)

    def test_05(self):
        """拍摄页面，设置速率"""
        click.resourceid(speed)
        #点击0.25X
        driver.tap(265, 1392)
        #点击0.5X
        driver.tap(398, 1392)
        #点击1.0X
        driver.tap(533, 1392)
        #点击2.0X
        driver.tap(654, 1392)
        #点击4.0X
        driver.tap(798, 1392)
        #从右向左滑动
        driver.swipe(810, 1389, 265, 1389, 1000)
        #从左向右滑动
        driver.swipe(265, 1389, 810, 1389, 1000)
        #点击0.25X
        driver.tap(265, 1392)
        #点击拍摄按钮
        driver.tap(510, 1610)
        time.sleep(4)
        Swipe.assertion_resourceid(u'输入标题更醒目哦～', "com.tudou.android:id/videoTitle")
        click.resourceid(back)

    def test_06(self):
        """拍摄页面，设置美颜"""
        #关闭美颜
        click.resourceid(fair)
        #开启美颜
        click.resourceid(fair)

    def test_07(self):
        """拍摄页面，设置前置摄像"""
        #切换至前置摄像
        click.resourceid(camera)
        #切换回后置摄像
        click.resourceid(camera)
        driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test('test_01'))
    suite.addTest(Test('test_02'))
    suite.addTest(Test('test_03'))
    suite.addTest(Test('test_04'))
    suite.addTest(Test('test_05'))
    suite.addTest(Test('test_06'))
    suite.addTest(Test('test_07'))
    unittest.TextTestRunner(verbosity=7).run(suite)
