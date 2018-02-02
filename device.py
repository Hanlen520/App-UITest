# coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['deviceName'] = "iPhone 8 Plus"
desired_caps['platformName'] = 'ios'
desired_caps['platformVersion'] = '10.3'
desired_caps['bundleId'] = 'com.youcai.iphone'     # 包名
desired_caps['udid'] = 'dc5b8e6f99c23817458e2a81f8e1c240f2b1614d'
desired_caps['AutomationName'] = 'XCUITest'
desired_caps['xcodeOrgId'] = "292867314@qq.com"
desired_caps['xcodeSigningId'] = "iPhone Developer"
desired_caps['no-reset'] = True
# desired_caps['app'] = "/Users/woody/Downloads/TDMainClient-Release.ipa"
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
time.sleep(2)

