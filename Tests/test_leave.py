import os
import pytest
from selenium import webdriver  # This was missing
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from PageObjects.LeavePage import LeavePage
from Utilities.config import Config
from datetime import datetime


class TestLeave:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Config.BASE_URL)

        login_page = LoginPage(self.driver)
        login_page.enter_username(Config.USERNAME)
        login_page.enter_password(Config.PASSWORD)
        login_page.click_login()

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//h6[text()="Dashboard"]'))
        )

        yield
        self.driver.quit()

    def test_leave_functionality(self, setup):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_my_leave()

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "oxd-layout")]'))
        )

        leave_page = LeavePage(self.driver)
        header_text = leave_page.get_leave_header()

        if not os.path.exists("Screenshots"):
            os.makedirs("Screenshots")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"Screenshots/leave_page_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)

        assert header_text, "No header text found - element not located"
        assert any(phrase in header_text for phrase in ["My Leave", "Leave List", "Leave"]), \
            f"Expected leave-related header but got: '{header_text}'"