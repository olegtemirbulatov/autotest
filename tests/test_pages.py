import pytest
from faker import Faker
from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestLoginPage:

    @pytest.mark.ui
    def test_correct_sign_in(self, login_page: LoginPage, gh_credentials: tuple[str, str]):
        if not all(gh_credentials):
            pytest.skip(reason="Credentials not provided")
        username, password = gh_credentials
        login_page.open()
        login_page.login(username, password)
        login_page.expect_login_succeeded()

    @pytest.mark.ui
    def test_incorrect_sign_in(self, login_page: LoginPage):
        fake = Faker()
        login_page.open()
        login_page.login(fake.email(), fake.password())
        login_page.expect_login_failed()


class TestContactingSalesPage:

    @pytest.mark.ui
    def test_filling_name_in_contact_sales_page(self, home_page: HomePage, gh_name):
        if not all(gh_name):
            pytest.skip(reason="First and last names not provided")
        first_name, last_name = gh_name
        home_page.open()
        contact_sales_page = home_page.go_to_solutions().select_ci_cd().click_contact_sales()
        contact_sales_page.fill_form(first_name, last_name)
        contact_sales_page.expect_form_filled(first_name, last_name)
