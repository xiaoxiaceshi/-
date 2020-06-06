from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    # 用户名
    username_edit_text = By.ID,"com.yunmall.lc:id/logon_account_textview"
    # 密码
    pwd_edit_text= By.ID,"com.yunmall.lc:id/logon_password_textview"
    # 登录
    login_button = By.ID,"com.yunmall.lc:id/logon_button"

    # 输入用户名
    def input_username(self,text):
        self.input(self.username_edit_text,text)

    # 输入密码
    def input_pwd(self,text):
        self.input(self.pwd_edit_text,text)

    # 点击登录
    def click_login(self):
        self.click(self.login_button)