from selenium.webdriver.common.by import By
from Locators.Locators import LoginPageLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def set_text_in_username_box(self, text):
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(text)

    def set_text_in_password_box(self, text):
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(text)

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
