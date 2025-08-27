from selenium.webdriver.common.by import By
from locators import Locators
from geniration_em_pas import User
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from curl import *
from data import Credantial
from selenium import webdriver

def test_entrance_on_the_main(login_page):

    login_page.find_element(*Locators.email_login).send_keys(Credantial.email)
    login_page.find_element(*Locators.password_login).send_keys(Credantial.password)
    email_field = login_page.find_element(*Locators.email_login)
    assert email_field.get_attribute("value") == Credantial.email
    password_field = login_page.find_element(*Locators.password_login)
    assert password_field.get_attribute("value") == Credantial.password
    login_page.find_element(*Locators.button).click()
    cabinet_element = WebDriverWait(login_page, 5).until(
        expected_conditions.visibility_of_element_located(Locators.cabinet)
    )
    assert cabinet_element.is_displayed()
   





