import pytest
from selenium import webdriver
from dotenv import load_dotenv


@pytest.fixture(scope="function")
def driver():
    load_dotenv()
    driver = webdriver.Chrome()
    yield driver
    driver.quit()