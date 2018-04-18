# coding=utf-8

from demo.ios_device import driver
from appium.webdriver.common.touch_action import TouchAction

# 按照坐标滑动，从x,y滑动到x1,y1
def press(x, y, x1, y1):
    TouchAction(driver).press(None, x, y).move_to(None, x1, y1).release().perform()

# 获得机器屏幕大小x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y

# 屏幕向上滑动，x轴固定，从y1滑动到y2
def swipeUp(time):
    l = getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.75)
    y2 = int(l[1] * 0.25)
    driver.swipe(x1, y1, x1, y2, time)

# 屏幕向下滑动，x轴固定，从y2滑动到y1
def swipeDown(time):
    l = getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.25)
    y2 = int(l[1] * 0.75)
    driver.swipe(x1, y1, x1, y2, time)

# 屏幕向左滑动
def swipeLeft(time):
    l = getSize()
    x1 = int(l[0]*0.75)
    y1 = int(l[1]*0.5)
    x2 = int(l[0]*0.05)
    driver.swipe(x1, y1, x2, y1, time)

# 屏幕向右滑动
def swipeRight(time):
    l = getSize()
    x1 = int(l[0]*0.05)
    y1 = int(l[1]*0.5)
    x2 = int(l[0]*0.75)
    driver.swipe(x1, y1, x2, y1, time)




