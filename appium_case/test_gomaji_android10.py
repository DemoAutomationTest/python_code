from time import sleep
from datetime import datetime
import pytest,os
#跨目錄引用Module
import sys,os
sys.path.append(os.getcwd())
# from Module.AUTO_HELP import Mobile_appium_startup
from Module.base import webdriver_base

sys_path=os.getcwd()
print(sys_path)
@pytest.mark.parametrize("set_city",["city_taipei","city_taoyuan","city_hsinchu","city_taichung","city_tainan","city_kaohsiung"])
def test_start_setup(set_city):


    CurrentTime=datetime.now().strftime('%Y_%m_%d_%H%M%S')
    image_name1=set_city+"_"+str(CurrentTime) + '.png'
    image_name2=".\\appium_case\\screenshot\\android10"+set_city+"_get_"+str(CurrentTime) + '.png'
    find_city_elemint="com.wantoto.gomaji2:id/"+set_city

    #安裝APP
    # os.system("adb -s emulator-5554 install C:\\Users\\pc\\AppData\\Local\\Android\\android-sdk\\platform-tools\\test_apk\\com.wantoto.gomaji2_2021-06-10.apk")
    #啟動APPium行動裝置Remote(服務器,配置參數)
    driver=webdriver_base.Mobile_appium_startup(".\\appium_case\\config\\appium10_cfg.yaml")
    # driver=help.Mobile_appium_startup(".\\appium_android\\config\\appium10_cfg.yaml")

    # driver.start_activity("com.android.settings","com.android.settings.SubSettings")
    driver.start_activity("com.wantoto.gomaji2","com.gomaji.MainActivity")
    #開始腳本操作
    driver.implicitly_wait(3)
    sleep(2)
    webdriver_base.wait_element_by_xpath(driver,"//*[contains(@text,'賺取點數')]").click()
    # driver.find_element_by_id("android:id/button2").click()
    sleep(3)
    driver.keyevent(4)
    driver.keyevent(4)
    webdriver_base.wait_element_by_xpath(driver,"//*[contains(@text,'按摩')]").click()

    #driver.save_screenshot(image_name1)
    # print(driver.page_source)
    driver.get_screenshot_as_file(image_name2)
    driver.quit()
    #移除APP
    # os.system("adb -s emulator-5554 shell pm uninstall -k com.wantoto.gomaji2")

if __name__ == "__main__":
    pytest.main(["-s",".\\appium_case\\test_gomaji_android10.py"])
