#coding=utf-8
'''
隱性等待物件
顯性等待物件
'''
import sys,os
sys.path.append(os.getcwd())
from Module.base import webdriver_base
from time import sleep

driver=webdriver_base.Brower('Chrome')
driver.implicitly_wait(60)
driver.get('https://www.esunbank.com.tw')
try:
    sleep(3)

    driver.switch_to_alert
    driver.find_element_by_id('btnAntiFraud').click()
    sleep(3)
    driver.find_element_by_link_text('存匯').click()

    sleep(3)
    driver.quit()
except:
    driver.quit()
