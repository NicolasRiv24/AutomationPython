from selenium.webdriver.common.by import By

class CheckOutComplete:
    def __init__(self, driver):
        self.driver = driver
        self.back_home_button = By.ID, "back-to-products"

    def click_back_home_button(self):
        self.driver.find_element(*self.back_home_button).click()
