import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Credantial
from name import *

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

@pytest.fixture
def logo_profile(driver, registration_page):
    registration_page.find_element(*Locators.password).send_keys(Credantial.password)  
    registration_page.find_element(*Locators.email).send_keys(Credantial.email)  
    registration_page.find_element(*Locators.name).send_keys(Credantial.name)  
    registration_page.find_element(*Locators.registration_button).click()  
    WebDriverWait(registration_page, 5).until(
        expected_conditions.visibility_of_element_located(Locators.entrance_registration_page)
    )
    return driver