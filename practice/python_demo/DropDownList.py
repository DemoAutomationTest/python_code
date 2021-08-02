import os,sys

from numpy import select
sys.path.append(os.getcwd())
from Module.base import webdriver_base
from time import sleep
from selenium.webdriver.support.ui import Select
driver=webdriver_base.Brower("Chrome")

driver.get("https://www.esunbank.com.tw/bank/about/services/customer/message-board")
sleep(2)
driver.implicitly_wait(3)
select = Select(driver.find_element_by_xpath('//*[@id="dealingCity"]'))
select.select_by_visible_text("嘉義縣")





# driver.get("https://www.esunbank.com.tw")
# sleep(2)
# driver.find_element_by_id("btnAntiFraud").click()
# sleep(2)
# driver.find_element_by_xpath('//*[@id="mainform"]/div[5]/div/ul/li[2]/div[1]').click()
# sleep(2)
# # driver.switch_to_frame('layout_0_maincontent_4_IframeTool')
# driver.switch_to_frame(1)
# sleep(3)
# driver.find_element_by_id("amount").send_keys("100")
# sleep(3)
# # driver.find_element_by_link_text("網銀換匯更划算").click()
# select=Select(driver.find_element_by_id("Select1"))
# select.select_by_value("USD")
# select.select_by_index(1)
sleep(3)
driver.quit()
