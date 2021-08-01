"""
MSSSQL 資料庫連線
"""
#coding=utf-8
import pymssql

conn=pymssql.connect(
    server='127.0.0.1'
    ,port='1433'
    ,user='Admin'
    ,password='admin1982'
    ,database='Master'
    ,charset='utf8')

cursor = conn.cursor()
sql1="select * from esun_account"
sql ='select id  from Customer2'.encode('utf8')
#執行SQL
cursor.execute(sql1)
# 獲取第一行資料
row_1 = cursor.fetchone()
#print(row_1[0])
# 獲取前n行資料(第一筆不會顯示)
row_2 = cursor.fetchmany(3)
#print(row_2)
# 獲取所有資料
row_3 = cursor.fetchall()
print(row_3)
conn.close()