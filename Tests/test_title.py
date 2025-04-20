import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.config import Config

class TestTitle:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_home_page_title(self, setup):
        self.driver.get(Config.BASE_URL)
        login_page = LoginPage(self.driver)
        assert login_page.get_login_page_title() == "OrangeHRM", \
            f"Expected title to be 'OrangeHRM' but got '{login_page.get_login_page_title()}'"
