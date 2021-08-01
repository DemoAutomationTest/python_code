import pytest
def add(num1,num2):
    return num1 + num2

def test_add1():
    assert add(3,4) == 7

def test_add2():
    assert add(3,5) == 8

# if __name__ =='__main__':
#     pytest.main()