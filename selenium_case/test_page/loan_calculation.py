from Module.base import webdriver_base
from time import sleep

sec=1
def fill_in(driver,device,amount,loanPeriod,ExMonth,Fee):
    if device == 'PC':
        webdriver_base.wait_element_by_id(driver, "TxtloanAmount").send_keys(amount)
        webdriver_base.wait_element_by_id(driver, "TxtloanPeriod").send_keys(loanPeriod)
        webdriver_base.wait_element_by_id(driver, "TxtExMonth").send_keys(ExMonth)
        webdriver_base.wait_element_by_id(driver, "TxtFee").send_keys(Fee)
    elif device =="M":
        webdriver_base.wait_element_by_id(driver, "layout_0_maincontent_0_HlkToMobile").click()
        sleep(sec)
        webdriver_base.wait_element_by_id(driver, "TxtloanAmount").send_keys(amount)
        webdriver_base.wait_element_by_id(driver, "TxtloanPeriod").send_keys(loanPeriod)
        webdriver_base.wait_element_by_id(driver, "TxtExMonth").send_keys(ExMonth)
        webdriver_base.wait_element_by_id(driver, "TxtFee").send_keys(Fee)

def PC_load_rate_1phase(driver,TxtRate1):
    webdriver_base.wait_element_by_id(driver, "rbPeriodTimes1").click()
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate1").send_keys(TxtRate1)
    sleep(sec)
    webdriver_base.wait_element_by_xpath(driver, '//*[@id="LbtnCalculate"]').click()

def PC_load_rate_2phase(driver,TxtPeriodEnd1,TxtRate1,TxtRate2):
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "rbPeriodTimes2").click()
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtPeriodEnd1").send_keys(TxtPeriodEnd1)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate1").send_keys(TxtRate1)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate2").send_keys(TxtRate2)
    sleep(sec)
    webdriver_base.wait_element_by_xpath(driver, '//*[@id="LbtnCalculate"]').click()

def PC_load_rate_3phase(driver,TxtPeriodEnd1,TxtPeriodEnd2,TxtRate1,TxtRate2,TxtRate3):
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "rbPeriodTimes3").click()
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtPeriodEnd1").send_keys(TxtPeriodEnd1)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate1").send_keys(TxtRate1)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtPeriodEnd2").send_keys(TxtPeriodEnd2)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate2").send_keys(TxtRate2)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate3").send_keys(TxtRate3)
    sleep(sec)
    webdriver_base.wait_element_by_xpath(driver, '//*[@id="LbtnCalculate"]').click()

def M_load_rate_1phase(driver,TxtRate1):
    webdriver_base.wait_element_by_xpath(driver, '//*[@id="mainContent"]/div/div[3]/div/div/div/div[2]/div[2]/div[4]/div[2]/ul/li[1]').click()
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate1").send_keys(TxtRate1)
    sleep(sec)
    webdriver_base.wait_element_by_xpath(driver, '//*[@id="LbtnCalculate"]').click()

def M_load_rate_2phase(driver,TxtPeriodEnd1,TxtRate1,TxtRate2):
    sleep(sec)
    webdriver_base.wait_element_by_xpath(driver, '//*[@id="mainContent"]/div/div[3]/div/div/div/div[2]/div[2]/div[4]/div[2]/ul/li[2]').click()
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtPeriodEnd1").send_keys(TxtPeriodEnd1)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate1").send_keys(TxtRate1)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate2").send_keys(TxtRate2)
    sleep(sec)
    webdriver_base.wait_element_by_xpath(driver, '//*[@id="LbtnCalculate"]').click()

def M_load_rate_3phase(driver,TxtPeriodEnd1,TxtPeriodEnd2,TxtRate1,TxtRate2,TxtRate3):
    sleep(sec)
    webdriver_base.wait_element_by_xpath(driver, '//*[@id="mainContent"]/div/div[3]/div/div/div/div[2]/div[2]/div[4]/div[2]/ul/li[3]').click()
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtPeriodEnd1").send_keys(TxtPeriodEnd1)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate1").send_keys(TxtRate1)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtPeriodEnd2").send_keys(TxtPeriodEnd2)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate2").send_keys(TxtRate2)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate3").send_keys(TxtRate3)
    sleep(sec)
    webdriver_base.wait_element_by_xpath(driver, '//*[@id="LbtnCalculate"]').click()