#coding=utf-8
from _pytest.fixtures import reorder_items
import pytest

#單一參數
@pytest.mark.parametrize('a',['a01','a02'],ids=['參數a01','參數a02'])
@pytest.mark.order(1)
def test_001(a):
    print(a)

#多參數
@pytest.mark.parametrize('a,b',
                        [('aa','test01'),('bb','test02'),('cc','test03')],ids=['參數a','參數b','參數c'])
@pytest.mark.order(2)
def test_002(a,b):
    print(a,'__',b)

#使用函數返回值帶入案例中 ,總案例數 2
def return_data():
    return[(1,2),(3,4)]
@pytest.mark.order(3)
@pytest.mark.parametrize('a,b',return_data(),ids=['參數1,2','參數3,4'])
def test_003(a,b):
    print(a,'+',b)

#使用多參數組合 ,總案例 9
@pytest.mark.parametrize('a',[1,2,3])
@pytest.mark.parametrize('b',[4,5,6])
def test_004(a,b):
    print(a,',',b)
    print(a+b)


if __name__ =='__main__':
    pytest.main(["-s","test_parametrize.py"])
