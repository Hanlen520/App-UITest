# coding=utf-8

import os
import configparser

# 获取本文件所在路径
prjDir = os.path.split(os.path.realpath(__file__))[0]
configfile_path = os.path.join(prjDir, "config.ini")

class Readconfig:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(configfile_path)

    def getAppValue(self, name):
        value = self.conf.get('app', name)
        return value

    def getcmdValue(self, name):
        value = self.conf.get('cmd', name)
        return value

    def getemailValue(self, name):
        value = self.conf.get('email', name)
        return value

