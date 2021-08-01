"""
取得資料庫特定欄位字串中的資料
"""
from Module.AUTO_HELP import DB_Link
key='NJZ'
A="select * from message where message like"+" '%" + key +"%'"
print(A)
result=DB_Link(A)
print(result)
str1=str(result[1])

str3=str1.find(key)
print(str1[str3+4:10])
