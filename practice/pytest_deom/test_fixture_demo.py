import pytest

@pytest.fixture()
def add ():
    return 'x'

def test_add(add):
    y=add+'a'
    assert y=='xa'
    print('測試'+y)

if __name__ == '__main__':
    pytest.main(['-s','test_fixture_demo.py'])