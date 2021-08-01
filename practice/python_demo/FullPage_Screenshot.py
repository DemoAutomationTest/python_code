"""
使用headless 擷取全網頁截圖
僅Chrome/Firefox可用
"""
from io import SEEK_CUR
from re import S
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


import csv
from time import sleep
from datetime import datetime

CurrentTime=datetime.now().strftime('%Y_%m_%d_%H%M%S')
image_name=str(CurrentTime) + '.png'

options_chrome=webdriver.ChromeOptions()
options_chrome.headless = True
options_firefox=webdriver.FirefoxOptions()
options_firefox.headless =True


#driver=webdriver.Chrome(chrome_options=options_chrome)
driver=webdriver.Firefox(firefox_options=options_firefox)


driver.get("https://www.esunbank.com.tw")
title=driver.title
driver.implicitly_wait(5)

sleep(1)
#scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
#scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
#driver.set_window_size(scroll_width, scroll_height)

driver.find_element_by_tag_name('body').screenshot('.\\screenshot\\'+image_name)

print('screenshoot done')
driver.quit()


