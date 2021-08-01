from appium import webdriver
from time import sleep
from datetime import datetime
from appium.webdriver import appium_connection
from selenium.webdriver.common.keys import Keys
import pytest
#跨目錄引用Module
import sys,os
from _pytest.config import main
o_path = os.getcwd()
sys.path.append(o_path)
from Module.AUTO_HELP import Mobile_appium_startup

@pytest.mark.parametrize("set_city",["city_taipei"])
def test_start_setup(set_city):
    '''
    將Appium 啟動參數放在appium_cfg.yaml中
    '''
    driver=Mobile_appium_startup(".\\appium_android\\config\\appium10_cfg.yaml")
    CurrentTime=datetime.now().strftime('%Y_%m_%d_%H%M%S')
    image_name=".\\appium_android\\screenshot\\android11_"+set_city+"_"+str(CurrentTime) + '.png'

    #開啟APP
    driver.start_activity("com.android.chrome","com.google.android.apps.chrome.Main")

    #啟動APPium行動裝置Remote(服務器,配置參數)
    #開始腳本操作
    driver.implicitly_wait(3)
    sleep(3)
    #driver.save_screenshot(image_name1)
    driver.get_screenshot_as_file(image_name)
    driver.quit()
    #移除APP


if __name__ == "__main__":
    pytest.main(["-s",".\\appium_android\\test_gomaji_android11.py"])
