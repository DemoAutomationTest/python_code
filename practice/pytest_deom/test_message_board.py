#coding=utf-8
from threading import current_thread
from Module.AUTO_HELP import Brower,screen_shot
from selenium.webdriver.support.ui import Select
from time import sleep
from datetime import datetime
import pytest
import allure
import os



class Test_message_board(object):
    @allure.title('選擇各縣市分行確認版面正常')
    def test_message_board (self):
        driver=Brower('Chrome')
        driver.get('https://www.esunbank.com.tw/bank/about/services/customer/message-board')
        driver.implicitly_wait(5)
        branch_count=[2,1,1,1] #實際分行數
        x=0
        while x < 4: #執行縣市數
            run_time=branch_count[x]
            try:
                for city_count in range(run_time):
                    #定義截圖檔名
                    CurrentTime=datetime.now().strftime('%Y_%m_%d_%H%M%S')
                    image_name=str(CurrentTime) + '.png'
                    with allure.step('第'+str(x+1)+'縣市+第'+str(city_count+1)+'分行'):
                        #輸入姓名
                        driver.find_element_by_name('name').send_keys('王大明')
                        #輸入ID
                        driver.find_element_by_id('citizenId').send_keys('A199999999')
                        #輸入電話
                        driver.find_element_by_id('phone').send_keys('0999123123')
                        #輸入email
                        driver.find_element_by_id('email').send_keys('0718test@gmail.com')
                    #選擇分行

                    if run_time==1: #判斷是否只有1間分行
                        #單一分行只選擇縣市
                        driver.find_element_by_xpath('//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[1]/li/span').click()
                        city_path='//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[1]/li/ul/li['+str(x+2)+']/span'
                        driver.find_element_by_xpath(city_path).click()
                    else:
                        #多分行選擇縣市
                        driver.find_element_by_xpath('//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[1]/li/span').click()
                        city_path='//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[1]/li/ul/li['+str(x+2)+']/span'
                        driver.find_element_by_xpath(city_path).click()
                        #多分行選擇分行
                        driver.find_element_by_xpath('//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[2]/li/span').click()
                        branch_path='//*[@id="mainform"]/div[9]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/ul[2]/li/ul/li['+str(city_count+1)+']/span'
                        driver.find_element_by_xpath(branch_path).click()

                #選擇留言業務
                    driver.find_element_by_xpath('//*[@id="mainform"]/div[9]/div[4]/div[4]/table/tbody/tr[1]/td[2]/ul/li/span').click()
                    driver.find_element_by_xpath('//*[@id="mainform"]/div[9]/div[4]/div[4]/table/tbody/tr[1]/td[2]/ul/li/ul/li[13]/span').click()
                    #輸入留言
                    driver.find_element_by_id('layout_0_maincontent_2_comments').send_keys('第'+str(x+1)+'縣市+第'+str(city_count+1)+'分行')

                    sleep(1)
                    with allure.step("截圖"):
                        screen_shot("allure",driver)
                        screen_shot("other",driver)
                        # driver.save_screenshot("./screenshotb.png")
                        # allure.attach.file("./screenshotb.png",name='頁面截圖', attachment_type=allure.attachment_type.PNG)
                    #截圖
                    driver.find_element_by_tag_name('body').screenshot('D:\\python_code\\screenshot\\'+image_name)
                    driver.refresh()
                x+=1
            except:
                with allure.step('執行失敗'):
                    print('執行失敗')
                    x+=1
                    with allure.step("截圖"):
                        screen_shot("allure",driver)
                        # driver.save_screenshot("./screenshotb.png")
                        # allure.attach.file("./screenshotb.png",name='頁面截圖', attachment_type=allure.attachment_type.PNG)
                    driver.quit()

                    #驗證須放在最後一行
                    assert 1==2

        driver.quit()

# if __name__ == '__main__':
#     #執行測試腳本並產生allure xml測試結果
#     pytest.main(['-s','-q','test_message_board.py','--alluredir','D:\\Python_Code\\pytest_deom\\allure_result\\0004'])
#     #將XML轉成HTML測試報告格
#     os.system('allure generate D:\\Python_Code\\pytest_deom\\allure_result\\0004 -o D:\\Python_Code\\pytest_deom\\allure_report\\0004 --clean')
if __name__ == '__main__':
    #執行測試腳本並產生allure xml測試結果
    pytest.main(['-s','-q','test_message_board.py','--alluredir','C:\\Users\\pc\\.jenkins\\workspace\\test_message_board\\target\\allure-results'])
    #將XML轉成HTML測試報告格
    #os.system('allure generate D:\\Python_Code\\pytest_deom\\allure_result\\0004 -o D:\\Python_Code\\pytest_deom\\allure_report\\0004 --clean')
