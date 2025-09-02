import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conftest import *
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Credantial
from selenium.webdriver.support import expected_conditions as EC

class TestEntrance:

    def test_entrance_on_the_main(self, main_page_start):

        main_page_start.find_element(*Locators.entrance_button).click()
        WebDriverWait(main_page_start, 10).until(
            EC.url_contains("/login")
        )
        main_page_start.find_element(*Locators.email_login).send_keys(Credantial.email)
        main_page_start.find_element(*Locators.password_login).send_keys(Credantial.password)
        main_page_start.find_element(*Locators.button).click()
        cabinet_element = WebDriverWait(main_page_start, 5).until(
            expected_conditions.visibility_of_element_located(Locators.make_order)
        )
        assert cabinet_element.is_displayed()

    def test_entrance_on_the_main_cabinet(self, main_page_start):

        main_page_start.find_element(*Locators.cabinet).click()
        WebDriverWait(main_page_start, 10).until(
            EC.url_contains("/login")
        )
        main_page_start.find_element(*Locators.email_login).send_keys(Credantial.email)
        main_page_start.find_element(*Locators.password_login).send_keys(Credantial.password)
        main_page_start.find_element(*Locators.button).click()
        cabinet_element = WebDriverWait(main_page_start, 5).until(
            expected_conditions.visibility_of_element_located(Locators.make_order)
        )
        assert cabinet_element.is_displayed()

    def test_entrance_on_registerbuttonclick(self, main_page_start):

        main_page_start.find_element(*Locators.cabinet).click()
        WebDriverWait(main_page_start, 10).until(
            EC.url_contains("/login")
        )
        main_page_start.find_element(*Locators.register_link).click()
        WebDriverWait(main_page_start, 10).until(
            EC.url_contains("/register")
        )
        main_page_start.find_element(*Locators.entrance_registration_page).click()
        WebDriverWait(main_page_start, 10).until(
            EC.url_contains("/login")
        )
        main_page_start.find_element(*Locators.email_login).send_keys(Credantial.email)
        main_page_start.find_element(*Locators.password_login).send_keys(Credantial.password)
        main_page_start.find_element(*Locators.button).click()
        cabinet_element = WebDriverWait(main_page_start, 5).until(
            expected_conditions.visibility_of_element_located(Locators.make_order)
        )
        assert cabinet_element.is_displayed()

    def test_entrance_on_new_password_button(self, main_page_start):

        main_page_start.find_element(*Locators.cabinet).click()
        WebDriverWait(main_page_start, 10).until(
            EC.url_contains("/login")
        )
        main_page_start.find_element(*Locators.new_password).click()
        WebDriverWait(main_page_start, 10).until(
            EC.url_contains("/forgot-password")
        )
        main_page_start.find_element(*Locators.entrance_registration_page).click()
        WebDriverWait(main_page_start, 10).until(
            EC.url_contains("/login")
        )
        main_page_start.find_element(*Locators.email_login).send_keys(Credantial.email)
        main_page_start.find_element(*Locators.password_login).send_keys(Credantial.password)
        main_page_start.find_element(*Locators.button).click()
        cabinet_element = WebDriverWait(main_page_start, 5).until(
            expected_conditions.visibility_of_element_located(Locators.make_order)
        )
        assert cabinet_element.is_displayed()

    def test_entrance_quit(self, main_page_start):

        main_page_start.find_element(*Locators.entrance_button).click()
        WebDriverWait(main_page_start, 10).until(
            EC.url_contains("/login")
        )
        main_page_start.find_element(*Locators.email_login).send_keys(Credantial.email)
        main_page_start.find_element(*Locators.password_login).send_keys(Credantial.password)
        main_page_start.find_element(*Locators.button).click()
        WebDriverWait(main_page_start, 5).until(
            expected_conditions.visibility_of_element_located(Locators.make_order)
        )
        main_page_start.find_element(*Locators.cabinet).click()
        WebDriverWait(main_page_start, 10).until(
            EC.url_contains("/account/profile")
        ) 
        main_page_start.find_element(*Locators.quit).click()
        login_element = WebDriverWait(main_page_start, 5).until(
            expected_conditions.visibility_of_element_located(Locators.button)
        )
        assert login_element.is_displayed()

    