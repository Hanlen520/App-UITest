# coding=utf-8

import os
from common.readConfig import Readconfig
from common.logs import log

conf = Readconfig()
log = log()

class devices:
    def __init__(self):
        # 从config配置文件中获取adb命令
        self.get_device = conf.getcmdValue('viewPhone')
        self.get_Version = conf.getcmdValue('viewAndroid')

    # 执行adb命令，打印出设备名称
    def get_deviceName(self):
        values = os.popen(self.get_device).readlines()
        dev = values[1].split()[0]
        if len(values)-2 == 1:
            log.info('手机设备为：'+dev)
            return dev
        else:
            log.warn('暂未获取到手机设备')

    # 执行adb命令，打印出设备版本号
    def get_platformVersion(self):
        values = os.popen(self.get_Version).readlines()
        if values != '':
            Version = values[0].split('=')[1]
            log.info('手机版本号为：'+Version)
            return Version.strip()
        else:
            log.warn('暂未获取到手机设备')


if __name__ == '__main__':
    cmd = devices()
    cmd.get_deviceName()
    cmd.get_platformVersion()
