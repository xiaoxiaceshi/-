import time
import pytest
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page

class TestLogin:

    def setup(self):
        self.driver = init_driver(noReset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("login_data.yaml","test_login"))
    def test_login(self,args):
        # 解析yaml数据
        username = args["username"]
        pwd = args["pwd"]
        toast = args["toast"]

        # 脚本流程
        self.page.home.click_me()
        self.page.register.click_go_login()
        self.page.login.input_username(username)
        self.page.login.input_pwd(pwd)
        self.page.login.click_login()

        if toast is None:
            assert self.page.me.get_login_nickname_text()=="xiaoxiatest","输入用户名与当前显示用户名不一致"
        else:
            assert self.page.login.is_toast_exist(toast)

