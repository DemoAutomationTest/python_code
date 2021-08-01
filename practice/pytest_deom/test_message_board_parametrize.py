#coding=utf-8
from threading import current_thread
import Module.AUTO_HELP as help
from datetime import datetime
import pytest
import allure


@allure.title('選擇各縣市分行確認版面正常')
@pytest.mark.parametrize('city_name,city,branch',[('基隆市',1,1),('台北市',2,2),('新北市',3,2),('桃園市',4,4)])
def test_message_board (city_name,city,branch):
    driver=help.Brower('Chrome')
    driver.get('https://www.esunbank.com.tw/bank/about/services/customer/message-board')
    driver.implicitly_wait(5)
    driver.find_element
    try:
        for city_count in range(branch):
            #定義截圖檔名
            with allure.step(city_name+'+第'+str(city_count+1)+'分行'):
                #輸入姓名
                help.wait_element_by_name(driver,'name').send_keys('王大明')
                # driver.find_element_by_name('name').send_keys('王大明')
                #輸入ID
                help.wait_element_by_id(driver,'citizenId').send_keys('A199999999')
                # driver.find_element_by_id('citizenId').send_keys('A199999999')
                #輸入電話
                help.wait_element_by_id(driver,'phone').send_keys('0999123123')
                # driver.find_element_by_id('phone').send_keys('0999123123')
                #輸入email
                help.wait_element_by_id(driver,'email').clear()
                help.wait_element_by_id(driver,'email').send_keys('test@gmail.com')
                # driver.find_element_by_id('email').send_keys('test@gmail.com')
            #選擇分行

            if branch==1: #判斷是否只有1間分行
                #單一分行只選擇縣市
                help.wait_element_by_xpath(driver,'//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[1]/li/span').click()
                # driver.find_element_by_xpath('//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[1]/li/span').click()
                city_path='//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[1]/li/ul/li['+ str(city+1) +']/span'
                help.wait_element_by_xpath(driver,city_path).click()

                # driver.find_element_by_xpath(city_path).click()
            else:
                #多分行選擇縣市
                help.wait_element_by_xpath(driver,'//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[1]/li/span').click()
                # driver.find_element_by_xpath('//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[1]/li/span').click()
                city_path='//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[1]/li/ul/li['+str(city+1)+']/span'
                help.wait_element_by_xpath(driver,city_path).click()
                # driver.find_element_by_xpath(city_path).click()
                #多分行選擇分行
                help.wait_element_by_xpath(driver,'//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[2]/li/span').click()
                # driver.find_element_by_xpath('//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[2]/li/span').click()
                branch_path='//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[2]/li/ul/li['+str(city_count+1)+']/span'
                help.wait_element_by_xpath(driver,branch_path).click()
                # driver.find_element_by_xpath(branch_path).click()

        #選擇留言業務
            help.wait_element_by_xpath(driver,'//*[@id="mainform"]/div[9]/div[4]/div[4]/table/tbody/tr[1]/td[2]/ul/li/span').click()
            help.wait_element_by_xpath(driver,'//*[@id="mainform"]/div[9]/div[4]/div[4]/table/tbody/tr[1]/td[2]/ul/li/ul/li[13]/span').click()
            # driver.find_element_by_xpath('//*[@id="mainform"]/div[9]/div[4]/div[4]/table/tbody/tr[1]/td[2]/ul/li/span').click()
            # driver.find_element_by_xpath('//*[@id="mainform"]/div[9]/div[4]/div[4]/table/tbody/tr[1]/td[2]/ul/li/ul/li[13]/span').click()
            #輸入留言
            help.wait_element_by_id(driver,'layout_0_maincontent_2_comments').send_keys(city_name+'+第'+str(city_count+1)+'分行')
            # driver.find_element_by_id('layout_0_maincontent_2_comments').send_keys(city_name+'+第'+str(city_count+1)+'分行')

            help.sleep(1)
            with allure.step("截圖"):
                help.screen_shot("allure",driver)
                # driver.save_screenshot("./screenshotb.png")
                # allure.attach.file("./screenshotb.png",name='頁面截圖', attachment_type=allure.attachment_type.PNG)
            #截圖
            help.screen_shot("other",driver)
    except:
        with allure.step('執行失敗'):
            print('執行失敗')
            with allure.step("截圖"):
                help.screen_shot("allure",driver)
                # driver.save_screenshot("./screenshot.png")
                # allure.attach.file("./screenshotb.png",name='頁面截圖', attachment_type=allure.attachment_type.PNG)
            driver.quit()

            #驗證須放在最後一行
            assert 1==2

    driver.quit()

# if __name__ == '__main__':
#     #執行測試腳本並產生allure xml測試結果
#     pytest.main(['-s','-q','test_message_board.py','--alluredir','.\\pytest_deom\\allure_result\\0004'])
#     #將XML轉成HTML測試報告格
#     os.system('allure generate .\\pytest_deom\\allure_result\\0004 -o .\\pytest_deom\\allure_report\\0004 --clean')
if __name__ == '__main__':
    #執行測試腳本並產生allure xml測試結果
    pytest.main(['-s','-q','test_message_board_parametrize.py','--alluredir','C:\\Users\\pc\\.jenkins\\workspace\\test_message_board_parametrize\\target\\allure-results'])
    #將XML轉成HTML測試報告格
    #os.system('C:\\Users\\pc\\.jenkins\\workspace\\test_message_board\\target\\allure-results -o C:\\Users\\pc\\.jenkins\\workspace\\test_message_board\\allure-report --clean')