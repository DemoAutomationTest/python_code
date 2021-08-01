"""
URL/API HTTP請求監測
可監控回傳時間、結果、特定回傳值
"""
import requests

r=requests.get('https://shopee.tw/')
print (r.url)
print(r.cookies)
#print(r.text)
print(r.json)
print(r.status_code)
print(r.headers)