import os
import pytest
from faker import Faker
from pages.login_page import LoginPage


@pytest.mark.ui
def test_correct_sign_in(login_page: LoginPage):
    username = os.getenv("GH_USER")
    password = os.getenv("GH_PASS")
    login_page.login(username, password)
    login_page.expect_login_succeeded()

@pytest.mark.ui
def test_incorrect_sign_in(login_page: LoginPage):
    fake = Faker()
    login_page.login(fake.email(), fake.password())
    login_page.expect_login_failed()
    