# coding=utf-8
from devices.ios_device import driver
from appium.webdriver.common.touch_action import TouchAction

#resourceId属性的方法
def resourceid(self):
    driver.find_element_by_id(self).click()

#class属性的方法
def classname(self):
    driver.find_element_by_class_name(self).click()

def classnames(self, x):
    driver.find_elements_by_class_name(self).__getitem__(x).click()

#text属性的方法
def text(self):
    driver.find_element_by_android_uiautomator('new UiSelector().text("self")').click()

#xpath属性方法
def xpath(self):
    driver.find_element_by_xpath(self).click()

#name属性方法
def name(self):
    driver.find_element_by_name(self).click()

#通过坐标点击
def tap(x, y):
    TouchAction(driver).tap(None, x, y).perform()


