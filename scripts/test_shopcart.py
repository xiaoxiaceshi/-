import time

from base.base_driver import init_driver
from page.page import Page


class TestShopcart:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_add_shopcart(self):
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 首页 - 分类
        self.page.home.click_category()
        # 分类 - 商品列表
        self.page.category.click_goods_list()
        # 商品列表 - 商品详情
        self.page.goods_list.click_goods()
        # 记录一下，当前商品的标题
        goods_title = self.page.goods_detail.get_goods_title()
        # 商品详情 - 加入购物车
        self.page.goods_detail.click_add_shopcart()
        # 商品详情 - 选择规格
        self.page.goods_detail.click_spec()
        # 点击购物车
        self.page.goods_detail.click_shopcart()
        time.sleep(2)
        # 查看购物车中有没有商品名称
        assert  self.page.goods_detail.is_goods_title_exist(goods_title)

    def test_shopcart_price(self):
        # 登录判断
        self.page.home.login_if_not(self.page)
        # 点击购物车
        self.page.home.click_shopcart()
        # 点击全选
        self.page.shopcart.click_select_all()
        # 获得商品单价
        price = self.page.shopcart.get_price()
        # 获得当前合计价格
        current_price = self.page.shopcart.get_total_price()
        # 点击编辑
        self.page.shopcart.click_edit()
        # 增加商品数量
        self.page.shopcart.click_add()
        # 点击完成
        self.page.shopcart.click_commit()
        # 获得当前的合计价格
        new_price = self.page.shopcart.get_total_price()
        # 断言价格是否正确（之前价格 + 单价 = 现价）
        assert current_price + price == new_price

    def test_del_shopcart(self):
        # 登录
        self.page.home.login_if_not(self.page)
        # 点击购物车
        self.page.home.click_shopcart()
        # 购物车 = 判断是否有商品，如果没有则添加
        if self.page.shopcart.is_shopcart_empty():
            # 首页 - 分类
            self.page.home.click_category()
            # 分类 - 商品列表
            self.page.category.click_goods_list()
            # 商品列表 - 商品详情
            self.page.goods_list.click_goods()
            # 记录一下，当前商品的标题
            goods_title = self.page.goods_detail.get_goods_title()
            # 商品详情 - 加入购物车
            self.page.goods_detail.click_add_shopcart()
            # 商品详情 - 选择规格
            self.page.goods_detail.click_spec()

            # 两次返回
            self.page.shopcart.press_back()
            time.sleep(2)
            self.page.shopcart.press_back()
            # 点击购物车
            self.page.home.click_shopcart()

        # 点击全选
        self.page.shopcart.click_select_all()
        # 点击编辑
        self.page.shopcart.click_edit()
        # 点击删除
        self.page.shopcart.click_del()
        # 确认删除
        self.page.shopcart.click_confirm_del()
        # 断言 toast 是不是叫做 删除成功
        assert self.page.shopcart.is_toast_exist("删除成功")
        # 断言，当前页面是不是有一个叫做“购物车还是空的”
        assert self.page.shopcart.is_shopcart_empty()