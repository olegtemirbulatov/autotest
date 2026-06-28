from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def open(self) -> LoginPage:
        self.driver.get(self.url)
        return self

    def login(self, username: str, password: str) -> LoginPage:
        wait = WebDriverWait(self.driver, timeout=10)
        sign_in_link = wait.until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, "a.HeaderMenu-link--sign-in")
            )
        )
        sign_in_link.click()
        wait.until(lambda d: "/login" in d.current_url)

        login_field = wait.until(
            ec.presence_of_element_located(
                (By.ID, "login_field")
            )
        )
        password_field = wait.until(
            ec.presence_of_element_located(
                (By.ID, "password")
            )
        )
        login_field.send_keys(username)
        password_field.send_keys(password)

        sign_in_button = wait.until(
            ec.element_to_be_clickable(
                (By.NAME, "commit")
            )
        )
        sign_in_button.click()
        return self
    
    def wait_until_login_succeeded(self):
        WebDriverWait(driver=self.driver, timeout=10).until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, "span.styles-module__contextCrumbLast__tI2e3")
            )
        )

    def wait_until_login_failed(self):
        WebDriverWait(driver=self.driver, timeout=10).until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, "div[role='alert']")
            )
        )