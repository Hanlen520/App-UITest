# coding=utf-8
import unittest
from time import sleep
from common import my_swipe, click

enter = "tab capture"
back = "camera discover"
more = "camera moreopt"
camera_button = "//XCUIElementTypeApplication[@name=\"有才企业release\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeButton"
camera_button_2 = "//XCUIElementTypeApplication[@name=\"有才企业release\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[4]/XCUIElementTypeButton"

class Test(unittest.TestCase):
    """拍摄"""
    @unittest.skip('跳过')
    def test_01(self):
        """拍摄页面，点击返回按钮"""
        click.name(enter)
        sleep(2)
        click.name(back)
        sleep(2)
        #拍摄一段视频后点击返回按钮，提示框测试
        click.name(enter)
        sleep(2)
        click.xpath(camera_button)
        sleep(3)
        click.xpath(camera_button)
        sleep(2)
        click.name(back)
        sleep(2)
        #提示框点击取消按钮
        click.name("取消")
        sleep(2)
        click.name(back)
        sleep(2)
        #提示框点击确定按钮，返回精选页
        click.name("确定")
        sleep(2)

    @unittest.skip('跳过')
    def test_02(self):
        """拍摄页面，设置倒计时"""
        click.name(enter)
        sleep(2)
        # 设置倒计时3s
        click.name(more)
        sleep(2)
        click.name("3s")
        click.name("5s")
        click.name("10s")
        # 点击屏幕收起倒计时浮层
        click.tap(208, 346)
        sleep(2)
        #验证设置10s是否生效
        my_swipe.assertion_name("10")
        click.name("10")
        sleep(2)
        my_swipe.assertion_name("9")
        click.xpath(camera_button_2)
        sleep(2)
        #取消倒计时设置
        click.name(more)
        click.name("camera countzero")
        #点击确定按钮收起浮层
        click.name("确定")
        #验证取消倒计时成功
        click.xpath(camera_button)
        sleep(4)
        my_swipe.assertion_name("camera nextstep")
        click.xpath(camera_button)
        sleep(2)
        #退出拍摄页面
        click.name(back)
        click.name("确定")


#    @unittest.skip('跳过')
    def test_03(self):
        """拍摄页面，设置拍摄时长"""
        click.name(enter)
        sleep(2)
        #取消倒计时
        click.name(more)
        #设置拍摄时长20s
        click.name("20s")
        click.tap(208, 346)
        sleep(2)
        #点击拍摄按钮，拍摄15s的视频，验证20s设置成功
        click.xpath(camera_button)
        sleep(12)
        click.xpath(camera_button)
        sleep(2)
        my_swipe.assertion_name("camera nextstep")
        click.name(back)
        click.name("确定")

    @unittest.skip('跳过')
    def test_04(self):
        """拍摄页面，设置闪光灯"""
        click.name(enter)
        #打开闪光灯
        click.name("camera flashoff")
        sleep(2)
        #关闭闪光灯
        click.name("camera flashon")
        sleep(2)

    @unittest.skip('跳过')
    def test_05(self):
        """拍摄页面，设置速率"""
        click.name(enter)
        click.name("camera speedcontrol")
        sleep(2)
        #点击0.25X
        click.name("极慢")
        #点击0.5X
        click.name("慢")
        #点击1.0X
        click.name("标准")
        #点击2.0X
        click.name("快")
        #点击4.0X
        click.name("极快")
        sleep(2)
        #左右滑动
        my_swipe.press(320, 577, -240, 0)
        sleep(2)
        my_swipe.press(85, 577, 240, 0)
        sleep(2)
        #点击0.25X
        click.name("极慢")
        #点击拍摄按钮
        click.xpath(camera_button_2)
        sleep(8)
        click.name("camera back")
        sleep(2)
        click.name(back)
        click.name("确定")


    @unittest.skip('跳过')
    def test_06(self):
        """拍摄页面，设置美颜"""
        click.name(enter)
        #关闭美颜
        click.name("camera beautyhighlighted")
        sleep(2)
        #开启美颜
        click.name("camera beautynormal")
        sleep(2)

    @unittest.skip('跳过')
    def test_07(self):
        """拍摄页面，设置前置摄像"""
        #切换至前置摄像
        click.name("camera flip")
        sleep(2)
        #切换回后置摄像
        click.tap(380, 257)
        sleep(2)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test('test_01'))
    suite.addTest(Test('test_02'))
    suite.addTest(Test('test_03'))
    suite.addTest(Test('test_04'))
    suite.addTest(Test('test_05'))
    suite.addTest(Test('test_06'))
    suite.addTest(Test('test_07'))
#    unittest.TextTestRunner(verbosity=1).run(suite)
