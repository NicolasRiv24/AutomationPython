from selenium.webdriver.common.by import By
from Locators.Locators import CheckOutPageLocators
from Resources.WaitToRender import WaitToRender
class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
        #self.first_name_field = By.ID, "first-name"
        #self.last_name_field = By.ID, "last-name"
        #self.postal_code_box = By.ID, "postal-code"
        #self.continue_button = By.ID, "continue"

    def set_text_in_first_name_box(self, text):
        self.driver.find_element(*CheckOutPageLocators.FIRST_NAME_FIELD).send_keys(text)

    def set_text_in_last_name_box(self, text):
        self.driver.find_element(*CheckOutPageLocators.LAST_NAME_FIELD).send_keys(text)

    def set_text_in_postal_code_box(self, text):
        self.driver.find_element(*CheckOutPageLocators.POSTAL_CODE_FIELD).send_keys(text)

    def click_continue_button(self):
        self.driver.find_element(*CheckOutPageLocators.CONTINUE_BUTTON).click()