from selenium.webdriver.common.by import By
from locators import Locators
from selenium import webdriver
from geniration_em_pas import User
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Credantial
from curl import *

class TestEntrance:
    def test_entrance_on_the_main(main_site):  # Добавлен self для методов класса
              
        # Кликаем на кнопку входа на главной странице
        main_site.find_element(*Locators.entrance_main_page).click()
        
        # Ждем появления формы входа
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.entrance_login_page)
        )
        
        # Вводим учетные данные
        driver.find_element(*Locators.email_login).send_keys(Credantial.email)
        driver.find_element(*Locators.password_login).send_keys(Credantial.password)
        
        # Проверяем введенные значения ДО нажатия кнопки
        email_field = driver.find_element(*Locators.email_login)
        assert email_field.get_attribute("value") == Credantial.email
    
        password_field = driver.find_element(*Locators.password_login)  # Исправлен локатор
        assert password_field.get_attribute("value") == Credantial.password
        
        # Нажимаем кнопку входа
        driver.find_element(*Locators.entrance_login_page).click()
        
        # Ждем перехода (например, в личный кабинет)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.cabinet)
        )
        
        # Дополнительная проверка успешного входа
        assert driver.current_url.endswith("/account")  # Или другая проверка