import os, sys
sys.path.append(os.getcwd())
from base.page_base import PageBase #导入页面基类
from selenium.webdriver.common.by import By

class PageConcat(PageBase):
    #这些是抽取元素特征
    loc_addConcat=By.ID,"com.android.contacts:id/floating_action_button"
    loc_bendibaocun=By.XPATH,"text,本地保存,1"
    loc_name=By.XPATH,"text,姓名,1"
    loc_nicen=By.XPATH,"text,昵称,1"
    loc_beizu=By.XPATH,"text,备注,1"
    loc_website=By.XPATH,"text,网站,1"
    loc_fanhui=By.CLASS_NAME,"android.widget.ImageButton"


    def __init__(self, driver):
        PageBase.__init__(self, driver)



    # 定位元素“添加联系人”按钮，并点击
    def click_addConcat(self):
        self.click(PageConcat.loc_addConcat);

    # 定位元素“本地保存”按钮，并点击
    def click_bendibaocun(self):
        self.click(PageConcat.loc_bendibaocun)

    # 定位元素“姓名”，并输入："张三"
    def input_name(self,name):
        self.input_text(PageConcat.loc_name,name)

    # 定位元素“昵称”，并输入:"小白兔"
    def input_nicen(self,nicen):
        self.input_text(PageConcat.loc_nicen,nicen)

    # 定位元素“备注”，并输入："是个帅哥"
    def input_beizu(self,beizu):
        self.input_text_scroll(loc=PageConcat.loc_beizu,data=beizu)

    # 定位元素“网站”,并输入:"http://52studyit.net"
    def input_website(self,website):
        self.input_text_scroll(loc=PageConcat.loc_website,data=website)

    def click_fanhui(self):
        self.click(PageConcat.loc_fanhui);
