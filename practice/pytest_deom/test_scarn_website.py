'''
取得http請求結果，驗證網站運行是否正常
'''
import pytest,allure,os,requests
from time import sleep
from Module.AUTO_HELP import Brower
from Module.AUTO_HELP import CSV
test_data=CSV('.\\case_demo\\test.csv','web_title','web_link','','','','')
@pytest.mark.parametrize('link',test_data[1])
# @pytest.mark.parametrize('name',test_data[0])
def test_scarn_website(link):
    with allure.step('檢查網頁瀏覽正常'):
        driver=Brower('Chrome')
        driver.get(link)
        link_status=requests.get(link).status_code
        with allure.step("截圖"):
            driver.save_screenshot("./screenshotb.png")
            allure.attach.file("./screenshotb.png",name='頁面截圖', attachment_type=allure.attachment_type.PNG)
        driver.quit()
        assert link_status == 200
if __name__ == '__main__':
    #執行測試腳本並產生allure xml測試結果
    pytest.main(['-s','-q','test_scarn_website.py','--alluredir','C:\\Users\\pc\\.jenkins\\workspace\\網站掃描\\allure-results'])
    #將XML轉成HTML測試報告格
    # os.system('allure generate D:\\Python_Code\\pytest_deom\\allure_result\\0006 -o D:\\Python_Code\\pytest_deom\\allure_report\\0006 --clean')
