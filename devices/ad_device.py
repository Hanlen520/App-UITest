# coding=utf-8
from appium import webdriver
import time

desired_caps = dict(
                    platformName='Android',
                    deviceName='343b59350104',
                    platformVersion='6.0.1',
                    appPackage='com.youcai.android',
                    appActivity='com.youcai.android.ui.activity.SplashActivity',
                    unicodeKeyboard=True,
                    resetKeyboard=True
                    #noReset=True
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
