import pytest
from faker import Faker

from pages.github.home_page import HomePage


class TestLoginPage:

    @pytest.mark.ui
    def test_correct_sign_in(
        self, github_home_page: HomePage, gh_credentials: tuple[str, str]
    ) -> None:
        if not all(gh_credentials):
            pytest.skip(reason="Credentials not provided")
        username, password = gh_credentials
        github_home_page.open()
        login_page = github_home_page.go_to_login()
        login_page.login(username, password)
        login_page.expect_login_succeeded()

    @pytest.mark.ui
    def test_incorrect_sign_in(self, github_home_page: HomePage, faker: Faker) -> None:
        github_home_page.open()
        login_page = github_home_page.go_to_login()
        login_page.login(faker.email(), faker.password())
        login_page.expect_login_failed()


class TestContactingSalesPage:

    @pytest.mark.ui
    def test_filling_name_in_contact_sales_page(
        self, github_home_page: HomePage, faker: Faker
    ) -> None:
        first_name, last_name = faker.first_name(), faker.last_name()
        github_home_page.open()
        contact_sales_page = (
            github_home_page.go_to_solutions().select_ci_cd().click_contact_sales()
        )
        contact_sales_page.fill_form(first_name, last_name)
        contact_sales_page.expect_form_filled(first_name, last_name)


class TestTopicsPageContents:

    @pytest.mark.ui
    def test_popular_topics_contents(self, github_home_page: HomePage) -> None:
        expected_topics = {"Python", "React", "CSS"}
        github_home_page.open()
        popular_topics_list = github_home_page.go_to_topics().get_popular_topics()
        assert expected_topics.issubset(popular_topics_list)
