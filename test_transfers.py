from selenium.webdriver.common.by import By
from locators import Locators
from geniration_em_pas import User
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from curl import *
from data import Credantial
from selenium import webdriver

def test_transfers_account(main_page_start):
    main_page_start.find_element(*Locators.entrance_button).click()
    WebDriverWait(main_page_start, 5).until(
        expected_conditions.visibility_of_element_located(Locators.button)
    )
    assert main_page_start.current_url.endswith('/login')
    
def test_personal_account_transfer_constructor(main_page_start, logo_profile):
    
    logo_profile.find_element(*Locators.constructor).click()
    WebDriverWait(logo_profile, 5).until(
        expected_conditions.visibility_of_element_located(Locators.buns)
    )
    assert main_page_start.find_element(*Locators.make_burger).text == 'Соберите бургер'

def test_personal_account_transfer_logo(main_page_start, logo_profile):
    
    logo_profile.find_element(*Locators.logo).click()
    WebDriverWait(logo_profile, 5).until(
        expected_conditions.visibility_of_element_located(Locators.buns)
    )
    assert main_page_start.find_element(*Locators.make_burger).text == 'Соберите бургер'