import pytest

@pytest.fixture()
def param1():
    return 1


@pytest.fixture()
def param2():
    return 2

@pytest.fixture()
def print1():
    print("\n輸出測試1")
@pytest.fixture()
def print2():
    print("\n輸出測試2")

#傳入參數方式引用
#可以取得返回參數用法
def test_case1(param1):
    print("\n test_data= ",param1)
    assert param1 == 1

def test_case2(param2):
    print("\n test_data= ",param2)
    assert param2 == 2

#函數方式引用
#無法取得返回參數用法
class Test_fixture():
    @pytest.mark.usefixtures("print1")
    def test_case3(self):

        assert 1==1

    @pytest.mark.usefixtures("print2")
    def test_case4(self):

        assert 1==1

@pytest.mark.usefixtures("print1")
def test_case5():
    assert 1==1

@pytest.mark.usefixtures("print2")
def test_case6():
    assert 1==1

#從conftest.py調用
def test_case7(login):
    assert 1==1

#skip and skipif
a=2
@pytest.mark.skip(reason="沒理由")
def test_case08():
    assert 1==1
@pytest.mark.skipif(condition= a == 1 ,reason="沒理由")
def test_case09():
    assert 1==1



if __name__ == "__main__":
    pytest.main(["-s","pytest_fixture.py"])