import random
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class GoodsListPage(BaseAction):

    # 商品详情按钮
    goods_button = By.ID,"com.yunmall.lc:id/iv_element_1"

    # 随机点击 商品详情
    @allure.step(title="商品列表 点击 任一商品")
    def click_goods(self):
        goods = self.find_elements(self.goods_button)
        goods_count = len(goods)
        goods_index = random.randint(0,goods_count-1)
        goods[goods_index].click()
