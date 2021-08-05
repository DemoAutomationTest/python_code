import pytest
import allure
import sys,os
os.chdir("\\python_code")
sys.path.append(os.getcwd())
from Module.base import webdriver_base
from Module.AUTO_HELP import CSV
from Module.AUTO_HELP import DB_Link
from time import sleep

from selenium_case.test_page.loan_calculation import PC_load_rate_1phase,PC_load_rate_2phase,PC_load_rate_3phase,M_load_rate_1phase,M_load_rate_2phase,M_load_rate_3phase,fill_in

class Test_loan_calculation:
    def setup(self):
        self.driver = webdriver_base.Brower('Chrome')
        self.driver.get('https://www.esunbank.com.tw/bank/personal/loan/tools/info/loan-calculation')
        self.driver.implicitly_wait(3)
    def teardown(self):
        sleep(5)
        self.driver.quit()

    def test_Period_1part_M(self):
        fill_in(self.driver,'M', '10', '1', '3', '5000')
        M_load_rate_1phase(self.driver, '1.11')

    def test_Period_2part_M(self):
        fill_in(self.driver,'M', '10', '1', '3', '5000')
        M_load_rate_2phase(self.driver, '3', '1.11','1.33')

    def test_Period_3part_M(self):
        fill_in(self.driver,'M', '10', '1', '3', '5000')
        M_load_rate_3phase(self.driver, '3','7', '1.11','1.33','1.45')

    def test_Period_1part_PC(self):
        fill_in(self.driver,'M', '10', '1', '3', '5000')
        PC_load_rate_1phase(self.driver, '1.11')

    def test_Period_2par_PCt(self):
        fill_in(self.driver,'M', '10', '1', '3', '5000')
        PC_load_rate_2phase(self.driver, '3', '1.11','1.33')

    def test_Period_2part_PC(self):
        fill_in(self.driver,'M', '10', '1', '3', '5000')
        PC_load_rate_3phase(self.driver, '3','7', '1.11','1.33','1.45')

if __name__ =="__main__":
    pytest.main(["-s", ".\\selenium_case\\test_case\\test_loan_calculation.py"])

