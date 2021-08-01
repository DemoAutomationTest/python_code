import sys
import os
o_path = os.getcwd()
sys.path.append(o_path)
from socket import MsgFlag
from Module.base import webdriver_base
from time import sleep
from selenium.webdriver.support.ui import Select
from Module.AUTO_HELP import OTP
from Module.AUTO_HELP import OCR
from Module.AUTO_HELP import save_img
driver=webdriver_base.Brower('Chrome')
driver.get('https://ebank.esunbank.com.tw')
driver.implicitly_wait(3)
driver.set_window_size(1440,1080)
driver.switch_to_frame(0)
sleep(2)
# try:
#     driver.find_element_by_id('loginform:custid').send_keys('f125351228')
#     driver.find_element_by_id('loginform:name').send_keys('toonice123')
#     driver.find_element_by_id('loginform:pxsswd').send_keys('njru04fup1982')
#     driver.find_element_by_id('loginform:linkCommand').click()
#     sleep(2)
#     #點MEGA MENU
#     driver.find_element_by_xpath('//*[@id="head"]/div[2]/div/ul/li[2]/a/div/p').click()
#     sleep(2)
#     #點FUNCTION MENU
#     driver.find_element_by_xpath('//*[@id="FCP"]/ul/li[2]/ul[1]/li[1]/a').click()
#     driver.find_element_by_id('fcp03003:cractrdo1').click()
#     select=Select(driver.find_element_by_id('fcp03003:cract1'))
#     select.select_by_visible_text('0000888463726789 匯豐台灣 蘇建欽 滙豐')
#     sleep(2)
#     driver.find_element_by_id('fcp03003:amt').clear()
#     driver.find_element_by_id('fcp03003:amt').send_keys('1')
#     driver.find_element_by_id('fcp03003:linkCommand').click()
#     sleep(2)
#     driver.find_element_by_id('fcp03003:passwd').send_keys('njru04fup1982')
#     driver.find_element_by_id('fcp03003:linkCommands2').click()
#     resurt=driver.find_element_by_xpath('//*[@id="fcp03003"]/table/tbody/tr[1]/td[2]/div')
#     print(resurt.text)
# except Exception as msg:
#     print(msg)
#     driver.find_element_by_link_text('登出').click()
#     driver.refresh()

try:
    driver.find_element_by_id('loginform:custid').send_keys('f125351228')
    driver.find_element_by_id('loginform:name').send_keys('toonice123')
    driver.find_element_by_id('loginform:pxsswd').send_keys('njru04fup1982')
    driver.find_element_by_id('loginform:linkCommand').click()
    sleep(2)
    #點MEGA MENU
    driver.find_element_by_xpath('//*[@id="head"]/div[2]/div/ul/li[2]/a/div/p').click()

    sleep(2)
    #點FUNCTION MENU
    driver.find_element_by_xpath('//*[@id="FCP"]/ul/li[2]/ul[1]/li[1]/a').click()
    driver.find_element_by_id('fcp03003:cractrdo3').click()
    driver.find_element_by_id('fcp03003:bankCode').send_keys('808')
    driver.find_element_by_id('fcp03003:cract3').send_keys('9999999999')
    sleep(2)
    driver.find_element_by_id('fcp03003:amt').clear()
    driver.find_element_by_id('fcp03003:amt').send_keys('1')
    driver.find_element_by_id('fcp03003:securerdo1').click()
    driver.find_element_by_id('fcp03003:linkCommand').click()
    sleep(3)
    driver.find_element_by_id('otpSend').click()
    sleep(5)
    # OTP_TIP=driver.find_element_by_id('otpWebCode').text
    # print(OTP_TIP)
    # OTP_Code=OTP(OTP_TIP)
    # print(OTP_Code)
    # driver.find_element_by_id('fcp03003:otpPassword').send_keys(OTP(OTP_Code))
    sleep(2)
    OCR_img=driver.find_element_by_id('captcha')
    OCR_img.screenshot('ocr_code.png')
    sleep(2)
    OCR_code=OCR('D:\Python Code\ocr_code.png')
    print(OCR_code)
    driver.find_element_by_id('fcp03003:magicNumber').send_keys(OCR_code)
    sleep(2)

    driver.find_element_by_id('fcp03003:linkCommands1').click()
    sleep(2)
    resurt=driver.find_element_by_xpath('//*[@id="fcp03003"]/table/tbody/tr[1]/td[2]/div')
    print(resurt.text)
    driver.find_element_by_link_text('登出').click()
except Exception as msg:
    print(msg)
    driver.find_element_by_link_text('登出').click()
    driver.refresh()

driver.quit()