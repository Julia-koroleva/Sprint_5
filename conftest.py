import pytest
from selenium import webdriver
from curl import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def main_page_start(driver):
    login_page_start = main_site
    driver.get(login_page_start)
    return driver

 
@pytest.fixture
def registration_page(driver):
    login_page = register_site
    driver.get(login_page)
    return driver

