from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,feature,timeout=10,poll_frequency=1):
        feature_by,feature_value = feature
        element = WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x : x.find_element(feature_by,feature_value))
        return element

    def find_elements(self,feature,timeout=10,poll_frequency=1):
        feature_by,feature_value = feature
        element = WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x : x.find_elements(feature_by,feature_value))
        return element

    def click(self,feature):
        self.find_element(feature).click()

    def input(self,feature,content):
        self.find_element(feature).send_keys(content)

    def clear(self,feature):
        self.find_element(feature).clear()

    def press_back(self):
        self.driver.press_keycode(4) # 返回

    def press_enter(self):
        self.driver.press_keycode(66) # 回车