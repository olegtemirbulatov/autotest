from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    
    def __init__(self, driver, url):
        self.url = url
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)

    def open(self):
        self.driver.get(self.url)
        return self
    