import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page
from bank_account import BankAccount
from pages.login_page import LoginPage


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
    load_dotenv()
    url = "https://github.com/"
    lp = LoginPage(page, url)
    lp.open()
    return lp
