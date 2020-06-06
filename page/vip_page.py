import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class VipPage(BaseAction):

    # 邀请码必填框
    invitecode_edit_text = By.XPATH,"//*[@placeholder='邀请码必填']"

    # 立即成为会员
    to_be_member_button = By.XPATH,"//*[@value='立即成为会员']"

    # 输入邀请码
    @allure.step(title="vip页 输入 邀请码")
    def input_invitecode(self,text):
        self.input(self.invitecode_edit_text, text)

    # 点击立即成为会员
    @allure.step(title="vip页 点击 立即成为会员")
    def click_to_be_member(self):
        self.find_element_with_scroll(self.to_be_member_button).click()


