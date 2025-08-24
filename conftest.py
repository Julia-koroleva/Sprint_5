import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from geniration_em_pas import User
from locators import Locators
from curl import *
from data import Credantial

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def main_site(driver):
    login_page = main_site
    driver.get(login_page)
    return driver

@pytest.fixture
def login_password(driver):
    driver.find_element(*Locators.email_login).send_keys(Credantial.email)
    driver.find_element(*Locators.password_login).send_keys(Credantial.passord)
    driver.find_element(*Locators.entrance_login_page).click()
    return driver

@pytest.fixture
def login_page(driver):
    login_page = login_site
    driver.get(login_page)
    return driver
    
@pytest.fixture
def registratin_page(driver):
    login_page = register_site
    driver.get(login_page)
    return driver

@pytest.fixture
def profile_page(driver):
    page = profile_site
    driver.get(page)
    return driver