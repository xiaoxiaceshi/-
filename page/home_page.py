from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class HomePage(BaseAction):

    # 我
    me_button = By.ID,"com.yunmall.lc:id/tab_me"

    # 分类
    category_button = By.ID,"com.yunmall.lc:id/tab_category"

    # 购物车
    shopcart_button = By.ID,"com.yunmall.lc:id/tab_shopping_cart"

    # 首页
    home_button = By.ID,"com.yunmall.lc:id/tab_home"

    # 放大镜
    search_button = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"

    # 点击我
    @allure.step(title="首页 点击 我")
    def click_me(self):
        self.click(self.me_button)

    # 点击分类
    @allure.step(title="首页 点击 分类")
    def click_category(self):
        self.click(self.category_button)

    # 点击购物车
    @allure.step(title="首页 点击 购物车")
    def click_shopcart(self):
        self.click(self.shopcart_button)

    # 点击首页
    @allure.step(title="首页 点击 首页")
    def click_home(self):
        self.click(self.home_button)

    # 点击放大镜
    @allure.step(title="首页 点击 放大镜")
    def click_search(self):
        self.click(self.search_button)

    # 判断是否登录
    @allure.step(title="首页 登录（没有登录时进行登录）")
    def login_if_not(self,page):
        self.click_me()
        if self.driver.current_activity !="com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        else:
            # 去登录
            page.register.click_go_login()
            # 输入用户名
            page.login.input_username("xiaoxiatest")
            # 输入密码
            page.login.input_pwd("xia123456")
            # 登录
            page.login.click_login()