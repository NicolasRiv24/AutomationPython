from selenium.webdriver.common.by import By
from Locators.Locators import InventoryPageLocators
class InventoryPageAddToCart:
    def __init__(self, driver):
        self.driver = driver
        #self.add_backpack = By.ID, "add-to-cart-sauce-labs-backpack"
        #self.add_bike_light = By.ID, "add-to-cart-sauce-labs-bike-light"
        #self.cart_button = By.ID, "shopping_cart_container"

    def click_buy_button_one(self):
        self.driver.find_element(*InventoryPageLocators.ADD_BACKPACK_BUTTON).click()

    def click_buy_button_two(self):
        self.driver.find_element(*InventoryPageLocators.ADD_BIKE_LIGHT_BUTTON).click()

    def click_cart_button(self):
        self.driver.find_element(*InventoryPageLocators.CART_BUTTON).click()
