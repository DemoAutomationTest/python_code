#coding=utf-8
'''
隱性等待物件
顯性等待物件
'''

from Module.AUTO_HELP import Brower
from time import sleep
driver=Brower('Chrome')
driver.implicitly_wait(60)
driver.get('https://www.google.com.tw')
try:
    driver.find_element_by_name('q').send_keys('123')
    sleep(3)
    driver.find_element_by_link_text('關於 2Google').click()
    sleep(3)
    driver.quit()
except:
    driver.quit()
