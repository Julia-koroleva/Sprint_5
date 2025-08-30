from selenium.webdriver.common.by import By
from locators import Locators
from geniration_em_pas import User
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from curl import *
from data import Credantial
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


def test_souces_click(main_page_start):
    WebDriverWait(main_page_start, 10).until(
        EC.visibility_of_element_located(Locators.buns)
    )
    main_page_start.find_element(*Locators.sauces).click()
    WebDriverWait(main_page_start, 10).until(
        EC.text_to_be_present_in_element(Locators.active_tab, "Соусы")
    )
    assert 'Соусы' in main_page_start.find_element(*Locators.active_tab).text


def test_buns_click(main_page_start):
    WebDriverWait(main_page_start, 10).until(
        EC.visibility_of_element_located(Locators.buns)
    )
    main_page_start.find_element(*Locators.sauces).click()
    WebDriverWait(main_page_start, 10).until(
        EC.text_to_be_present_in_element(Locators.active_tab, "Соусы")
    )
    main_page_start.find_element(*Locators.buns).click()
    WebDriverWait(main_page_start, 10).until(
        EC.text_to_be_present_in_element(Locators.active_tab, "Булки")
    )
    assert 'Булки' in main_page_start.find_element(*Locators.active_tab).text

def test_fillings_click(main_page_start):
    WebDriverWait(main_page_start, 10).until(
        EC.visibility_of_element_located(Locators.buns)
    )
    main_page_start.find_element(*Locators.fillings).click()
    WebDriverWait(main_page_start, 10).until(
        EC.text_to_be_present_in_element(Locators.active_tab, "Начинки")
    )
    assert 'Начинки' in main_page_start.find_element(*Locators.active_tab).text