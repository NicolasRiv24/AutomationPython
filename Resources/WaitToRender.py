from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WaitToRender:
    @staticmethod
    def element_by_id(driver, element_id):
        try:
            WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.ID, element_id)))
            return driver.find_element(By.ID, element_id)
        except TimeoutException:
            print(f"Element with ID '{element_id}' not found within the specified time.")
            return None

    @staticmethod
    def element_by_xpath(driver, element_xpath):
        try:
            WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
            return driver.find_element(By.XPATH, element_xpath)
        except TimeoutException:
            print(f"Element with XPath '{element_xpath}' not found within the specified time.")
            return None

    @staticmethod
    def page_by_url(driver, url):
        try:
            WebDriverWait(driver, 8).until(EC.url_to_be(url))
        except TimeoutException:
            print(f"URL '{url}' not reached within the specified time.")
