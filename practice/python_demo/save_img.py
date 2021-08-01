'''
透過URL儲存圖檔
'''
import requests
from Module.AUTO_HELP import OCR
img_url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
file_name='ocr_code.jpg'

res=requests.get(img_url)
with open(file_name,'wb') as f:
    f.write(res.content)

OCR('.\ocr_code.jpg')