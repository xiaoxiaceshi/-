from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class AboutPage(BaseAction):

    # 版本更新
    update_button = By.ID,"com.yunmall.lc:id/about_version_update"

    #点击版本更新
    @allure.step(title="关于页 点击 版本更新")
    def click_update(self):
        self.find_element_with_scroll(self.update_button).click()