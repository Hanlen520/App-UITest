# coding=utf-8

import time
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from common.readConfig import Readconfig
from common.getDevices import devices
from common.logs import log


log = log()
con = Readconfig()
cmd = devices()


deviceName = cmd.get_deviceName()
platformVersion = cmd.get_platformVersion()
platformName = con.getAppValue('platformName')
appPackage = con.getAppValue('appPackage')
appActivity = con.getAppValue('appActivity')


desired_caps = {}
desired_caps['deviceName'] = '%s' % deviceName
desired_caps['platformName'] = '%s' % platformName
desired_caps['platformVersion'] = '%s' % platformVersion
desired_caps['appPackage'] = '%s' % appPackage
desired_caps['appActivity'] = '%s' % appActivity
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['no-reset'] = True

try:
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    time.sleep(5)
    log.info('获取driver成功')
except WebDriverException:
    print('No driver')

