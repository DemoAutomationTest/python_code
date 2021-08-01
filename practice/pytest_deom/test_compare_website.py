import os,sys,pytest,allure
o_path = os.getcwd()
sys.path.append(o_path)
from time import sleep
from datetime import datetime
from Module.AUTO_HELP import Brower,CSV
from numpy import NaN
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from Module.compare_Imag import runAllImageSimilaryFun
test_data=CSV('.\\case_demo\\screenshot_websit_testdata.csv','link_url','old_img_name','','','','')
x=0
old_img_name=test_data[1]

@allure.title('網站版面掃描')
@pytest.mark.parametrize('url',(test_data[0]))
def test_compare_website_UI(url):
    global x,old_img_name

    #啟用無頭模式
    options_firefox=webdriver.FirefoxOptions()
    options_firefox.headless =True
    driver=webdriver.Firefox(firefox_options=options_firefox)
    CurrentTime=datetime.now().strftime('%Y_%m_%d_%H%M%S')
    image_name=str(CurrentTime) +'_'+ old_img_name[x]
    old_img_file=".\\case_demo\\screenshot\\"+old_img_name[x]
    new_img_file=".\\case_demo\\screenshot\\"+image_name

    driver.get(url)
    driver.implicitly_wait(5)
    sleep(3)

    '''
    判斷首次增加圖檔是否存在
        存在-則進行前次圖檔差異比較
        不存在-則建立網站首次截圖
    '''
    if os.path.isfile(old_img_file):
        driver.find_element_by_tag_name('body').screenshot('.\\case_demo\\screenshot\\'+image_name)
        print(old_img_name[x],"檔案存在。")
        #比較圖檔相似度
        compare_image=runAllImageSimilaryFun(old_img_file,new_img_file)
        if (compare_image[0]+compare_image[1])/2 < 0.9 :
            print('站台有跑版風險',compare_image)
            with allure.step("比對結果"):
                allure.attach.file(old_img_file,name='原始截圖', attachment_type=allure.attachment_type.PNG)
                allure.attach.file(new_img_file,name='本次截圖', attachment_type=allure.attachment_type.PNG)
            x+=1
            driver.quit()
            assert 0==1
        else:
            print('站台無跑版風險',compare_image)
            os.remove(old_img_file)
            driver.find_element_by_tag_name('body').screenshot('.\\case_demo\\screenshot\\'+old_img_name[x])
    else:
        print(old_img_name[x],"檔案不存在。")
        driver.find_element_by_tag_name('body').screenshot('.\\case_demo\\screenshot\\'+old_img_name[x])
    x+=1
    driver.quit()

if __name__ == "__main__":
    # Jenkins設定
    # pytest.main(['-s','-q','test_compare_website.py','--alluredir','C:\\Users\\pc\\.jenkins\\workspace\\test_compare_website\\target\\allure-results'])
    pytest.main(['-s','test_compare_website.py','--alluredir','.\\pytest_deom\\allure_result\\0007'])
    #將XML轉成HTML測試報告格
    os.system('allure generate .\\pytest_deom\\allure_result\\0007 -o .\\pytest_deom\\allure_report\\0007  --clean')

