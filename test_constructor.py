from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
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