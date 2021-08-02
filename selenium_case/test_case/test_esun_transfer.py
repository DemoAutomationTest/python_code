import pytest
import allure
import sys,os
sys.path.append(os.getcwd())
print(os.getcwd())
from Module.base import webdriver_base
from Module.AUTO_HELP import DB_Link

from selenium_case.test_page.login_out import login, logout
from selenium_case.test_page.NTD_transfer import transfer
from time import sleep
test_account=DB_Link("select * from esun_account")
class Test_transer:
    def setup(self):
        self.driver=webdriver_base.Brower('Chrome')
        self.driver.get('https://ebank.esunbank.com.tw')
        self.driver.implicitly_wait(3)
        self.driver.switch_to_frame("iframe1")
        sleep(2)
        global test_account
        login(self.driver,test_account[0],test_account[1],test_account[2])
    def teardown(self):
        logout(self.driver)
        sleep(3)
        self.driver.quit()
        sleep(1)
    @pytest.mark.parametrize("amount",[100,1000])
    @allure.title("台幣轉帳_立即交易_轉入本行帳戶_成功")
    def test_001(self,amount):
        transfer(self.driver,"04629XXXXX7 自訂台幣主帳戶",("1","00008XXXX726789 匯豐台灣 滙豐"),amount)
        sleep(2)
    def test_002(self):
        transfer(self.driver,"04629XXXXX7 自訂台幣主帳戶",("2","808","9999XXX3123"),"222")
        sleep(2)
    def test_003(self):
        transfer(self.driver,"04629XXXXX7 自訂台幣主帳戶",("1","000002000XXX522 臺灣銀行 臺銀"),"333")
        sleep(2)


if __name__ =="__main__":
    pytest.main(["-s",".\\selenium_case\\test_case\\test_esun_transfer.py"])