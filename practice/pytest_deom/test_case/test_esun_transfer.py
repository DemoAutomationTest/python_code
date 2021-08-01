import pytest
#跨目錄引用Module
import sys,os
sys.path.append(os.getcwd())
from Module.base import webdriver_base
import allure
from pytest_deom.test_page.login_out import login, logout
from pytest_deom.test_page.NTD_transfer import transfer
from time import sleep
class Test_transer:
    def setup(self):
        self.driver=webdriver_base.Brower('Chrome')
        self.driver.get('https://ebank.esunbank.com.tw')
        self.driver.implicitly_wait(3)
        self.driver.switch_to_frame("iframe1")
        sleep(2)
        login(self.driver,"f125351228","toonice123","njru04fup1982")
    def teardown(self):
        logout(self.driver)
        sleep(3)
        self.driver.quit()
        sleep(1)
    @pytest.mark.parametrize("amount",[100,1000])
    @allure.title("台幣轉帳_立即交易_轉入本行帳戶_成功")
    def test_001(self,amount):
        transfer(self.driver,"0462968079477 自訂台幣主帳戶",("1","0000888463726789 匯豐台灣 蘇建欽 滙豐"),amount)
        sleep(2)
    def test_002(self):
        transfer(self.driver,"0462968079477 自訂台幣主帳戶",("2","808","9999123123123"),"222")
        sleep(2)
    def test_003(self):
        transfer(self.driver,"0462968079477 自訂台幣主帳戶",("1","0000020004078522 臺灣銀行 蘇建欽 臺銀"),"333")
        sleep(2)


if __name__ =="__main__":
    # pytest.main(["-s","D:\\Python_Code\\pytest_deom\\test_case\\test_esun_transfer.py"])
    pytest.main(["-s",".\\pytest_deom\\test_case\\test_esun_transfer.py"])