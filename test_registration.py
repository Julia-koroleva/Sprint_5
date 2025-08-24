from selenium.webdriver.common.by import By
from locators import Locators
from geniration_em_pas import User
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from curl import *

def test_registration(registration_page):
    driver = registration_page
    

    driver.find_element(*Locators.password_registration).send_keys(*User.email)
    driver.find_element(*Locators.email_reg).send_keys(*User.email)
    driver.find_element(*Locators.name_registration).send_keys('Name')
    driver.find_element(*Locators.entrance_login_page).click()
    
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.cabinet)
    )
    
    email_field = registration_page.find_element(*Locators.email_reg)
    assert email_field.get_attribute("value") == User.email
    
    password_field = registration_page.find_element(*Locators.password_registration)
    assert password_field.get_attribute("value") == User.email


