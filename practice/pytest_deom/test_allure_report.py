import pytest
import os
import allure
import time
current_time=time.strftime("%Y%m%d_%I%M%S",time.localtime())
TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'

@allure.feature('測試需求001:資料庫串接驗證')
@allure.story('測試場景001:查詢簡訊密碼')
@allure.title('測試案例001:查詢結果非空值')
@allure.step('第1個步驟')
@allure.severity(allure.severity_level.BLOCKER)
@allure.link('https://www.youtube.com/watch?v=4YYzUTYZRMU',name='点击我看一看youtube吧')
@allure.issue(TEST_CASE_LINK, 'bug issue链接')
@allure.testcase(TEST_CASE_LINK, '测试用例地址')
def test_case01():
    '''測試註解'''
    assert 1==1
    #插入測試報告
    with allure.step('第1個步驟'):
        with open('./screenshot/2021_06_25_170015.png','rb') as f:
            img =f.read()
        allure.attach(img,'測試截圖')
    with allure.step('第2個步驟'):
        with open('./screenshot/2021_06_25_170015.png','rb') as f:
            img =f.read()
        allure.attach(img,'測試截圖')
    with allure.step('第3個步驟'):
        with open('./screenshot/2021_06_25_170015.png','rb') as f:
            img =f.read()
        allure.attach(img,'測試截圖')

@allure.feature('測試需求001:資料庫串接驗證')
@allure.story('測試場景002:查詢簡訊密碼')
@allure.title('測試案例001:連線異常')
@pytest.mark.skip(reason='本次不執行')
@allure.severity(allure.severity_level.CRITICAL)
def test_case02():
    assert 2==2

@allure.feature('測試需求001:資料庫串接驗證')
@allure.story('測試場景002:查詢簡訊密碼')
@allure.title('測試案例002:查詢失敗')
@allure.severity(allure.severity_level.NORMAL)
def test_case03():
    assert 2==3

if __name__ == '__main__':r
    #執行測試腳本並產生allure xml測試結果
    pytest.main(['-s','test_allure_report.py','--alluredir','D:\\Python_Code\\pytest_deom\\allure_result\\0001'])
    #將XML轉成HTML測試報告格
    os.system('allure generate D:\\Python_Code\\pytest_deom\\allure_result\\0001 -o D:\\Python_Code\\pytest_deom\\allure_report\\0001 --clean')
