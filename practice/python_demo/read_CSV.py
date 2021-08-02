'''
讀取CSV檔(使用pandas)
'''
import csv
import os
os.chdir('../../')
print(os.getcwd())
file=open('.\\practice\\python_demo\\screenshot_website\\screenshot_websit_testdata.csv','r')
testdata =csv.DictReader(file)
testdata2 =csv.reader(file)

for i in testdata2:
    print(i[0])

# for i in testdata:
#     driver=Brower('Chrome')
#     driver.get('https://ebank.esunbank.com.tw')
#     driver.implicitly_wait(3)
#     sleep(3)
#     # driver.find_element_by_id("login-username").send_keys(i['ID'])
#     # sleep(3)
#     # driver.find_element_by_id('loginform:name').sendkeys(i['ACCOUNT'])
#     #sleep(3)
#     driver.find_element_by_id('loginform:pxsswd').sendkeys(i['PASSWORD'])
#     sleep(3)
#     driver.quit()
# print('執行結束')