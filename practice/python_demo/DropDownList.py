import os,sys
sys.path.append(os.getcwd())
from Module.base import webdriver_base
from time import sleep
from selenium.webdriver.support.ui import Select
driver=webdriver_base.Brower("Chrome")

driver.get("https://www.esunbank.com.tw/bank/about/services/customer/message-board")

driver.implicitly_wait(3)
# 透過改變網頁JS將隱藏的select顯示出來
# https://zhuanlan.zhihu.com/p/97189984

js = 'document.querySelectorAll("select")[2].style.display="block";'
driver.execute_script(js)
dropdwon=driver.find_element_by_id('salesType')

select =Select(dropdwon)

select.select_by_value("信用卡緩繳展延")
sleep(5)
select.select_by_index(3)
sleep(5)
driver.quit()
