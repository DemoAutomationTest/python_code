import allure
import pytest
from selenium import webdriver
import time
import os
from Module.AUTO_HELP import Brower


@allure.testcase("http://www.github.com")
@allure.feature("百度搜尋")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest'])
def test_steps_demo(test_data1):
    with allure.step("打開網頁"):
        driver = Brower('Chrome')
        driver.get("http://www.google.com")

    with allure.step("搜尋關鍵字"):
        driver.find_element_by_name("q").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_name("btnK").click()
        time.sleep(2)

    with allure.step("截圖"):
        driver.save_screenshot("./screenshotb.png")
        allure.attach.file("./screenshotb.png",name='頁面截圖', attachment_type=allure.attachment_type.PNG)
        allure.attach('<head></head><body>首页</body>', 'Attach with HTML type', allure.attachment_type.HTML)

    with allure.step("退出瀏覽器"):
        driver.quit()

if __name__ == '__main__':
    #執行測試腳本並產生allure xml測試結果
    pytest.main(['-s','test_allure_baidu.py','--alluredir','.\\pytest_deom\\allure_result\\0003'])
    #將XML轉成HTML測試報告格
    os.system('allure generate .\\pytest_deom\\allure_result\\0003 -o .\\pytest_deom\\allure_report\\0003 --clean')