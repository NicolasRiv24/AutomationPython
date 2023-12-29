from selenium.webdriver.common.by import By

class CheckOutPageTwo:
    def __init__(self, driver):
        self.driver = driver
        self.finish_button = By.ID, "finish"

    def click_finish_button(self):
        self.driver.find_element(*self.finish_button).click()
