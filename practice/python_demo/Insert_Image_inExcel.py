from time import sleep
from datetime import datetime
import xlsxwriter
from Module.AUTO_HELP import Brower

driver=Brower('Chrome')
book = xlsxwriter.Workbook('pict2.xlsx')
sheet = book.add_worksheet('demo')
title=1
web_link=('https://ebank.esunbank.com.tw','http://google.com','https:/tw.yahoo.com')
for i in web_link:
    driver.get(i)
    sleep(3)
    CurrentTime=datetime.now().strftime('%Y_%m_%d_%H%M%S')
    image_name=str(CurrentTime) + '.png'
    driver.find_element_by_tag_name('body').screenshot('.\\screenshot\\'+image_name)
    img_file='.\\screenshot\\'+image_name
    sheet.insert_image('A'+str(title),img_file)
    title+=100
book.close()
driver.quit()
