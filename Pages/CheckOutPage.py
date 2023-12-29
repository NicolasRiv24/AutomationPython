from selenium.webdriver.common.by import By

class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = By.ID, "first-name"
        self.last_name_field = By.ID, "last-name"
        self.postal_code_box = By.ID, "postal-code"
        self.continue_button = By.ID, "continue"

    def set_text_in_first_name_box(self, text):
        self.driver.find_element(*self.first_name_field).send_keys(text)

    def set_text_in_last_name_box(self, text):
        self.driver.find_element(*self.last_name_field).send_keys(text)

    def set_text_in_postal_code_box(self, text):
        self.driver.find_element(*self.postal_code_box).send_keys(text)

    def click_continue_button(self):
        self.driver.find_element(*self.continue_button).click()
