import pytest
from faker import Faker
from pages.home_page import HomePage


class TestLoginPage:

    # @pytest.mark.skip
    @pytest.mark.ui
    def test_correct_sign_in(self, home_page: HomePage, gh_credentials: tuple[str, str]):
        if not all(gh_credentials):
            pytest.skip(reason="Credentials not provided")
        username, password = gh_credentials
        home_page.open()
        login_page = home_page.go_to_login()
        login_page.login(username, password)
        login_page.expect_login_succeeded()

    # @pytest.mark.skip
    @pytest.mark.ui
    def test_incorrect_sign_in(self, home_page: HomePage):
        fake = Faker()
        home_page.open()
        login_page = home_page.go_to_login()
        login_page.login(fake.email(), fake.password())
        login_page.expect_login_failed()


class TestContactingSalesPage:

    # @pytest.mark.skip
    @pytest.mark.ui
    def test_filling_name_in_contact_sales_page(self, home_page: HomePage, gh_name):
        if not all(gh_name):
            pytest.skip(reason="First and last names not provided")
        first_name, last_name = gh_name
        home_page.open()
        contact_sales_page = home_page.go_to_solutions().select_ci_cd().click_contact_sales()
        contact_sales_page.fill_form(first_name, last_name)
        contact_sales_page.expect_form_filled(first_name, last_name)


class TestTopicsPageContents:

    @pytest.mark.ui
    def test_popular_topics_contents(self, home_page: HomePage):
        expected_topics = {"Python", "React", "CSS"}
        home_page.open()
        popular_topics_list = home_page.go_to_topics().get_popular_topics()
        assert expected_topics.issubset(popular_topics_list)
