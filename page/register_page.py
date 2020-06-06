from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class RegisterPage(BaseAction):

    # 已有帐号，去登录
    go_login_button = By.XPATH,"//*[@text='已有账号，去登录']"

    # 点击去登录
    @allure.step(title="注册 点击 去登录")
    def click_go_login(self):
        self.click(self.go_login_button)