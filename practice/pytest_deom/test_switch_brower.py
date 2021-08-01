import pytest,allure,os
from Module.AUTO_HELP import Brower,CSV
from time import sleep


test_data=CSV('.\\case_demo\\screenshot_websit_testdata.csv','link_url','old_img_name','','','','')
test_url=test_data[0]


@pytest.mark.parametrize('link',test_url)
@pytest.mark.parametrize('brower',('Chrome','Firefox','Edge'))
@allure.title("瀏覽器切換驗證_")
def test_switch_brower(brower,link):
    driver=Brower(brower)
    driver.implicitly_wait(5)
    driver.get(link)
    driver.quit()

if __name__  == "__main__":
    pytest.main(['-s','test_switch_brower.py','--alluredir','.\\pytest_deom\\allure_result\\0008'])
    #將XML轉成HTML測試報告格
    os.system('allure generate .\\pytest_deom\\allure_result\\0008 -o .\\pytest_deom\\allure_report\\0008  --clean')

