'''
圖形辨識
'''
import pytesseract
from PIL import Image

def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    code_list=['code1.png','code2.png','code3.png','code4.png','code5.png','code6.png','code7.png','code8.png','code9.png']
    for i in code_list:
        path=".\\practice\\python_demo\\OCT\\verify_code\\" + i
        img = Image.open(path)
        img_opt =img.convert('L') # 處理灰度
        table = [0 if i < 140 else 1 for i in range(256)] #調整閥值
        out = img_opt.point(table,'1')
        # out.show()
        # img_opt.show()
        print(i +'-----'+ pytesseract.image_to_string(img, lang='eng'))


if __name__ == "__main__":
    main()