# coding=utf-8

from selenium.webdriver.support.ui import WebDriverWait
from common.logs import log
import os
import time

'''
一些基础操作：滑动、截图、点击页面元素等
'''

log = log()
class BaseOperate:
    def __init__(self, driver):
        self.driver = driver

    def back(self):
        '''
        返回键
        :return:
        '''
        os.popen("adb shell input keyevent 4")

    def swipeUp(self):
        '''
        向上滑动
        :return:
        '''
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width/2, height*3/4, width/2, height/4, 1000)

    def swipeDown(self):
        '''
        向下滑动
        :return:
        '''
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width/2, height/4, width/2, height*3/4, 1000)

    def swipeLeft(self):
        '''
        向左滑动
        :return:
        '''
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width*3/4, height/2, width/20, height/2, 1000)

    def swipeRight(self):
        '''
        向右滑动
        :return:
        '''
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width*3/4, height/2, width/20, height/2, 1000)

    def screenshot(self):
        # 获取当前时间
        now = time.strftime("%Y%m%d.%H.%M.%S")
        # 将图片保存到指定目录下，并用时间命名
        self.driver.get_screenshot_as_file('D:\\Study-Appium\\screenshot\\' + now + '.png')
#       self.driver.get_screenshot_as_file('/Users/xintudoutest/appium/AppiumUI/screenshot/' + now + '.png')
        print('screenshot:', now, '.png')

    def find_id(self, id):
        '''
        寻找元素
        :return:
        '''
        exsit = self.driver.find_element_by_id(id)
        if exsit:
            return True
        else:
            return False

    def find_name(self, name):
        '''
        判断页面是否存在某个元素
        :param name: text
        :return:
        '''
        findname = "//*[@text='%s']"%(name)
        exsit = self.driver.find_element_by_xpath(findname)
        if exsit:
            return True
        else:
            return False

    def get_name(self, name):
        '''
        定位页面text元素
        :param name:
        :return:
        '''
        # element = driver.find_element_by_name(name)
        # return element

        findname = "//*[@text='%s']"%(name)
        try:
            element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(findname))
            # element = self.driver.find_element_by_xpath(findname)
            self.driver.implicitly_wait(2)
            return element
        except:
            self.screenshot()
            log.error('未定位到元素：'+'%s'%(name))

    def get_id(self, id):
        '''
        定位页面resouce-id元素
        :param id:
        :return:
        '''
        try:
            # element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(id()))
            element = self.driver.find_element_by_id(id)
            self.driver.implicitly_wait(2)
            return element
        except:
            self.screenshot()
            log.error('未定位到元素：'+'%s'%(id))

    def get_xpath(self, xpath):
        '''
        定位页面xpath元素
        :param id:
        :return:
        '''
        try:
            element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(xpath))
            # element = self.driver.find_element_by_xpath(xpath)
            self.driver.implicitly_wait(2)
            return element
        except:
            self.screenshot()
            log.error('未定位到元素：'+'%s'%(xpath))

    def get_ids(self, id):
        '''
        定位页面resouce-id元素组
        :param id:
        :return:列表
        '''
        try:
            # elements = self.driver.find_elements_by_id(id)
            elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_id(id))
            self.driver.implicitly_wait(2)
            return elements
        except:
            self.screenshot()
            log.error('未定位到元素：'+'%s'%(id))

    def page(self, name):
        '''
        返回至指定页面
        :return:
        '''
        i = 0
        while i < 10:
            i = i+1
            try:
                findname = "//*[@text='%s']"%(name)
                self.driver.find_element_by_xpath(findname)
                self.driver.implicitly_wait(2)
                break
            except :
                os.popen("adb shell input keyevent 4")
                try:
                    findname = "//*[@text='确定']"
                    self.driver.find_element_by_xpath(findname).click()
                    self.driver.implicitly_wait(2)
                except:
                    os.popen("adb shell input keyevent 4")
                try:
                    self.driver.find_element_by_xpath("//*[@text='工作台']")
                    self.driver.implicitly_wait(2)
                    break
                except:
                    os.popen("adb shell input keyevent 4")