from selenium.webdriver.common.by import By
from Resources.WaitToRender import WaitToRender
class SideBar:
    def __init__(self, driver):
        self.driver = driver
        self.side_bar_button = By.ID, "react-burger-menu-btn"
        self.log_out_button = By.ID, "logout_sidebar_link"

    def click_side_bar(self):
        self.driver.find_element(*self.side_bar_button).click()

    def click_log_out_button(self):
        WaitToRender.element_by_id(self.driver, "logout_sidebar_link")
        self.driver.find_element(*self.log_out_button).click()
