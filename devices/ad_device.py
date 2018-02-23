# coding=utf-8
from appium import webdriver
import time

desired_caps = dict(
                    platformName='Android',
                    deviceName='20389c54',
                    platformVersion='7.1.2',
                    appPackage='com.youcai.android',
                    appActivity='com.youcai.android.ui.activity.SplashActivity',
                    unicodeKeyboard=True,
                    resetKeyboard=True
                    # noReset=True
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
