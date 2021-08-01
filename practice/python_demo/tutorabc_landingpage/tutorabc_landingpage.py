import sys
import os
o_path = os.getcwd()
sys.path.append(o_path)
from Module.base import webdriver_base
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from numpy import NaN
import pandas
from Module.AUTO_HELP import CSV
test_data=CSV('.\\practice\\python_demo\\tutorabc_landingpage\\tutorabc_landingpage.csv','link_url','name','mail','','','')
print(test_data)


driver=webdriver_base.Brower('Chrome')

#def test_error_name():
for i in test_data[0]:
    driver.get(i)
    driver.implicitly_wait(3)
    for name_list in test_data[1]:
        driver.find_element_by_id('name').send_keys(name_list)
        sleep (1)
        ActionChains(driver).move_by_offset(1,1).click().perform()
        sleep (1)
        error_msg=driver.find_element_by_class_name('meg-error').text
        print(error_msg)
        driver.refresh()
    for mail_list in test_data[2]:
    #['test','test@@','test@mail']:
        driver.find_element_by_id('name').send_keys('填表測試')
        driver.find_element_by_id('mail').send_keys(mail_list)
        sleep (1)
        ActionChains(driver).move_by_offset(1,1).click().perform()
        sleep (1)
        error_msg=driver.find_element_by_class_name('meg-error').text
        print(error_msg)
        driver.refresh()
    print('完成URL 1')
driver.quit()
