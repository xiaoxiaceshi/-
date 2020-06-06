import random
import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class EditAreaPage(BaseAction):

    # 收件人
    name_edit_text = By.ID,"com.yunmall.lc:id/address_receipt_name"
    # 手机号
    phone_edit_text = By.ID,"com.yunmall.lc:id/address_add_phone"
    # 所在地区
    area_button = By.ID,"com.yunmall.lc:id/address_province"
    # 省市区特征
    area_feature = By.ID,"com.yunmall.lc:id/area_title"
    # 详细地址
    area_detail_edit_text = By.ID,"com.yunmall.lc:id/address_detail_addr_info"
    # 邮编
    post_code_edit_text = By.ID,"com.yunmall.lc:id/address_post_code"
    # 默认地址
    default_area_button = By.ID,"com.yunmall.lc:id/address_default"
    # 保存
    save_area_button = By.ID,"com.yunmall.lc:id/button_send"


    # 输入收件人
    @allure.step(title="地址页 输入 收件人")
    def input_name(self,text):
        self.input(self.name_edit_text,text)

    # 输入手机号
    @allure.step(title="地址页 输入 手机号")
    def input_phone(self,text):
        self.input(self.phone_edit_text,text)

    # 选择所在地区
    @allure.step(title="地址页 点击 所在地区")
    def click_area(self):
        self.find_element_with_scroll(self.area_button).click()

    # 输入详细地址
    @allure.step(title="地址页 输入 详细地址")
    def input_area_detail(self,text):
        self.input(self.area_detail_edit_text,text)

    # 输入邮编
    @allure.step(title="地址页 输入 邮编")
    def input_post_code(self,text):
        self.input(self.post_code_edit_text,text)

    # 设置默认地址
    @allure.step(title="地址页 设置 默认地址")
    def click_default_area(self):
        self.find_element_with_scroll(self.default_area_button).click()

    # 点击保存
    @allure.step(title="地址页 点击 保存")
    def click_save_area(self):
        self.find_element_with_scroll(self.save_area_button).click()

    # 进入所在地区，并且选择一个随机的区域
    @allure.step(title="地址页 选择 地区")
    def select_area(self):
        self.click_area()
        time.sleep(1)
        while True:
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            areas = self.find_elements(self.area_feature)
            area_index = random.randint(0,len(areas)-1)
            areas[area_index].click()
            time.sleep(1)