import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import Page
from bank_account import BankAccount
from pages.login_page import LoginPage


load_dotenv()

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
def login_page(page: Page) -> LoginPage:
    return LoginPage(page, "https://github.com/")

@pytest.fixture()
def gh_credentials():
    return os.getenv("GH_USER"), os.getenv("GH_PASS")