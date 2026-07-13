import os

import pytest
from faker import Faker
from dotenv import load_dotenv
from playwright.sync_api import Page
from pages.github.home_page import HomePage

GITHUB_URL = "https://github.com/"
load_dotenv()


@pytest.fixture()
def github_home_page(page: Page):
    yield HomePage(page, GITHUB_URL)


@pytest.fixture()
def gh_credentials():
    yield os.getenv("GH_USER"), os.getenv("GH_PASS")


@pytest.fixture()
def faker():
    yield Faker()