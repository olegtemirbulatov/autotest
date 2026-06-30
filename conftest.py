import pytest
import os
from selenium import webdriver
from dotenv import load_dotenv
from pages.home_page import HomePage


load_dotenv()
BASE_URL = "https://github.com/"

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def home_page(driver):
    yield HomePage(driver, BASE_URL)

@pytest.fixture(scope="function")
def gh_credentials():
    yield os.getenv("GH_USER"), os.getenv("GH_PASS")