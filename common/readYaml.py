# coding=utf-8

import yaml
from common.logs import log

log = log()

# 读取yaml文件，返回testcase的信息
class readyaml:

    # path：文件路径
    def __init__(self, path):
        self.path = path

    # 读取yaml文件
    def readYaml(self):
        try:
            f = open(self.path, encoding='utf-8')
            data = yaml.load(f)
            f.close()
            return data
        except Exception:
            log.error('未找到yaml文件')
            # print(u"未找到yaml文件")

    def alldata(self):
        data = self.readYaml()
        return data

    # 获取case的个数
    def caselen(self):
        data = self.alldata()
        length = len(data['testcase'])
        return length

    # 获取element_info信息
    def get_elementinfo(self, i):
        data = self.alldata()
        return data['testcase'][i]['element_info']

    # 获取find_type信息
    def get_findtype(self, i):
        data = self.alldata()
        return data['testcase'][i]['find_type']

    # 获取operate_type信息
    def get_operate_type(self, i):
        data = self.alldata()
        return data['testcase'][i]['operate_type']

    # 获取index信息
    def get_index(self, i):
        data = self.alldata()
        if self.get_findtype(i) == 'ids':
            return data['testcase'][i]['index']
        else:
            pass

    # 获取要输入的内容
    def get_send_content(self, i):
        data = self.alldata()
        if self.get_operate_type(i) == 'send_keys':
            return data['testcase'][i]['send_content']
        else:
            pass

    # 获取返回和滑动的次数
    def get_backtimes(self, i):
        data = self.alldata()
        if self.get_operate_type(i) == 'back' or self.get_operate_type(i) == 'swipe_up' or self.get_operate_type(i) == 'swipe_down':
            return data['testcase'][i]['times']
        else:
            pass

    def get_title(self):
        data = self.alldata()
        return data['testinfo'][0]['title']

