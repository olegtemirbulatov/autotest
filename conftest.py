import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import Page
from tests.bank_account import BankAccount
from pages.login_page import LoginPage
from pages.home_page import HomePage


load_dotenv()
BASE_URL = "https://github.com/"

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

@pytest.fixture()
def home_page(page: Page):
    yield HomePage(page, BASE_URL)

@pytest.fixture()
def gh_credentials():
    yield os.getenv("GH_USER"), os.getenv("GH_PASS")

@pytest.fixture()
def gh_name():
    yield os.getenv("GH_FIRST_NAME"), os.getenv("GH_LAST_NAME")
