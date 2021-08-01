from Module.base import webdriver_base
from time import sleep

driver=webdriver_base.Mobile_Brower(1440,768)
driver.get("https://momoshop.com.tw")
sleep(2)
driver.find_element_by_link_text("看看買").click()
sleep(1)
driver.back()
sleep(1)
driver.quit()
