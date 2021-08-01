#coding=utf-8
'''
切換視窗
'''

from Module.AUTO_HELP import Brower
from time import sleep
driver=Brower('Chrome')
driver.implicitly_wait(60)
driver.get('https://www.baidu.com/')
try:
    driver.find_element_by_link_text('新闻').click()
    sleep(10)
    all_handles =driver.window_handles
    driver.switch_to_window(all_handles[0])
    sleep(2)
    driver.quit()
except:
    driver.quit()
