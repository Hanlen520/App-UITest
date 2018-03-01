# coding=utf-8

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from common.getDriver import driver

def resourceid(id):
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(id))
    driver.implicitly_wait(2)
    element.click()

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


