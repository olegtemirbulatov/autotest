import os
import pytest
from faker import Faker
from pages.login_page import LoginPage


@pytest.mark.ui
def test_correct_sign_in(login_page: LoginPage, gh_credentials: tuple[str, str]):
    username, password = gh_credentials
    login_page.open()
    login_page.login(username, password)
    login_page.expect_login_succeeded()

@pytest.mark.ui
def test_incorrect_sign_in(login_page: LoginPage):
    fake = Faker()
    login_page.open()
    login_page.login(fake.email(), fake.password())
    login_page.expect_login_failed()
    