'''
切換不同瀏覽器
'''
from selenium import webdriver
from time import sleep
import sys,os
sys.path.append(os.getcwd())
Chrome=webdriver.Chrome()#('D:\Python Code\webdriver\chromedriver.exe')
# Firefox=webdriver.Firefox() #'D:\Python Code\webdriver\geckodriver.exe'
# Edge=webdriver.Edge()#('D:\Python Code\webdriver\msedgedriver.exe')
# IE11=webdriver.Ie() #('D:\Python Code\webdriver\IEDriverServer3.exe')
sys_path=os.getcwd()
print(sys_path)
Driver=Chrome
Driver.get('https://WWW.ESUNBANK.COM.TW')
sleep(2)
Driver.quit()
