# coding=utf-8

import os
import time
import logging

# 使用相对路径+绝对路径
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
# log_path = PATH("D:\\Study-Appium\\log\\")
log_path = PATH('/Users/xintudoutest/github/Appium/log/')

class log():
    def __init__(self):
        # 设置log文件名称
        filename = 'Quanquan'+''.join(time.strftime('%Y%m%d'))+''.join('.log')
        self.logname = os.path.join(log_path, filename)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 设置日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] - %(message)s')

    # 打印log信息，level：日志等级，message：日志需要打印的信息
    def output(self, level, message):

        # send logging output to a disk file
        fh = logging.FileHandler(self.logname, 'a')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # send logging output to streams
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level =='debug':
            self.logger.debug(message)
        elif level =='warn':
            self.logger.warn(message)
        elif level =='error':
            self.logger.error(message)

        # 防止重复打印
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)

        fh.close()

    def info(self, message):
        self.output('info', message)

    def debug(self, message):
        self.output('debug', message)

    def warn(self, message):
        self.output('warn', message)

    def error(self, message):
        self.output('error', message)

