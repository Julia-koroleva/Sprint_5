from selenium.webdriver.common.by import By
from locators import Locators
from geniration_em_pas import User
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from curl import *
from data import Credantial
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

def test_entrance_on_the_main_first(login_page):

    login_page.find_element(*Locators.email_login).send_keys(Credantial.email)
    login_page.find_element(*Locators.password_login).send_keys(Credantial.password)
    login_page.find_element(*Locators.button).click()
    cabinet_element = WebDriverWait(login_page, 5).until(
        expected_conditions.visibility_of_element_located(Locators.cabinet)
    )
    assert cabinet_element.is_displayed()
   
def test_entrance_on_the_main_second(main_page_start):

    main_page_start.find_element(*Locators.entrance_button).click()
    WebDriverWait(main_page_start, 10).until(
        EC.url_contains("/login")
    )
    main_page_start.find_element(*Locators.email_login).send_keys(Credantial.email)
    main_page_start.find_element(*Locators.password_login).send_keys(Credantial.password)
    main_page_start.find_element(*Locators.button).click()
    cabinet_element = WebDriverWait(main_page_start, 5).until(
        expected_conditions.visibility_of_element_located(Locators.cabinet)
    )
    assert cabinet_element.is_displayed()

def test_entrance_on_the_main_cabinet(main_page_start):

    main_page_start.find_element(*Locators.cabinet).click()
    WebDriverWait(main_page_start, 10).until(
        EC.url_contains("/login")
    )
    main_page_start.find_element(*Locators.email_login).send_keys(Credantial.email)
    main_page_start.find_element(*Locators.password_login).send_keys(Credantial.password)
    main_page_start.find_element(*Locators.button).click()
    cabinet_element = WebDriverWait(main_page_start, 5).until(
        expected_conditions.visibility_of_element_located(Locators.cabinet)
    )
    assert cabinet_element.is_displayed()

def test_entrance_on_registerbuttonclick(main_page_start):

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
        expected_conditions.visibility_of_element_located(Locators.cabinet)
    )
    assert cabinet_element.is_displayed()

def test_entrance_on_new_password_button(main_page_start):
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
        expected_conditions.visibility_of_element_located(Locators.cabinet)
    )
    assert cabinet_element.is_displayed()