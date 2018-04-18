# coding=utf-8

from common.readYaml import readyaml
from common.baseOperate import BaseOperate

class Operate:
    def __init__(self, path, driver):
        self.path = path
        self.driver = driver
        self.yaml = readyaml(self.path)
        self.baseoperate = BaseOperate(driver)

    def check_operate_type(self):

        """
            # 读取yaml的信息并执行
            # element_info：定位的元素信息
            # find_type：id、xpath、text、ids
            # operate_type: click、send_keys、back、swipe_up、swipe_down、show
            # send_content：执行send_keys时，要输入的内容
            # index：ids时用到，元素组的第几位
            # times: swpie和back的次数
        """

        for i in range(self.yaml.caselen()):

            if self.yaml.get_operate_type(i) == 'click':
                self.driver.implicitly_wait(3)
                if self.yaml.get_findtype(i) == 'text':
                    self.baseoperate.get_name(self.yaml.get_elementinfo(i)).click()
                elif self.yaml.get_findtype(i) == 'id':
                    self.baseoperate.get_id(self.yaml.get_elementinfo(i)).click()
                elif self.yaml.get_findtype(i) == 'xpath':
                    self.baseoperate.get_xpath(self.yaml.get_elementinfo(i)).click()
                elif self.yaml.get_findtype(i) == 'ids':
                    self.baseoperate.get_ids(self.yaml.get_elementinfo(i))[self.yaml.get_index(i)].click()

            elif self.yaml.get_operate_type(i) == 'send_keys':
                self.driver.implicitly_wait(3)
                if self.yaml.get_findtype(i) == 'text':
                    self.baseoperate.get_name(self.yaml.get_elementinfo(i)).send_keys(self.yaml.get_send_content(i))
                elif self.yaml.get_findtype(i) == 'id':
                    self.baseoperate.get_id(self.yaml.get_elementinfo(i)).send_keys(self.yaml.get_send_content(i))
                elif self.yaml.get_findtype(i) == 'xpath':
                    self.baseoperate.get_xpath(self.yaml.get_elementinfo(i)).send_keys(self.yaml.get_send_content(i))
                elif self.yaml.get_findtype(i) == 'ids':
                    self.baseoperate.get_ids(self.yaml.get_elementinfo(i))[self.yaml.get_index(i)].send_keys(self.yaml.get_send_content(i))

            elif self.yaml.get_operate_type(i) == 'show':
                if self.yaml.get_findtype(i) == 'text':
                    self.baseoperate.get_name(self.yaml.get_elementinfo(i))
                elif self.yaml.get_findtype(i) == 'toast':
                    self.baseoperate.get_toast(self.yaml.get_elementinfo(i))

            elif self.yaml.get_operate_type(i) == 'back':
                for n in range(self.yaml.get_backtimes(i)):
                    self.baseoperate.back()

            elif self.yaml.get_operate_type(i) == 'swipe_up':
                for n in range(self.yaml.get_backtimes(i)):
                    self.baseoperate.swipeUp()

            elif self.yaml.get_operate_type(i) == 'swipe_down':
                for n in range(self.yaml.get_backtimes(i)):
                    self.baseoperate.swipeDown()

    # 返回首页
    def back_home(self):
        self.baseoperate.backpage(u'推荐')
