"""
自定義函數
"""
from numpy import NaN
from PIL import Image
from time import sleep
import requests
import pymssql
import pytesseract
import pandas
import os,shutil

#取得資料庫特定資料
def DB_Link(SQL):
    '''
    以sql指令查詢資料表，以單欄位/單筆資料為主

    輸入
        sql  EX : select name from customer where id='a123456789'
    輸出
        顯示查詢結果
    '''

    conn=pymssql.connect(
    server='127.0.0.1'
    ,port='1433'
    ,user='Admin'
    ,password='admin1982'
    ,database='Master'
    ,charset='utf8')
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_1 = cursor.fetchone()
    return row_1
    #new one

 #取得資料庫中簡訊密碼值,簡訊未產生時間隔5秒查詢10次
def OTP(verify_code):
    '''
    查詢簡訊密碼

    輸入
        輸入密碼關鍵字，ex:ATX-568695， 輸入ATX
    輸出
        簡訊密碼
    '''

    verify_code=verify_code.upper()
    A="select * from message where message like"+" '%" + verify_code +"%'"
    result=DB_Link(A)
    for i in range(0,10,1):
        if result is None:
            sleep(5)
            result=DB_Link(A)
        else:
            str1=str(result[1])
            str2=str1.find(verify_code)
            OTP_Code=str1[str2+4:str2+10]
            return OTP_Code


#儲存網頁圖檔
def save_img(url):
    '''
    儲存網頁圖檔
    '''
    file_name='ocr_code.jpg'
    res=requests.get(url)
    with open(file_name,'wb') as f:
        f.write(res.content)

#OCR辨識
def OCR(file_path):
    '''
    圖像辨識，用於圖形驗證碼

    輸入
        辨識圖檔路徑
    輸出
        字串型態辨識結果
    '''

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open(file_path)
    return pytesseract.image_to_string(img,lang='eng')

#取得csv變數
def CSV(file_path:str,column1:str,column2:str,column3:str,column4:str,column5:str,column6:str):
    '''
    取得CSV檔案內容

    輸入
        檔案路徑、欄位名1、欄位名2、欄位名3、欄位名4、欄位名5、欄位名6
        若欄位為空值則輸入''
    輸出
        以列表型態顯示結果
    '''

    file=pandas.read_csv(file_path)
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    if column1 != '':
        for i in  file[column1]:
            if i is not NaN:
                A.append(i)
    if column2 != '':
        for j in  file[column2]:
            if j is not NaN:
                B.append(j)
    if column3 != '':
        for k in  file[column3]:
            if k is not NaN:
                C.append(k)
    if column4 != '':
        for l in  file[column4]:
            if l is not NaN:
                D.append(l)
    if column5 != '':
        for m in  file[column5]:
            if m is not NaN:
                E.append(m)
    if column6 != '':
        for n in  file[column6]:
            if n is not NaN:
                F.append(n)

    return(A,B,C,D,E,F)

#清除並重建暫存檔
def clean_temp_file(file_path):
    '''
    輸入暫存資料夾的路徑
    如不存在建立資料夾
    若存在則先刪除資料夾在建立
    '''
    if os.path.isdir(file_path):
        shutil.rmtree(file_path)
        os.mkdir(file_path)
    else:
        os.mkdir(file_path)

