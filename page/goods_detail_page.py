import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class GoodsDetailPage(BaseAction):

    # 加入购物车
    add_shopcart_button = By.ID,"com.yunmall.lc:id/btn_add_to_shopping_cart"

    # 确认按钮
    commit_button = By.XPATH,"//*[@text='确认']"

    # 商品标题特征
    goods_title_feature = By.ID,"com.yunmall.lc:id/tv_product_title"

    # 购物车按钮
    shopcart_button = By.ID,"com.yunmall.lc:id/btn_shopping_cart"

    # 点击加入购物车
    @allure.step(title="商品详情 点击 加入购物车")
    def click_add_shopcart(self):
        self.find_element_with_scroll(self.add_shopcart_button).click()

    # 点击确认
    @allure.step(title="商品详情 点击 确认")
    def click_commit(self):
        self.find_element_with_scroll(self.commit_button).click()

    # 根据 “请选择 分类 规格”获取，请选择后面的第一个规格的名字
    @allure.step(title="商品详情 获取 toast首个分类标签")
    def get_choose_spec(self,text):
        return text.split(" ")[1]

    # 选择 规格
    @allure.step(title="商品详情 选择 规格")
    def click_spec(self):
        while True:
            self.click_commit()
            time.sleep(1)
            if self.is_toast_exist("请选择"):
                spec = self.get_choose_spec(self.get_toast_text("请选择"))
                spec_feature = By.XPATH,"//*[@text='%s']/../*[2]/*[1]" % spec
                self.find_element_with_scroll(spec_feature).click()
                time.sleep(3)
            else:
                break

    # 获取商品名称
    @allure.step(title="商品详情 获取 商品名称")
    def get_goods_title(self):
        return  self.get_text(self.goods_title_feature)

    # 点击购物车
    @allure.step(title="商品详情 点击 购物车")
    def click_shopcart(self):
        self.find_element_with_scroll(self.shopcart_button).click()

    # 判断商品名称在不在
    @allure.step(title="购物车 判断 列表中有没有该商品名称")
    def is_goods_title_exist(self,title):
        title_feature = By.XPATH,"//*[@text='%s']" % title
        return  self.is_feature_exist(title_feature)