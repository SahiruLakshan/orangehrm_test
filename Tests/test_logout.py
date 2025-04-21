import os
import pytest
from datetime import datetime
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from Utilities.config import Config


class TestLogout:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Config.BASE_URL)

        login_page = LoginPage(self.driver)
        login_page.enter_username(Config.USERNAME)
        login_page.enter_password(Config.PASSWORD)
        login_page.click_login()

        yield
        self.driver.quit()

    def test_logout_functionality(self, setup):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_user_dropdown()

        if not os.path.exists("Screenshots"):
            os.makedirs("Screenshots")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"Screenshots/logout_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)

        dashboard_page.click_logout()

        login_page = LoginPage(self.driver)
        assert "OrangeHRM" in login_page.get_login_page_title()
