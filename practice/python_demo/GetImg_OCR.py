'''
圖形辨識，圖形驗證碼應用
1.透過requests以圖檔URL儲存檔案後辨識
2.透過webdriver 元件截圖後辨識
'''
from Module.AUTO_HELP import Brower
from Module.AUTO_HELP import OCR
from Module.AUTO_HELP import save_img

driver=Brower('Chrome')
driver.get('https://www.google.com')

url=driver.find_element_by_class_name('lnXdpd').get_attribute('src')
save_img(url)
print('下載法--'+OCR('.\ocr_code.jpg'))

img=driver.find_element_by_link_text('Gmail')
img.screenshot('.\ocr_code.png')
print('截圖法--'+OCR('.\ocr_code.png'))
driver.quit()
