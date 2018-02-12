# coding=utf-8
from appium import webdriver
import time

desired_caps = dict(platformName='Android',
                    deviceName='WWOUPJ9T99999999',
                    platformVersion='5.1',
                    appPackage='com.youcai.android',
                    appActivity='com.youcai.android.ui.activity.SplashActivity',
                    unicodeKeyboard=True,
                    resetKeyboard=True)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
