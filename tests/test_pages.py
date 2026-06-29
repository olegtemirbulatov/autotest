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
    def test_correct_login(self, driver, gh_credentials):
        if not all(gh_credentials):
            pytest.skip(reason="Credentials not provided")
        username, password = gh_credentials
        login_page = LoginPage(driver, self.URL)
        login_page.open()
        login_page.login(username, password)
        assert login_page.wait_until_login_succeeded() is not None
    
    @pytest.mark.ui
    def test_incorrect_login(self, driver):
        login_page = LoginPage(driver, self.URL)
        fake = Faker()
        login_page.open()
        login_page.login(fake.email(), fake.password())
        assert login_page.wait_until_login_failed() is not None
