import pytest
import os
from selenium import webdriver
from dotenv import load_dotenv


load_dotenv()

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def gh_credentials():
    return os.getenv("GH_USER"), os.getenv("GH_PASS")