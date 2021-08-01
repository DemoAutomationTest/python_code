# coding=utf-8

import pytest
import allure
import os

@allure.feature('購物車功能')  # 用feature说明产品需求，可以理解为JIRA中的Epic
class TestShoppingTrolley_1(object):
    @allure.story('加入購物車')  # 用story说明用户场景，可以理解为JIRA中的Story
    def test_add_shopping_trolley(self):
        login('張大名', '密碼')  # 步骤1，调用“step函数”
        with allure.step("瀏覽商品"):  # 步骤2，step的参数将会打印到测试报告中
            allure.attach('筆記本', '商品1')  # attach可以打印一些附加信息
            allure.attach('手機', '商品2')
        with allure.step("點擊商品"):  # 步骤3
            pass
        with allure.step("驗證結果"):  # 步骤4
            allure.attach('添加購物車成功', '期望結果')
            allure.attach('添加購物車失敗', '實際結果')
            assert 'success' == 'failed'

    @allure.story('修改購物車')
    def test_edit_shopping_trolley(self):
        pass

    @pytest.mark.skipif(reason='本次不執行')
    @allure.story('刪除購物車中商品')
    def test_delete_shopping_trolley(self):
        pass


@allure.feature('購物車功能')  # 用feature说明产品需求，可以理解为JIRA中的Epic
class TestShoppingTrolley_2(object):
    @allure.story('加入購物車')  # 用story说明用户场景，可以理解为JIRA中的Story
    def test_add_shopping_trolley(self):
        login('張大名', '密碼')  # 步骤1，调用“step函数”
        with allure.step("瀏覽商品"):  # 步骤2，step的参数将会打印到测试报告中
            allure.attach('筆記本', '商品1')  # attach可以打印一些附加信息
            allure.attach('手機', '商品2')
        with allure.step("點擊商品"):  # 步骤3
            pass
        with allure.step("驗證結果"):  # 步骤4
            allure.attach('添加購物車成功', '期望結果')
            allure.attach('添加購物車失敗', '實際結果')
            assert 'success' == 'failed'

    @allure.story('修改購物車')
    def test_edit_shopping_trolley(self):
        pass

    @pytest.mark.skipif(reason='本次不執行')
    @allure.story('刪除購物車中商品')
    def test_delete_shopping_trolley(self):
        pass

@allure.step('用戶登錄')  # 将函数作为一个步骤，调用此函数时，报告中输出这个步骤，我把这样的函数叫“step函数”
def login(user, pwd):
    print(user, pwd)

if __name__ == '__main__':
    #執行測試腳本並產生allure xml測試結果
    pytest.main(['-s','test_allure_shopping_trolley.py','--alluredir','.\\pytest_deom\\allure_result\\0002'])
    #將XML轉成HTML測試報告格
    os.system('allure generate .\\pytest_deom\\allure_result\\0002 -o .\\pytest_deom\\allure_report\\0002 --clean')
