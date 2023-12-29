from selenium.webdriver.common.by import By
from Locators.Locators import CartPageLocators
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        #self.checkout_button = By.ID, "checkout"

    def click_checkout_button(self):
        self.driver.find_element(*CartPageLocators.CHECKOUT_BUTTON).click()