#案例：PO模式、参数化：从yaml文件中读取测试数据
import os, sys
import pytest
import time

from selenium.webdriver.common.by import By
sys.path.append(os.getcwd())
from base.base_yaml import yml_data_with_filename_and_key
from base.base_driver import init_driver
from page.page_concat import PageConcat
from appium import webdriver
import allure

#辅助函数：用于再处理测试数据
def data_with_key(key):
    return yml_data_with_filename_and_key("data_concat", key)

class TestConcat:
    # def setup(self):
    #     self.driver = init_driver()
    #     self.page_concat = PageConcat(self.driver)
    #
    # def teardown(self):
    #     time.sleep(2)
    #     self.driver.quit()

    def setup_class(self):
        self.driver = init_driver()
        self.page_concat = PageConcat(self.driver)


    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()

    @allure.severity("blocker")
    @allure.step(title="添加联系人")
    @pytest.mark.parametrize("data", data_with_key("test_concat01"))
    def test_concat01(self,data):
        allure.attach("","步骤1：接收测试数据")
        name=data["name"]
        nicen=data["nicen"]
        beizu=data["beizu"]
        website=data["website"]

        allure.attach("", "步骤2：定位元素“添加联系人”按钮，并点击")
        #定位元素“添加联系人”按钮，并点击
        self.page_concat.click_addConcat();
        allure.attach("", "步骤3：定位元素“本地保存”按钮，并点击")
        #定位元素“本地保存”按钮，并点击
        self.page_concat.click_bendibaocun();
        allure.attach("", "步骤4：定位元素“姓名”，并输入："+name)
        #定位元素“姓名”，并输入："张三"
        self.page_concat.input_name(name);
        allure.attach("", "步骤5：定位元素“昵称”，并输入:"+nicen)
        #定位元素“昵称”，并输入:"小白兔"
        self.page_concat.input_nicen(nicen);
        #定位元素“备注”，并输入："是个帅哥"
        self.page_concat.input_beizu(beizu);
        #定位元素“网站”,并输入:"http://52studyit.net"
        self.page_concat.input_website(website);
        #定位元素“返回箭头”，并点击
        self.page_concat.click_fanhui();
        #返回键
        self.driver.keyevent(4)
        time.sleep(2)

    @allure.severity("minor")
    def test_concat02(self):
        print("111")