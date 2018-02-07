# coding=utf-8
from devices.ios_device import driver
from public.screenshot import screenshot


#通过classname查找元素，进行断言
def assertion_class(self, id):
    try:
        assert self == driver.find_element_by_class_name(id).text
    except Exception as msg:
        print(u'测试未通过%s'%msg)
        screenshot()
        raise


#通过resourceid查找元素，进行断言
def assertion_resourceid(self, id):
    try:
        assert self == driver.find_element_by_id(id).text
    except Exception as msg:
        print(u'测试未通过%s'%msg)
        screenshot()
        raise


#通过name查找元素是否存在，进行断言
def assertion_name(name):
    try:
        assert driver.find_element_by_name(name).is_displayed()
    except Exception as msg:
        print(u'测试未通过%s' % msg)
        screenshot()
        raise