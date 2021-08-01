import sys
import os,shutil
o_path = os.getcwd()
sys.path.append(o_path)
from time import sleep
from datetime import datetime
import xlsxwriter
# from Module.base import webdriver_base
from numpy import NaN
import pandas
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from Module.AUTO_HELP import CSV,clean_temp_file

#清除screenshot資料夾
clean_temp_file('.\\practice\\python_demo\\screenshot_website\\screenshot')
#啟用無頭模式
options_firefox=webdriver.FirefoxOptions()
options_firefox.headless =True
driver=webdriver.Firefox(firefox_options=options_firefox)
file=CSV('.\\practice\\python_demo\\screenshot_website\\screenshot_websit_testdata.csv','link_url','','','','','')
# file=pandas.read_csv('.\\case_demo\\screenshot_websit_testdata.csv')
# url=[]
# for j in  file['link_url']:
#     if j is not NaN:
#         url.append(j)

CurrentTime=datetime.now().strftime('%Y_%m_%d_%H%M%S')
book = xlsxwriter.Workbook('.\\practice\\python_demo\\screenshot_website\\screenshot_website_result_'+CurrentTime+'.xlsx')
sheet1 = book.add_worksheet('list')
sheet2 = book.add_worksheet('screenshot')
title=1
list_nunber=1
for i in file[0]:
    driver.get(i)
    driver.implicitly_wait(5)
    sleep(2)
    CurrentTime=datetime.now().strftime('%Y_%m_%d_%H%M%S')
    image_name=str(CurrentTime) + '.png'
    img_file='.\\practice\\python_demo\\screenshot_website\\screenshot\\'+image_name
    driver.find_element_by_tag_name('body').screenshot(img_file)
    #寫入連結清單
    sheet1.write('A'+str(list_nunber),title)
    sheet1.write('B'+str(list_nunber),i)
    #寫入截圖
    if title ==1:
        sheet2.write('A'+str(title),i)
        sheet2.insert_image('A'+str(title+1),img_file)
    else:
        sheet2.write('A'+str(title-1),i)
        sheet2.insert_image('A'+str(title),img_file)
    title+=300
    list_nunber+=1
book.close()
driver.quit()
