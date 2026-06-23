import os
import pytest
from faker import Faker
from pages.github_page import GithubPage
from playwright.sync_api import expect


@pytest.mark.ui
def test_correct_sign_in(github_page: GithubPage):
    username = os.getenv("GH_USER")
    password = os.getenv("GH_PASS")
    github_page.sign_in(username, password)
    expect(github_page.page.locator("span.styles-module__contextCrumbLast__tI2e3")).to_be_visible()

@pytest.mark.ui
def test_incorrect_sign_in(github_page: GithubPage):
    fake = Faker()
    github_page.sign_in(fake.email(), fake.password())
    expect(github_page.page.get_by_text("Incorrect username or password")).to_be_visible()