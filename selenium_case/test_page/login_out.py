from Module.base import webdriver_base
from selenium.webdriver.common.keys import Keys
def login(driver,id,name,password):
    webdriver_base.wait_element_by_id(driver,'loginform:custid').send_keys(id)
    webdriver_base.wait_element_by_id(driver,'loginform:name').send_keys(name)
    webdriver_base.wait_element_by_id(driver,'loginform:pxsswd').send_keys(password)
    webdriver_base.wait_element_by_id(driver,'loginform:linkCommand').click()
def logout(driver):
    driver.find_element_by_link_text("登出").click()