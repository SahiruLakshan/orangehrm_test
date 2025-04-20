import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from Utilities.config import Config


class TestLogin:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_home_page_title(self, setup):
        self.driver.get(Config.BASE_URL)
        login_page = LoginPage(self.driver)
        assert "OrangeHRM" in login_page.get_login_page_title()

    def test_login_functionality(self, setup):
        self.driver.get(Config.BASE_URL)
        login_page = LoginPage(self.driver)
        login_page.enter_username(Config.USERNAME)
        login_page.enter_password(Config.PASSWORD)
        login_page.click_login()

        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.get_dashboard_header() == "Dashboard"