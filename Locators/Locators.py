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

class CartPageLocators:
    CHECKOUT_BUTTON = By.ID, "checkout"

class CheckOutPageLocators:
    FIRST_NAME_FIELD = By.ID, "first-name"
    LAST_NAME_FIELD = By.ID, "last-name"
    POSTAL_CODE_FIELD = By.ID, "postal-code"
    CONTINUE_BUTTON = By.ID, "continue"