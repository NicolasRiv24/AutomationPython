from selenium import webdriver

class BrowserSetup:
    @staticmethod
    def initialize_browser(browser_name):
        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--incognito")
            options.add_argument("--remote-allow-origins=*")
            options.add_argument("--disable-blink-features=AutomationControlled")
            driver = webdriver.Chrome(options=options)
        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("-private")
            driver = webdriver.Firefox(options=options)
        elif browser_name.lower() == "edge":
            driver = webdriver.Edge()
        else:
            raise ValueError("Invalid browser name: " + browser_name)

        return driver
