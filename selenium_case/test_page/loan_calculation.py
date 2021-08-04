from Module.base import webdriver_base
from time import sleep
sec = 1
def fill_in(driver,amount,loanPeriod,ExMonth,Fee):
    webdriver_base.wait_element_by_id(driver, "TxtloanAmount").send_keys(amount)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtloanPeriod").send_keys(loanPeriod)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtExMonth").send_keys(ExMonth)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtFee").send_keys(Fee)

def load_rate_1phase(driver,TxtRate1):
    webdriver_base.wait_element_by_id(driver, "rbPeriodTimes1").click()
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate1").send_keys(TxtRate1)
    sleep(sec)
    webdriver_base.wait_element_by_xpath(driver, '//*[@id="LbtnCalculate"]').click()

def load_rate_2phase(driver,TxtPeriodEnd1,TxtRate1,TxtRate2):
    webdriver_base.wait_element_by_id(driver, "rbPeriodTimes2").click()
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtPeriodEnd1").send_keys(TxtPeriodEnd1)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate1").send_keys(TxtRate1)
    sleep(sec)
    webdriver_base.wait_element_by_id(driver, "TxtRate2").send_keys(TxtRate2)
    sleep(sec)
    webdriver_base.wait_element_by_xpath(driver, '//*[@id="LbtnClear"]').click()

def load_rate_3phase(driver,TxtPeriodEnd1,TxtPeriodEnd2,TxtRate1,TxtRate2,TxtRate3):
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
    webdriver_base.wait_element_by_xpath(driver, '//*[@id="LbtnClear"]').click()