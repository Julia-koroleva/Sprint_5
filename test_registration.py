from locators import Locators
from geniration_em_pas import User
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_registration(registration_page):
    user = User.create_random_user()
    registration_page.find_element(*Locators.password).send_keys(user.password)  
    registration_page.find_element(*Locators.email).send_keys(user.email)  
    registration_page.find_element(*Locators.name).send_keys(user.name)  
    registration_page.find_element(*Locators.registration_button).click()  
    WebDriverWait(registration_page, 5).until(
        expected_conditions.visibility_of_element_located(Locators.entrance_registration_page)
    )
    email_field = registration_page.find_element(*Locators.email)
    assert email_field.get_attribute("value") == user.email
    password_field = registration_page.find_element(*Locators.password)
    assert password_field.get_attribute("value") == user.password  

def test_reg_mistake(registration_page):

    user = User.create_random_user()
    registration_page.find_element(*Locators.password).send_keys(user.mist_pass)  
    registration_page.find_element(*Locators.email).send_keys(user.email)  
    registration_page.find_element(*Locators.name).send_keys(user.name)  
    registration_page.find_element(*Locators.registration_button).click()  
    WebDriverWait(registration_page, 5).until(
        expected_conditions.visibility_of_element_located(Locators.mistake)
    )
    assert registration_page.current_url == "https://stellarburgers.nomoreparties.site/register"
    error_message = registration_page.find_element(*Locators.mistake).text
    assert "некорректный пароль" in error_message.lower()
    