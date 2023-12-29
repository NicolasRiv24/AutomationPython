class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = "user-name"
        self.password_field = "password"
        self.login_button = "login-button"

    def set_text_in_username_box(self, text):
        self.driver.find_element_by_id(self.username_field).send_keys(text)

    def set_text_in_password_box(self, text):
        self.driver.find_element_by_id(self.password_field).send_keys(text)

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button).click()
