
from Pages.InventoryPageAddToCart import InventoryPageAddToCart
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckOutPage
from Pages.CheckOutPageTwo import CheckOutPageTwo
from Pages.CheckOutComplete import CheckOutComplete
from Pages.SideBar import SideBar
from selenium.webdriver.common.by import By
import unittest
from Pages.LoginPage import LoginPage
from Resources.BrowserSetup import BrowserSetup
from Locators.Locators import LoginPageLocators
class LoginLogOutThirdOption(unittest.TestCase):
    def test_login_and_logout(self):
        # Can change "chrome" for "firefox" or "edge" in order to change the browser
        driver = BrowserSetup.initialize_browser("chrome")

        # Pages
        login_page = LoginPage(driver)
        inventory_page = InventoryPageAddToCart(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckOutPage(driver)
        checkout_page_two = CheckOutPageTwo(driver)
        checkout_complete_page = CheckOutComplete(driver)
        side_bar = SideBar(driver)

        # navigate to the page
        driver.get("https://www.saucedemo.com/")

        # Assertion for login page
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/")
        # Agrega más afirmaciones según sea necesario

        # LogIn Page
        login_page.set_text_in_username_box("standard_user")
        login_page.set_text_in_password_box("secret_sauce")
        login_page.click_login_button()

        # Assertions for inventory
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/inventory.html")
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").is_displayed(),
                        "El icono no está presente en el botón.")

        # Buying things
        inventory_page.click_buy_button_one()
        inventory_page.click_buy_button_two()

        # Cart Page
        inventory_page.click_cart_button()

        # Assertions for cart page
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/cart.html")

        # CheckOut page
        cart_page.click_checkout_button()

        # Assertions for cart page
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/checkout-step-one.html")

        # Client information filling
        checkout_page.set_text_in_first_name_box("Susana")
        checkout_page.set_text_in_last_name_box("Oria")
        checkout_page.set_text_in_postal_code_box("000")
        checkout_page.click_continue_button()

        # Assertions for second checkout page
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/checkout-step-two.html")

        # Paying
        checkout_page_two.click_finish_button()

        # Assertion for CheckOutComplete Page
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/checkout-complete.html")
        self.assertEqual(driver.find_element(By.XPATH, "//h2[normalize-space()='Thank you for your order!']").text,
                         "Thank you for your order!")

        # Complete the buy
        checkout_complete_page.click_back_home_button()

        # SideBar
        # Assertion after finish the buy
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/inventory.html")

        # LogOut
        side_bar.click_side_bar()
        side_bar.click_log_out_button()

        # Close the Browser
        driver.quit()

# Verify if the script is executing as the main program
if __name__ == "__main__":
    unittest.main()
