# coding=utf-8
from appium import webdriver
import time

<<<<<<< HEAD
desired_caps = dict(platformName='Android',
                    deviceName='WWOUPJ9T99999999',
                    platformVersion='5.1',
                    appPackage='com.tencent.qqmusic',
                    appActivity='com.tencent.qqmusic.activity.AppStarterActivity',
=======
desired_caps = dict(
                   #automationName='UIAutomator2',
                    platformName='Android',
                    #deviceName='WWOUPJ9T99999999',
                    deviceName='20389c54',
                    platformVersion='7.1.2',
                    appPackage='com.youcai.android',
                    appActivity='com.youcai.android.ui.activity.SplashActivity',
>>>>>>> 67559665831ff94eb9f16bc8afd6c0bda9c83fcb
                    unicodeKeyboard=True,
                    resetKeyboard=True)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
