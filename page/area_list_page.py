import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class AreaListPage(BaseAction):

    # 新增地址按钮
    add_area_button = By.ID,"com.yunmall.lc:id/address_add_new_btn"

    # 默认收件人和电话
    default_name_feature = By.ID,"com.yunmall.lc:id/receipt_name"

    # 默认标记
    is_default_feature = By.ID,"com.yunmall.lc:id/address_is_default"

    # 编辑按钮
    edit_button = By.ID,"com.yunmall.lc:id/ymtitlebar_right_btn"

    # 删除按钮
    del_button = By.ID,"com.yunmall.lc:id/delete"

    # 确认删除
    confirm_del_button = By.ID,"com.yunmall.lc:id/ymdialog_left_button"

    # 点击新增地址
    @allure.step(title="地址列表 点击 新增地址")
    def click_add_area(self):
        self.find_element_with_scroll(self.add_area_button).click()

    # 获取默认收件人和电话内容
    @allure.step(title="地址列表 获取 默认收件人和电话")
    def get_default_name_text(self):
        return  self.get_text(self.default_name_feature)

    # 默认标记是否存在
    @allure.step(title="地址列表 判断 默认标记是否存在")
    def is_default_feature_exist(self):
        return self.is_feature_exist(self.is_default_feature)

    # 进入默认地址
    @allure.step(title="地址列表 点击 默认地址")
    def click_default_area(self):
        self.click(self.is_default_feature)

    # 点击编辑
    @allure.step(title="地址列表 点击 编辑")
    def click_edit(self):
        self.find_element_with_scroll(self.edit_button).click()

    # 点击删除
    @allure.step(title="地址列表 点击 删除")
    def click_del(self):
        self.find_element_with_scroll(self.del_button).click()

    # 删除是否存在
    @allure.step(title="地址列表 判断 删除是否存在")
    def is_del_exist(self):
        return self.is_feature_exist(self.del_button)

    # 确认删除
    @allure.step(title="地址列表 点击 确认删除")
    def click_confirm_del(self):
        self.find_element_with_scroll(self.confirm_del_button).click()
