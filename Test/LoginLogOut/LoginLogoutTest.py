import unittest
from Pages import *
from Resources.BrowserSetup import BrowserSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.LoginPage import LoginPage
from Resources.WaitToRender import WaitToRender
from Pages.InventoryPageAddToCart import InventoryPageAddToCart
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckOutPage
from Pages.CheckOutPageTwo import CheckOutPageTwo
from Pages.CheckOutComplete import CheckOutComplete
from Pages.SideBar import SideBar
from Resources.BrowserSetup import BrowserSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from Pages.LoginPage import LoginPage
from Resources.BrowserSetup import BrowserSetup
class LoginLogOutThirdOption(unittest.TestCase):
    def test_login_and_logout(self):
        # Puedes cambiar "chrome" por "firefox" o "edge" para cambiar el navegador
        driver = BrowserSetup.initialize_browser("edge")

        # Inicializar las páginas
        login_page = LoginPage(driver)
        inventory_page = InventoryPageAddToCart(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckOutPage(driver)
        checkout_page_two = CheckOutPageTwo(driver)
        checkout_complete_page = CheckOutComplete(driver)
        side_bar = SideBar(driver)

        # Navegar a la página
        driver.get("https://www.saucedemo.com/")

        # Primeras afirmaciones para la página de inicio de sesión
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/")
        # Agrega más afirmaciones según sea necesario

        # Iniciar sesión
        login_page.set_text_in_username_box("standard_user")
        login_page.set_text_in_password_box("secret_sauce")
        login_page.click_login_button()

        # Afirmaciones para la página de inventario
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/inventory.html")
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").is_displayed(),
                        "El icono no está presente en el botón.")

        # Comprar productos
        inventory_page.click_buy_button_one()
        inventory_page.click_buy_button_two()

        # Ir a la página del carrito
        inventory_page.click_cart_button()

        # Afirmaciones para la página del carrito
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/cart.html")

        # Ir al proceso de pago
        cart_page.click_checkout_button()

        # Afirmaciones para la página de pago
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/checkout-step-one.html")

        # Completar información del cliente
        checkout_page.set_text_in_first_name_box("Susana")
        checkout_page.set_text_in_last_name_box("Oria")
        checkout_page.set_text_in_postal_code_box("000")
        checkout_page.click_continue_button()

        # Afirmaciones para la segunda página de pago
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/checkout-step-two.html")

        # Completar el proceso de pago
        checkout_page_two.click_finish_button()

        # Afirmaciones para la página de pago completo
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/checkout-complete.html")
        self.assertEqual(driver.find_element(By.XPATH, "//h2[normalize-space()='Thank you for your order!']").text,
                         "Thank you for your order!")

        # Completar la compra
        checkout_complete_page.click_back_home_button()

        # Menú lateral de cierre de sesión
        # Afirmaciones para finalizar la compra
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/inventory.html")

        side_bar.click_side_bar()
        side_bar.click_log_out_button()

        # Cerrar el navegador
        driver.quit()


if __name__ == "__main__":
    unittest.main()
