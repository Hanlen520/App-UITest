# coding=utf-8
from common.getDriver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.logs import log

log = log()

driver.find_element_by_id("com.waka:id/edt_login_email").send_keys("test1@example.com")
driver.find_element_by_id("com.waka:id/edt_login_password").send_keys("123")
driver.find_element_by_id("com.waka:id/btn_login").click()



def get_Toast(message):
    try:
        mes = '//*[contains(@text,\'{}\')]'.format(message)
        element = WebDriverWait(driver, 5, 0.5).until(
            EC.presence_of_element_located((By.XPATH, mes)))
        log.info('查找到toast：'+'%s'%(element.text))
    except:
        log.error('没有查找到toast：'+'%s'%(message))

get_Toast(u'密码错误')
