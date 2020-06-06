from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class MePage(BaseAction):

    # 登录昵称
    login_nickname_text = By.ID,"com.yunmall.lc:id/tv_user_nikename"

    # 设置按钮
    setting_button = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"

    # 加入超级VIP
    vip_button = By.ID,"com.yunmall.lc:id/tv_my_shop_text"

    # 获取登录昵称
    @allure.step(title="我 获取 昵称")
    def get_login_nickname_text(self):
        return self.find_element(self.login_nickname_text).text

    # 点击设置按钮
    @allure.step(title="我 点击 设置")
    def click_setting(self):
        self.find_element_with_scroll(self.setting_button).click()

    # 点击加入超级VIP
    @allure.step(title="我 点击 加入超级VIP")
    def click_vip(self):
        self.find_element_with_scroll(self.vip_button).click()
