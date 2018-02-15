# coding=utf-8
from devices.ad_device import driver
import time

def screenshot():
    # 获取当前时间
    now = time.strftime("%Y%m%d.%H.%M.%S")
    # 将图片保存到指定目录下，并用时间命名
    driver.get_screenshot_as_file('D:\\Study-Appium\\screenshot\\' + now + '.png')
    # driver.get_screenshot_as_file('/Users/xintudoutest/appium/AppiumUI/screenshot/' + now + '.png')
    print('screenshot:', now, '.png')

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