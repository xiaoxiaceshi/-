import time

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page
import pytest

class TestSearch:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()


    @pytest.mark.parametrize("args",analyze_file("search_data.yaml","test_search"))
    def test_search(self,args):
        keyword = args["keyword"]
        # 登录判断
        self.page.home.login_if_not(self.page)
        # 点击首页
        self.page.home.click_home()
        # 点击放大镜
        self.page.home.click_search()

        # 输入内容
        self.page.search.input_keyword(keyword)
        # 点击搜索
        self.page.search.click_search()
        time.sleep(3)
        # 返回
        self.page.search.press_back()
        time.sleep(3)
        # 断言 搜索的关键字，是不是存在在搜索的页面
        assert self.page.search.is_keyword_exist(keyword)

    def test_del_search(self):
        # 登录判断
        self.page.home.login_if_not(self.page)
        # 点击首页
        self.page.home.click_home()
        # 点击放大镜
        self.page.home.click_search()
        # 输入内容
        self.page.search.input_keyword("男鞋")
        # 点击搜索
        self.page.search.click_search()
        time.sleep(3)
        # 返回
        self.page.search.press_back()

        # 删除搜索记录
        self.page.search.click_del_search()

        # 断言 是否还有搜索历史
        assert  self.page.search.is_search_empty()
