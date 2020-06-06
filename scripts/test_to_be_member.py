import time

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page

class TestToBeMember:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("vip_data.yaml","test_to_be_member"))
    def test_to_be_member(self,args):
        keyword = args['keyword']
        expect = args['expect']

        self.page.home.login_if_not(self.page)
        self.page.me.click_vip()
        time.sleep(5)
        # 切换到webview
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        self.page.vip.input_invitecode(keyword)
        self.page.vip.click_to_be_member()
        assert self.page.vip.is_keyword_in_page_source(expect),"%s不在page_source中"%expect
        # 切换到到原生
        self.driver.switch_to.context("NATIVE_APP")

