#coding=utf-8
#跨目錄引用Module
import sys
import os
from _pytest.config import main
o_path = os.getcwd()
sys.path.append(o_path)

import pytest
from Module.AUTO_HELP import DB_Link
from Module.AUTO_HELP import OTP
from Module.AUTO_HELP import Brower
from time import sleep
import allure
@pytest.mark.g3 #分類標籤，須同步定義在pytest.ini
@pytest.mark.parametrize('a,b,c' #使用參數化條件，ids可以作為中文名稱或註解
,[(1,2,3),(2,3,5),(3,4,9)],ids=['交易成功','test2','test3'])
def test_add(a,b,c):
    assert a+b == c
    sleep(1)
    print('數學加法測試')

@pytest.mark.g1  #分類標籤，須同步定義在pytest.ini
@allure.feature('資料庫串接驗證')
@allure.story('查詢顧客資料')
@allure.title('查詢結果非空值')
def test_case1():
    '''執行資料庫查詢'''
    sleep(1)

    A='select * from Customer2'
    row=DB_Link(A)
    print('資料庫查詢測試:'+row[1])
    assert row[1] is not None

@allure.feature('資料庫串接驗證')
@allure.story('查詢簡訊密碼')
@allure.title('查詢結果非空值')
@pytest.mark.g1  #分類標籤，須同步定義在pytest.ini
def test_case2():
    sleep(1)
    code='DWR'
    key=OTP(code)
    print(key)
    print('簡訊OTP查詢')
    assert key is not None

@pytest.mark.g2  #分類標籤，須同步定義在pytest.ini
def test_case3():
    #僅支援Chrome/Firefox/IE11/Edge
    driver=Brower('Firefox')
    driver.get("https://www.google.com.tw")
    sleep(3)
    driver.quit()
    print('開啟Firefox瀏覽器')
    assert True
@pytest.mark.order1
@pytest.mark.g1  #分類標籤，須同步定義在pytest.ini
def test_step1 ():
    sleep(3)
    driver=Brower('Edge')
    driver.get("https://www.google.com.tw")
    print('開啟Edge瀏覽器')
    driver.quit()
@pytest.mark.order2
@pytest.mark.g2  #分類標籤，須同步定義在pytest.ini
def test_step2 ():
    sleep(3)
    driver=Brower('Chrome')
    driver.get("https://www.google.com.tw")
    print('開啟Chrome瀏覽器')
    driver.quit()
@pytest.mark.order3
@pytest.mark.g2  #分類標籤，須同步定義在pytest.ini
def test_step3 ():
    sleep(3)
    driver=Brower('Chrome')
    driver.get("https://www.google.com.tw")
    print('開啟Chrome瀏覽器')
    driver.quit()
@pytest.mark.g2  #分類標籤，須同步定義在pytest.ini
def test_step4 ():
    sleep(3)
    driver=Brower('Chrome')
    driver.get("https://www.google.com.tw")
    print('開啟Chrome瀏覽器')
    driver.quit()
@pytest.mark.g2  #分類標籤，須同步定義在pytest.ini
def test_step5 ():
    sleep(3)
    driver=Brower('Chrome')
    driver.get("https://www.google.com.tw")
    print('開啟Chrome瀏覽器')
    driver.quit()
@pytest.mark.g2  #分類標籤，須同步定義在pytest.ini
def test_step6 ():
    sleep(3)
    driver=Brower('Chrome')
    driver.get("https://www.google.com.tw")
    print('開啟Chrome瀏覽器')
    driver.quit()



if __name__ =='__main__':
    pytest.main()

