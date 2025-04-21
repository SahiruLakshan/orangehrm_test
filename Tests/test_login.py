import os
import pytest
from datetime import datetime
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

    def test_login_functionality(self, setup):
        self.driver.get(Config.BASE_URL)
        login_page = LoginPage(self.driver)
        login_page.enter_username(Config.USERNAME)
        login_page.enter_password(Config.PASSWORD)
        login_page.click_login()

        dashboard_page = DashboardPage(self.driver)
        dashboard_header = dashboard_page.get_dashboard_header()

        if not os.path.exists("Screenshots"):
            os.makedirs("Screenshots")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"Screenshots/login_test_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)

        assert dashboard_header == "Dashboard", f"Expected 'Dashboard' but got '{dashboard_header}'"
