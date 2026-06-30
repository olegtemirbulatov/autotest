import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import Page
from tests.bank_account import BankAccount
from pages.github.home_page import HomePage
from pages.duckduckgo.search_page import SearchPage


load_dotenv()
GITHUB_URL = "https://github.com/"
GOOGLE_URL = "https://duckduckgo.com/"


# GITHUB
@pytest.fixture()
def github_home_page(page: Page):
    yield HomePage(page, GITHUB_URL)

@pytest.fixture()
def gh_credentials():
    yield os.getenv("GH_USER"), os.getenv("GH_PASS")

@pytest.fixture()
def gh_name():
    yield os.getenv("GH_FIRST_NAME"), os.getenv("GH_LAST_NAME")


# DUCKDUCKGO
@pytest.fixture()
def ddg_search_page(page: Page):
    yield SearchPage(page, GOOGLE_URL)


# OTHER
@pytest.fixture()
def account():
    return BankAccount("Ivan", 1000)

@pytest.fixture(autouse=True)
def printing_autouse_flag():
    print("Before test")
    yield
    print("After test")

@pytest.fixture()
def output_file():
    filename = "./test.txt"
    with open(filename, '+a') as file:
        file.write("Before test\n")
    yield filename
    with open(filename, '+a') as file:
        file.write("After test\n\n")