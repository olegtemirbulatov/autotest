import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from faker import Faker


class TestLoginPage:

    URL = "https://github.com/"

    # @pytest.mark.skip
    @pytest.mark.ui
    def test_correct_login(self, home_page: HomePage, gh_credentials):
        if not all(gh_credentials):
            pytest.skip(reason="Credentials not provided")
        username, password = gh_credentials
        login_page = home_page.open().go_to_login().login(username, password)
        assert login_page.wait_until_login_succeeded() is not None
    
    # @pytest.mark.skip
    @pytest.mark.ui
    def test_incorrect_login(self, home_page: HomePage):
        fake = Faker()
        login_page = home_page.open().go_to_login().login(fake.email(), fake.password())
        assert login_page.wait_until_login_failed() is not None


class TestTopicsPageContents:

    @pytest.mark.ui
    def test_popular_topics_contents(self, home_page: HomePage):
        expected_topics = {"Python", "React", "CSS"}
        home_page.open()
        popular_topics_list = home_page.go_to_topics().get_popular_topics()
        assert expected_topics.issubset(popular_topics_list)
