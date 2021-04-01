import sys,os
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.page_search import PageSearch
from time import sleep
import pytest

class TestSearch:
    def setup(self):
        self.driver=init_driver();
        self.page_search=PageSearch(self.driver);

    def teardown(self):
        sleep(2)
        self.driver.quit();

    @pytest.mark.parametrize("kw", ["张三","李四"])
    def test_search_01(self,kw):
        #定位到元素“放大镜”，并点击
        self.page_search.click_fdj();
        #定位到元素“输入框”，并输入数据：张三
        self.page_search.input_kw(kw);