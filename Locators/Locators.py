# locators.py
from selenium.webdriver.common.by import By


#Locators for LoginPage
class LoginPageLocators:
    USERNAME_FIELD = By.ID, "user-name"
    PASSWORD_FIELD = By.ID, "password"
    LOGIN_BUTTON = By.ID, "login-button"

class InventoryPageLocators:
    ADD_BACKPACK_BUTTON = By.ID, "add-to-cart-sauce-labs-backpack"
    ADD_BIKE_LIGHT_BUTTON = By.ID, "add-to-cart-sauce-labs-bike-light"
    CART_BUTTON = By.ID, "shopping_cart_container"