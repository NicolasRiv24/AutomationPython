from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = By.ID, "user-name"
        self.password_field = By.ID, "password"
        self.login_button = By.ID, "login-button"

    def set_text_in_username_box(self, text):
        self.driver.find_element(*self.username_field).send_keys(text)

    def set_text_in_password_box(self, text):
        self.driver.find_element(*self.password_field).send_keys(text)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
