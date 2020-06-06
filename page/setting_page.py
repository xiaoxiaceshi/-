from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class SettingPage(BaseAction):

    # 关于
    about_button = By.XPATH,"//*[@text='关于百年奥莱']"

    # 地址管理
    area_manage_button = By.ID,"com.yunmall.lc:id/setting_address_manage"

    # 点击关于百年奥莱
    @allure.step(title="设置 点击 关于百年奥莱")
    def click_about(self):
        self.find_element_with_scroll(self.about_button).click()

    # 点击地址管理
    @allure.step(title="设置 点击 地址管理")
    def click_area_manage(self):
        self.find_element_with_scroll(self.area_manage_button).click()