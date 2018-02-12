# coding=utf-8
from devices.ios_device import driver


def id_sendkeys(self, text):
    driver.find_element_by_id(self).send_keys(text)

def xpath_sendkeys(self, text):
    driver.find_element_by_xpath(self).send_keys(text)