#coding=utf-8
import pytest
import sys
import os
o_path = os.getcwd()
sys.path.append(o_path)

from Module.AUTO_HELP import DB_Link
A='select * from Customer2'
row=DB_Link(A)
print(row[1])

from Module.AUTO_HELP import OTP
code='jjj'
key=OTP(code)
print(key)

from Module.base import webdriver_base
from time import sleep
#僅支援Chrome/Firefox/IE11/Edge
driver=webdriver_base.Brower('Chrome')
driver.get("https://www.google.com.tw")
sleep(3)
driver.quit()


'''
from AUTO_HELP import Brower
from time import sleep

def step1 ():
    driver=Brower('IE11')
    driver.get("https://www.google.com.tw")


def step2 ():
    driver=Brower('Chrome')
    driver.get("https://www.google.com.tw")


def step3 ():
    print('step3')
'''