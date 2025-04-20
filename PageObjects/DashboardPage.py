from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    DASHBOARD_HEADER = (By.XPATH, '//h6[text()="Dashboard"]')
    MY_LEAVE_BUTTON = (By.XPATH, '//button[@title="My Leave"]')
    USER_DROPDOWN = (By.XPATH, '//span[@class="oxd-userdropdown-tab"]')
    LOGOUT_LINK = (By.XPATH, '//a[text()="Logout"]')

    def get_dashboard_header(self):
        return self.wait.until(EC.presence_of_element_located(self.DASHBOARD_HEADER)).text

    def click_my_leave(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_LEAVE_BUTTON)).click()

    def click_user_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_DROPDOWN)).click()

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()