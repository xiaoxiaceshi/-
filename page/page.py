from page.about_page import AboutPage
from page.area_list_page import AreaListPage
from page.category_page import CategoryPage
from page.edit_area_page import EditAreaPage
from page.goods_detail_page import GoodsDetailPage
from page.goods_list_page import GoodsListPage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MePage
from page.register_page import RegisterPage
from page.search_page import SearchPage
from page.setting_page import SettingPage
from page.shopcart_page import ShopcartPage
from page.vip_page import VipPage


class Page:

    def __init__(self,driver):
        self.driver = driver

    # 首页
    @property
    def home(self):
        return HomePage(self.driver)

    #登录页
    @property
    def login(self):
        return LoginPage(self.driver)

    # 个人中心
    @property
    def me(self):
        return MePage(self.driver)

    #注册页
    @property
    def register(self):
        return RegisterPage(self.driver)

    # 设置页
    @property
    def setting(self):
        return SettingPage(self.driver)

    # 关于页
    @property
    def about(self):
        return AboutPage(self.driver)

    # 会员页
    @property
    def vip(self):
        return VipPage(self.driver)

    #地址列表页
    @property
    def area_list(self):
        return AreaListPage(self.driver)

   # 编辑/新增页
    @property
    def edit_area(self):
        return EditAreaPage(self.driver)

    # 商品分类页
    @property
    def category(self):
        return CategoryPage(self.driver)

    # 商品列表页
    @property
    def goods_list(self):
        return GoodsListPage(self.driver)

    # 商品详情页
    @property
    def goods_detail(self):
        return GoodsDetailPage(self.driver)

    # 购物车页
    @property
    def shopcart(self):
        return ShopcartPage(self.driver)

    # 搜索页
    @property
    def search(self):
        return SearchPage(self.driver)
