import os,sys

from numpy import select
sys.path.append(os.getcwd())
from Module.base import webdriver_base
from time import sleep
from selenium.webdriver.support.ui import Select
driver=webdriver_base.Brower("Chrome")

driver.get("https://www.esunbank.com.tw/bank/about/services/customer/message-board")

driver.implicitly_wait(3)
# 透過改變網頁JS將隱藏的select顯示出來
js = 'document.querySelectorAll("select")[2].style.display="block";'
driver.execute_script(js)
dropdwon=driver.find_element_by_id('salesType')

select =Select(dropdwon)

select.select_by_value("信用卡緩繳展延")
sleep(5)
select.select_by_index(3)
sleep(5)





driver.get("https://www.esunbank.com.tw")
sleep(2)
driver.find_element_by_id("btnAntiFraud").click()
js = 'document.querySelectorAll("li class")[2].style.display="block";'
driver.execute_script(js)
sleep(2)
driver.find_element_by_xpath('//*[@id="mainform"]/div[5]/div/ul/li[2]/div[1]').click()
sleep(2)
# driver.switch_to_frame('layout_0_maincontent_4_IframeTool')
driver.switch_to_frame(1)
sleep(3)
driver.find_element_by_id("amount").send_keys("100")
sleep(3)
# driver.find_element_by_link_text("網銀換匯更划算").click()
select=Select(driver.find_element_by_id("Select1"))
select.select_by_value("USD")
select.select_by_index(1)
sleep(3)
driver.quit()
