from Module.base import webdriver_base
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
def transfer(driver,transfer_from,transfer_to,amount):
    #進入功能
    webdriver_base.wait_element_by_xpath(driver,'//*[@id="head"]/div[2]/div/ul/li[2]/a/div/p').click()
    sleep(1)
    webdriver_base.wait_element_by_xpath(driver,'//*[@id="FCP"]/ul/li[2]/ul[1]/li[1]/a').click()
    sleep(1)
    #繳費操作
    #選擇轉出帳號
    select = Select(webdriver_base.wait_element_by_id(driver,"fcp03003:dract"))
    sleep(1)
    select.select_by_visible_text(transfer_from)
    sleep(1)
    #選擇轉入帳號
    if transfer_to[0] =="1":
        webdriver_base.wait_element_by_id(driver,"fcp03003:cractrdo1").click()
        sleep(1)
        select = Select(webdriver_base.wait_element_by_id(driver,"fcp03003:cract1"))
        select.select_by_visible_text(transfer_to[1])
        sleep(1)

    elif transfer_to[0] =="2":
        webdriver_base.wait_element_by_id(driver,"fcp03003:cractrdo3").click()
        sleep(1)
        webdriver_base.wait_element_by_id(driver,"fcp03003:bankCode").send_keys(transfer_to[1])
        sleep(1)
        webdriver_base.wait_element_by_id(driver,"fcp03003:cract3").send_keys(transfer_to[2])
        sleep(1)
    #輸入金額
    webdriver_base.wait_element_by_id(driver,"fcp03003:amt").clear()
    webdriver_base.wait_element_by_id(driver,"fcp03003:amt").send_keys(amount)