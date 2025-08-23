from selenium import webdriver
from selenium.webdriver.common.by import By

# Кнопка "Войти в эккаунт" на главной странице
entrance_main_page = (By.XPATH, ".//button[text()='Войти в аккаунт']")

# Кнопка "Личный кабинет" на главной странице
cabinet = (By.XPATH,".//header//a[@href='/account']")

# Кнопка "Войти" на странице ввода логина и пароля
entrance_login_page = (By.XPATH, ".//button[text()='Войти']")

# Поле для ввода адреса электронной почты на странице ввода логина и пароля
email_login = (By.XPATH, ".//form[contains(@class, 'Account_profile__')]//input[@name='name']")

# Поле для ввода пароля на странице ввода логина и пароля
password_login = (By.XPATH, ".//form[contains(@class, 'Account_profile__')]//input[@name='Пароль']")

# Поле для ввода адреса электронной почты на странице регистрации
email_registration = (By.XPATH, ".//form[contains(@action, 'register')]//input[@type='email']")

# Поле для ввода пароля на странице регистрации
password_registration = (By.XPATH, ".//form[contains(@action, 'register')]//input[@type='Пароль']")

# Поле для ввода имени на странице регистрации
name_registration = (By.XPATH, ".//form[contains(@action, 'register')]//input[@type='name']")

# Кнопка "Зарегистрироваться" 
registration = (By.XPATH, ".//button[text()='Зарегистрироваться']")

# Поле "Войти" с формы регистрации
entrance_registration_page = (By.XPATH, ".//a[@href='/login']")

# Поле "Восстановить пароль" из личного кабинета
new_password = (By.XPATH, ".//a[@href='/forgot-password']")

# Кнопка "Выход"
quit = (By.XPATH, ".//button[text()='Выход']")

# Кнопка "Конструктор"
constructor = (By.XPATH, ".//a[.//p[text()='Конструктор']]")

# Кнопка "Булки"
buns = (By.XPATH, ".//span[text()='Булки']")

# Кнопка "Соусы"
sauces = (By.XPATH, ".//span[text()='Соусы']")

# Кнопка "Начинки"
fillings = (By.XPATH, ".//span[text()='Начинки']")