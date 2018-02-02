# coding=utf-8
from device import driver
from appium.webdriver.common.touch_action import TouchAction
import time

#滑动元素
def press(x, y, x1, y1):
    TouchAction(driver).press(None, x, y).move_to(None, x1, y1).release().perform()

#输入
def sendkeys(self, text):
    driver.find_element_by_id(self).send_keys(text)

def xpath_sendkeys(self, text):
    driver.find_element_by_xpath(self).send_keys(text)

#截图
def screenshot():
    now = time.strftime("%Y%m%d.%H.%M.%S")#获取当前时间
    driver.get_screenshot_as_file('/Users/xintudoutest/appium/AppiumUI/screenshot/'+now+'.png')#截图，将截图保存到指定目录下，并用时间命名图片
    print 'screenshot:', now, '.png'


#通过classname查找元素，进行断言
def assertion_class(self, id):
    try:
        assert self == driver.find_element_by_class_name(id).text
    except Exception as msg:
        print(u'测试未通过%s'%msg)
        screenshot()
        raise

#通过resourceid查找元素，进行断言
def assertion_resourceid(self, id):
    try:
        assert self == driver.find_element_by_id(id).text
    except Exception as msg:
        print(u'测试未通过%s'%msg)
        screenshot()
        raise

#通过name查找元素是否存在，进行断言
def assertion_name(name):
    try:
        assert driver.find_element_by_name(name).is_displayed()
    except Exception as msg:
        print(u'测试未通过%s' % msg)
        screenshot()
        raise




#获得机器屏幕大小x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y

    #屏幕向上滑动
def swipeUp(time):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2, time)

    #屏幕向下滑动
def swipeDown(time):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    driver.swipe(x1, y1, x1, y2, time)

    #屏幕向左滑动
def swipeLeft(time):
    l = getSize()
    x1 = int(l[0]*0.75)
    y1 = int(l[1]*0.5)
    x2 = int(l[0]*0.05)
    driver.swipe(x1, y1, x2, y1, time)


    #屏幕向右滑动
def swipeRight(time):
    l = getSize()
    x1 = int(l[0]*0.05)
    y1 = int(l[1]*0.5)
    x2 = int(l[0]*0.75)
    driver.swipe(x1, y1, x2, y1, time)


def quit():
    driver.quit()


