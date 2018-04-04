# coding=utf-8

from selenium.webdriver.support.ui import WebDriverWait
from common.logs import log
import os
import time

log = log()

# 基础操作：返回、上下左右滑动屏幕、截图、获取element信息
class BaseOperate:
    def __init__(self, driver):
        self.driver = driver

    # Android 点击物理返回键
    def back(self):
        os.popen("adb shell input keyevent 4")

    # 获取屏幕大小
    def get_window_size(self):
        global windowSize
        windowSize = WebDriverWait(self.driver, 10).until(lambda x: x.get_window_size())
        self.driver.implicitly_wait(2)
        return windowSize

    # 向上滑动
    def swipeUp(self):
        windowsSize = self.get_window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        self.driver.swipe(width/2, height*3/4, width/2, height/4, 1000)

    # 向下滑动
    def swipeDown(self):
        windowsSize = self.get_window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        self.driver.swipe(width/2, height/4, width/2, height*3/4, 1000)

    # 向左滑动
    def swipeLeft(self):
        windowsSize = self.get_window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        self.driver.swipe(width*3/4, height/2, width/20, height/2, 1000)

    # 向右滑动
    def swipeRight(self):
        windowsSize = self.get_window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        self.driver.swipe(width/20, height/2, width*3/4, height/2, 1000)

    # 截图
    def screenshot(self):
        # 获取当前时间
        now = time.strftime("%Y%m%d.%H.%M.%S")
        # 将图片保存到指定目录下，并用时间命名
        self.driver.get_screenshot_as_file('E:\\App-UITest\\screenshot\\' + now + '.png')
        # self.driver.get_screenshot_as_file('/Users/xintudoutest/github/Appium/screenshot/' + now + '.png')
        print('screenshot:', now, '.png')

    # 定位页面text元素，param：name
    def get_name(self, name):
        findname = "//*[@text='%s']"%(name)
        try:
            element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(findname))
            self.driver.implicitly_wait(2)
            return element
        except:
            log.error('未定位到元素：'+'%s'%(name))
            self.screenshot()

    # 定位页面resouce id元素，param：id
    def get_id(self, id):
        try:
            element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(id))
            self.driver.implicitly_wait(2)
            return element
        except:
            log.error('未定位到元素：'+'%s'%(id))
            self.screenshot()

    # 定位页面xpath元素，param：xpath
    def get_xpath(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(xpath))
            self.driver.implicitly_wait(2)
            return element
        except:
            log.error('未定位到元素：'+'%s'%(xpath))
            self.screenshot()

    # 定位页面resouce id元素组，param：id，return：元素列表
    def get_ids(self, id):
        try:
            elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_id(id))
            self.driver.implicitly_wait(2)
            return elements
        except:
            log.error('未定位到元素：'+'%s'%(id))
            self.screenshot()

    # 返回到指定页面，不兼容Android7.0系统
    def backpage(self, name):
        i = 0
        while i < 10:
            i = i + 1
            try:
                findname = "//*[@text='%s']" % (name)
                self.driver.find_element_by_xpath(findname)
                self.driver.implicitly_wait(2)
                break
            except:
                os.popen("adb shell input keyevent 4")
                try:
                    findname = "//*[@text='首页']"
                    self.driver.find_element_by_xpath(findname).click()
                    self.driver.implicitly_wait(2)
                except:
                    os.popen("adb shell input keyevent 4")