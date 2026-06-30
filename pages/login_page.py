from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    LOGIN_FIELD_LOCATOR = (By.ID, "login_field")
    PASSWORD_FIELD_LOCATOR = (By.ID, "password")
    SIGN_IN_BUTTON_LOCATOR = (By.NAME, "commit")
    SUCCESS_ELEMENT_LOCATOR = (By.XPATH, "//span[text()='Dashboard']")
    ERROR_ALERT_LOCATOR = (By.CSS_SELECTOR, "div[role='alert']")

    def login(self, username: str, password: str) -> LoginPage:
        login_field = self.wait.until(
            ec.presence_of_element_located(self.LOGIN_FIELD_LOCATOR)
        )
        password_field = self.wait.until(
            ec.presence_of_element_located(self.PASSWORD_FIELD_LOCATOR)
        )
        login_field.send_keys(username)
        password_field.send_keys(password)

        sign_in_button = self.wait.until(
            ec.element_to_be_clickable(self.SIGN_IN_BUTTON_LOCATOR)
        )
        sign_in_button.click()
        return self
    
    def wait_until_login_succeeded(self):
        return self.wait.until(
            ec.presence_of_element_located(self.SUCCESS_ELEMENT_LOCATOR)
        )

    def wait_until_login_failed(self):
        return self.wait.until(
            ec.presence_of_element_located(self.ERROR_ALERT_LOCATOR)
        )