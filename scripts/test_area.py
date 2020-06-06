import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestArea:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("area_data.yaml","test_add_area"))
    def test_add_area(self,args):
        name = args["name"]
        phone = args["phone"]
        area_detail = args["area_detail"]
        post_code = args["post_code"]
        toast = args["toast"]

        self.page.home.login_if_not(self.page)
        self.page.me.click_setting()
        self.page.setting.click_area_manage()
        self.page.area_list.click_add_area()
        self.page.edit_area.input_name(name)
        self.page.edit_area.input_phone(phone)
        self.page.edit_area.input_area_detail(area_detail)
        self.page.edit_area.input_post_code(post_code)
        self.page.edit_area.click_default_area()
        self.page.edit_area.select_area()
        time.sleep(2)
        self.page.edit_area.click_save_area()
        if toast is None:
            assert self.page.area_list.get_default_name_text() == "%s  %s" % (name,phone),"保存成功，默认的姓名和电话与输入的不符"
        else:
            assert self.page.edit_area.is_toast_exist(toast),"保存不成功，toast内容和预期不符"


    def test_edit_area(self):
        self.page.home.login_if_not(self.page)
        self.page.me.click_setting()
        self.page.setting.click_area_manage()
        if not self.page.area_list.is_default_feature_exist():
            self.page.area_list.click_add_area()
            self.page.edit_area.input_name("简自豪")
            self.page.edit_area.input_phone("18311111111")
            self.page.edit_area.input_area_detail("RNG基地208")
            self.page.edit_area.input_post_code("666666")
            self.page.edit_area.click_default_area()
            self.page.edit_area.select_area()
            time.sleep(2)
            self.page.edit_area.click_save_area()
        # 进入默认地址
        self.page.area_list.click_default_area()
        self.page.edit_area.input_name("UZI")
        self.page.edit_area.input_phone("18311111112")
        self.page.edit_area.input_area_detail("RNG基地308")
        self.page.edit_area.input_post_code("888888")
        self.page.edit_area.select_area()
        time.sleep(2)
        self.page.edit_area.click_save_area()
        # 断言 是否出现“保存成功”的toast信息
        assert self.page.area_list.is_toast_exist("保存成功")

    def test_del_area(self):
        self.page.home.login_if_not(self.page)
        self.page.me.click_setting()
        self.page.setting.click_area_manage()

        if not self.page.area_list.is_default_feature_exist():
            self.page.area_list.click_add_area()
            self.page.edit_area.input_name("简自豪")
            self.page.edit_area.input_phone("18311111111")
            self.page.edit_area.input_area_detail("RNG基地208")
            self.page.edit_area.input_post_code("666666")
            self.page.edit_area.click_default_area()
            self.page.edit_area.select_area()
            time.sleep(2)
            self.page.edit_area.click_save_area()

        for i in range(10):
            # 点击编辑
            self.page.area_list.click_edit()
            if self.page.area_list.is_del_exist():
                #点击删除
                self.page.area_list.click_del()
                # 确认删除
                self.page.area_list.click_confirm_del()
            else:
                break

        # 点击编辑
        self.page.area_list.click_edit()
        assert not self.page.area_list.is_del_exist(),"收货地址没有删除完毕"






