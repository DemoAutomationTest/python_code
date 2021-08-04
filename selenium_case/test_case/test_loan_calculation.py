import pytest
import allure
import sys,os
sys.path.append(os.getcwd())
from Module.base import webdriver_base
from Module.AUTO_HELP import CSV
from Module.AUTO_HELP import DB_Link
from time import sleep
from selenium_case.test_page.loan_calculation import load_rate_1phase,load_rate_2phase,load_rate_3phase,fill_in
class loan_calculation:
    def setup(self):
        self.driver = webdriver_base.Brower('Chrome')
        self.driver.get('https://www.esunbank.com.tw/bank/personal/loan/tools/info/loan-calculation')
        self.driver.implicitly_wait(3)
    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_Period_1part(self):
        fill_in(self.driver, '10', '1', '3', '5000')
        load_rate_1phase(self.driver, '1.11')
    def test_Period_2part(self):
        fill_in(self.driver, '10', '1', '3', '5000')
        load_rate_2phase(self.driver, '3', '1.11','1.33')
if __name__ =="__main__":
    pytest.main(["-s", ".\\selenium_case\\test_case\\test_loan_calculation.py"])

