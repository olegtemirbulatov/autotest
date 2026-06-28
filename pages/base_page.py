class BasePage:
    def __init__(self, driver, url):
        self.url = url
        self.driver = driver

    