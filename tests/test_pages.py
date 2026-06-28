import pytest
import os
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from faker import Faker


class TestLoginPage:

    URL = "https://github.com/"

    @pytest.mark.ui
    def test_correct_login(self, driver):
        login_page = LoginPage(driver, self.URL)
        username = os.getenv("GH_USER")
        password = os.getenv("GH_PASS")
        login_page.open()
        login_page.login(username, password)
        login_page.wait_until_login_succeeded()
        assert "/login" not in driver.current_url
    
    @pytest.mark.ui
    def test_incorrect_login(self, driver):
        login_page = LoginPage(driver, self.URL)
        fake = Faker()
        login_page.open()
        login_page.login(fake.email(), fake.password())
        login_page.wait_until_login_failed()
