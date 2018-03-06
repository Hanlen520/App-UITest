# coding=utf-8

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from common.getDriver import driver

def resourceid(id):
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(id))
    driver.implicitly_wait(2)
    element.click()

def classname(name):
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name(name))
    driver.implicitly_wait(2)
    element.click()


def xpath(xpath):
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath))
    driver.implicitly_wait(2)
    element.click()

def name(name):
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_name(name))
    driver.implicitly_wait(2)
    element.click()

def tap(x, y):
    TouchAction(driver).tap(None, x, y).perform()


