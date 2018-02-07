# coding=utf-8
from devices.ios_device import driver
import time


#截取图片
def screenshot():
    #获取当前时间
    now = time.strftime("%Y%m%d.%H.%M.%S")
    #将图片保存到指定目录下，并用时间命名
    driver.get_screenshot_as_file('/Users/xintudoutest/appium/AppiumUI/screenshot/'+now+'.png')
    print 'screenshot:', now, '.png'