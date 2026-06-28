import pytest
from selenium import webdriver
from dotenv import load_dotenv


@pytest.fixture(scope="function")
def driver():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()