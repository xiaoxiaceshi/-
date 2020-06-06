from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class SearchPage(BaseAction):

    # 输入框
    keyword_edit_text = By.ID,"com.yunmall.lc:id/text_search_keyword"

    # 搜索按钮
    search_button = By.ID,"com.yunmall.lc:id/button_search"

    # 删除搜索记录按钮
    del_search_button = By.ID,"com.yunmall.lc:id/search_del"

    # 输入内容
    @allure.step(title="搜索页 输入 内容")
    def input_keyword(self,text):
        self.input(self.keyword_edit_text,text)

    # 点击搜索
    @allure.step(title="搜索页 点击 搜索")
    def click_search(self):
        self.click(self.search_button)

    # 点击删除搜索记录
    @allure.step(title="搜索页 点击 删除搜索记录")
    def click_del_search(self):
        self.click(self.del_search_button)

    #
    def is_search_empty(self):
        xpath = By.XPATH,"//*[@text='暂无搜索历史']"
        return self.is_feature_exist(xpath)

    # 是否存在该关键词
    @allure.step(title="搜索页 判断 是否存在该关键词")
    def is_keyword_exist(self,text):
        # text_feature = By.XPATH,"//*[@text='%s']"%text
        text_feature = By.XPATH,"//*[@resource-id='com.yunmall.lc:id/keyayout']/*/*[@text='%s']" % text
        return  self.is_feature_exist(text_feature)
