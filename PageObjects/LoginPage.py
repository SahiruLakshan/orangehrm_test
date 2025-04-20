from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    LOGIN_PAGE_TITLE = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[1]/img')

    def get_login_page_title(self):
        return self.driver.title

    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(self.PASSWORD_FIELD)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()