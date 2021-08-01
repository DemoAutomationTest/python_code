#coding=utf-8
'''
切換iFrame
'''

from Module.AUTO_HELP import Brower
from time import sleep
driver=Brower('Chrome')
driver.implicitly_wait(5)
driver.get('https://www.esunbank.com.tw/bank/personal/wealth/stock/us-list')
try:
    driver.switch_to_frame('layout_0_rightcontent_1_CustomIframe')
    sleep(2)
    driver.find_element_by_link_text('1W').click()
    sleep(5)
    driver.quit()
except:
    driver.quit()
