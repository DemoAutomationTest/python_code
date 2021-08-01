#coding=utf-8
import pytest
import time
import os
import allure

current_time=time.strftime("%Y%m%d_%I%M%S",time.localtime())
print(current_time)
if __name__ =='__main__':
    #定義Pytest設定檔
    setting_file=open('.\pytest.ini','w')
    setting_file.write('[pytest]\n'
    #+"disable_test_id_escaping_and_forfeit_all_rights_to_community_support = True \n"
    #↑↑解決pytest.parametrize ids中文顯示問題
    + "addopts = --tb short -s --reruns 2 -n auto -p no:warnings --durations=3 -vv --html='D:\\Python_Code\\pytest_deom\\test_report\\"+current_time+"_report.html' --alluredir 'D:\\Python_Code\\pytest_deom\\allure_result\\"+current_time+"' \n"
    + "testpaths = \n"
    + "markers = \n"
    +"g1: group1\n"
    +"g2: group2\n"
    +"g3: counting test\n"
    +"g5: group5")
    setting_file.close()

    os_command='allure generate .\\pytest_deom\\allure_result\\'+current_time+' -o .\\pytest_deom\\allure_report\\'+current_time+ ' --clean'

    '''
    執行三步驟
    1.執行測案並產生allure xml
    2.建立測試環境定義檔environment.properties
    3.產生allure Html測報
    '''
    pytest.main()
    #在Allure report 顯示測試環境定義檔(中文顯示會有問題)
    setting_file=open('.\\pytest_deom\\allure_result\\'+current_time+'\\environment.properties','w')
    setting_file.write(
    "systemVersion=win10 \n"+
    "pythonVersion=3.7.0 \n"+
    "allureVersion=2.13.15 \n"+
    "baseUrl=https://www.test.com.tw/ \n"+
    "projectName=test_project \n"+
    "author=Kim \n" )
    setting_file.close()

    os.system(os_command)
