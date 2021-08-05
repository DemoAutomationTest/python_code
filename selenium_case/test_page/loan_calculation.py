from Module.base import webdriver_base
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
def fill_in(driver,device,amount,loanPeriod,ExMonth,Fee):
    if device == 'PC':
        webdriver_base.wait_element_by_id(driver, "TxtloanAmount").send_keys(amount)
        webdriver_base.wait_element_by_id(driver, "TxtloanPeriod").send_keys(loanPeriod)
        webdriver_base.wait_element_by_id(driver, "TxtExMonth").send_keys(ExMonth)
        webdriver_base.wait_element_by_id(driver, "TxtFee").send_keys(Fee)
    elif device =="M":
        webdriver_base.wait_element_by_id(driver, "layout_0_maincontent_0_HlkToMobile").click()
        sleep(3)
        webdriver_base.wait_element_by_id(driver, "TxtloanAmount").send_keys(amount)
        webdriver_base.wait_element_by_id(driver, "TxtloanPeriod").send_keys(loanPeriod)
        webdriver_base.wait_element_by_id(driver, "TxtExMonth").send_keys(ExMonth)
        webdriver_base.wait_element_by_id(driver, "TxtFee").send_keys(Fee)
def PC_load_rate_1phase(driver,TxtRate1):
    webdriver_base.wait_element_by_id(driver, "rbPeriodTimes1").click()
    webdriver_base.wait_element_by_id(driver, "TxtRate1").send_keys(TxtRate1)
def PC_load_rate_2phase(driver,TxtPeriodEnd1,TxtRate1,TxtRate2):
    webdriver_base.wait_element_by_id(driver, "rbPeriodTimes2").click()
    webdriver_base.wait_element_by_id(driver, "TxtPeriodEnd1").send_keys(TxtPeriodEnd1)
    webdriver_base.wait_element_by_id(driver, "TxtRate1").send_keys(TxtRate1)
    webdriver_base.wait_element_by_id(driver, "TxtRate2").send_keys(TxtRate2)
def PC_load_rate_3phase(driver,TxtPeriodEnd1,TxtPeriodEnd2,TxtRate1,TxtRate2,TxtRate3):
    webdriver_base.wait_element_by_id(driver, "rbPeriodTimes3").click()
    webdriver_base.wait_element_by_id(driver, "TxtPeriodEnd1").send_keys(TxtPeriodEnd1)
    webdriver_base.wait_element_by_id(driver, "TxtRate1").send_keys(TxtRate1)
    webdriver_base.wait_element_by_id(driver, "TxtPeriodEnd2").send_keys(TxtPeriodEnd2)
    webdriver_base.wait_element_by_id(driver, "TxtRate2").send_keys(TxtRate2)
    webdriver_base.wait_element_by_id(driver, "TxtRate3").send_keys(TxtRate3)
