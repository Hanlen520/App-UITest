# coding=utf-8
from devices.ad_device import driver
from appium.webdriver.common.touch_action import TouchAction

def resourceid(self):
    driver.find_element_by_id(self).click()

def classname(self):
    driver.find_element_by_class_name(self).click()

def classnames(self, x):
    driver.find_elements_by_class_name(self).__getitem__(x).click()

def xpath(self):
    driver.find_element_by_xpath(self).click()

def name(self):
    driver.find_element_by_name(self).click()

def tap(x, y):
    TouchAction(driver).tap(None, x, y).perform()


