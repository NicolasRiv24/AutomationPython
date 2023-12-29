from selenium import webdriver

class BrowserSetup:
    @staticmethod
    def initialize_browser(browser_name):
        # Function to initialize a web browser based on the provided name

        if browser_name.lower() == "chrome":
            # If the browser is Chrome, configure Chrome-specific options

            options = webdriver.ChromeOptions()
            options.add_argument("--incognito")
            options.add_argument("--remote-allow-origins=*")
            options.add_argument("--disable-blink-features=AutomationControlled")
            driver = webdriver.Chrome(options=options)

            # If the browser is Firefox, configure Firefox-specific options

        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("-private")
            driver = webdriver.Firefox(options=options)

            # If the browser is Edge, initialize a new Edge driver

        elif browser_name.lower() == "edge":
            driver = webdriver.Edge()
        else:
            # If the browser name is not recognized, raise a ValueError

            raise ValueError("Invalid browser name: " + browser_name)

        return driver
