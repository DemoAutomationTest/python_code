"coding=utf-8"

from appium import webdriver
from time import sleep
from datetime import datetime
from appium.webdriver import appium_connection
from appium.webdriver.extensions.android.network import Network
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import pytest
#跨目錄引用Module
import sys,os
from _pytest.config import main
o_path = os.getcwd()
sys.path.append(o_path)
from Module.AUTO_HELP import mobile_appium_yamlcfg,wait_element_by_xpath
from appium.webdriver.common.touch_action import TouchAction

os.system("adb -s emulator-5554 install C:\\Users\\pc\\AppData\\Local\\Android\\android-sdk\\platform-tools\\test_apk\\com.wantoto.gomaji2_2021-06-10.apk")
start=mobile_appium_yamlcfg(".\\appium_android\\config\\appium10_cfg.yaml")
driver=webdriver.Remote(start[1],start[0])
driver.close_app()
sleep(2)

# driver.start_activity("com.android.settings","com.android.settings.homepage.SettingsHomepageActivity")
# sleep(2)
# ele_list = driver.find_elements_by_id("android:id/title")
# for i in ele_list:
#     print(i.text)
#     if i.text=="網路和網際網路":
#         i.click()
#         sleep(3)
#         driver.find_element_by_class_name("android.widget.ImageButton").click()
#         break

# driver.start_activity("com.android.settings","com.android.settings.homepage.SettingsHomepageActivity")
# driver.implicitly_wait(10)
# ele_list2 = driver.find_elements_by_id("android:id/summary")

# for j in ele_list2:
#     print(j.text)
#     if j.text =="100%":
#         j.click()
#         sleep(3)
#         driver.find_element_by_class_name("android.widget.ImageButton").click()
#         break
# driver.close_app()

# driver.start_activity("com.android.settings","com.android.settings.homepage.SettingsHomepageActivity")
# driver.implicitly_wait(10)
# driver.find_element_by_id("com.android.settings:id/search_action_bar_title").click()
# for i in ("電","音","定123"):
#     driver.find_element_by_id("android:id/search_src_text").clear()
#     driver.find_element_by_id("android:id/search_src_text").send_keys(i)
#     driver.keyevent(66)
#     result_list=driver.find_elements_by_id("android:id/title")
#     for x in result_list:
#         print(x.text)
# driver.close_app()

# driver.start_activity("com.android.settings","com.android.settings.homepage.SettingsHomepageActivity")
# driver.implicitly_wait(10)
# sleep(3)
# driver. (530,1930,530,430)
# driver.close_app()

# driver.start_activity("com.android.settings","com.android.settings.homepage.SettingsHomepageActivity")
# driver.implicitly_wait(10)
# sleep(3)
# start_ele=driver.find_element_by_xpath("//*[contains(@text,'音效')]")
# end_ele=driver.find_element_by_xpath("//*[contains(@text,'網路和網際網路')]")
# driver.scroll(start_ele,end_ele)
# sleep(2)
# driver.close_app()

# sleep(2)
# ele=driver.find_element_by_accessibility_id("GOMAJI")
# TouchAction(driver).long_press(ele).perform()
# # TouchAction(driver).long_press(ele).perform()
# driver.find_element_by_id("com.google.android.apps.nexuslauncher:id/bubble_text").click()
# sleep(1)
# driver.find_element_by_id("com.android.settings:id/button2").click()
# sleep(1)
# driver.press_keycode(3)



# print(driver.network_connection)
# driver.set_network_connection(4)
# #設定到飛航模式會有權限問題()
# driver.open_notifications()
# driver.keyevent(3)


# sleep(2)
# w_h=driver.get_window_size()
# w=w_h["width"]
# h=w_h["height"]
# print(w,h)
# driver.swipe(w*0.2,h*0.5,w*0.8,h*0.5,2000)
# driver.keyevent(3)



driver.start_activity("com.android.settings","com.android.settings.homepage.SettingsHomepageActivity")
ele=wait_element_by_xpath(driver,"//*[contains(@text,'音效')]")
driver.find_element_by_class_name
print (ele.text)