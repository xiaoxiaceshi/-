import time
from base.base_driver import init_driver


class TestLogin:

    def setup(self):
        self.driver = init_driver()

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_login(self):
        print("hello")
        assert 1

    def test_login1(self):
        print("1111")
        assert 0
