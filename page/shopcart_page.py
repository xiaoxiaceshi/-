from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class ShopcartPage(BaseAction):

    # 全选按钮
    select_all_button = By.ID,"com.yunmall.lc:id/tv_select_all"

    # 合计价格
    total_price_text = By.ID,"com.yunmall.lc:id/tv_count_money"

    # 编辑按钮
    edit_button = By.XPATH,"//*[@text='编辑']"

    # 完成按钮
    commit_button = By.XPATH, "//*[@text='完成']"

    # 删除按钮
    del_button = By.ID,"com.yunmall.lc:id/tv_del_all"

    # 删除确认按钮
    confirm_del_button = By.XPATH,"//*[@text='确认']"

    # 添加数量
    add_button = By.ID,"com.yunmall.lc:id/iv_add"

    # 单价
    price_text = By.ID,"com.yunmall.lc:id/tv_price"

    # 点击全选按钮
    @allure.step(title="购物车 点击 全选")
    def click_select_all(self):
        self.find_element_with_scroll(self.select_all_button).click()

    # 点击添加
    @allure.step(title="购物车 点击 +")
    def click_add(self):
        self.click(self.add_button)

    # 获得商品单价
    @allure.step(title="购物车 获得 商品单价")
    def get_price(self):
        return  self.deal_with_price(self.get_text(self.price_text))

    # 获得合计价格
    @allure.step(title="购物车 获得 总价")
    def get_total_price(self):
        # 获得单价的文字
        price_text= self.get_text(self.total_price_text)
        # 通过deal_with_price去掉前面的￥，并且转化为float类型
        return  self.deal_with_price(price_text)

    # 价格处理
    @allure.step(title="购物车 处理 价格")
    def deal_with_price(self,text):
        return float(text[2:])

    # 点击编辑
    @allure.step(title="购物车 点击 编辑")
    def click_edit(self):
        self.click(self.edit_button)

    # 点击完成
    @allure.step(title="购物车 点击 完成")
    def click_commit(self):
        self.click(self.commit_button)

    # 点击删除
    @allure.step(title="购物车 点击 删除")
    def click_del(self):
        self.click(self.del_button)

    # 确认删除
    @allure.step(title="购物车 点击 确认删除")
    def click_confirm_del(self):
        self.click(self.confirm_del_button)

    # 判断购物车是否为空
    @allure.step(title="购物车 判断 购物车是否为空")
    def is_shopcart_empty(self):
        empty_tip_text = By.XPATH,"//*[contains(@text,'购物车还是空的')]"
        return self.is_feature_exist(empty_tip_text)


