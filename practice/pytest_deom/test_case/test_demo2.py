#coding=utf-8
import sys
import os
from _pytest.config import main
o_path = os.getcwd()
sys.path.append(o_path)
import pytest
from time import sleep
from Module.AUTO_HELP import Brower

def setup_function(function):
    driver=Brower('Chrome')
    print("開啟瀏覽器")


def teardown_function(function):
    driver=Brower('Chrome')
    driver.quit()
    print("關閉瀏覽器")
@pytest.mark.order(3)
def test_case1():
    sleep(3)
    assert 1==1
    print("測案1")
@pytest.mark.order(2)
def test_case2():
    assert 2==2
    print("測案2")
@pytest.mark.order(1)
def test_case3():
    assert 2==2
    print("測案3")



if __name__ =='__main__':
    pytest.main()
