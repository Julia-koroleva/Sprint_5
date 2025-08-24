from selenium.webdriver.common.by import By

class Locators:

# Кнопка "Войти в эккаунт" на главной странице
    entrance_main_page = (By.XPATH, "//button[text()='Войти в аккаунт']")

# Кнопка "Личный кабинет" на главной странице
    cabinet = (By.XPATH,".//header//a[@href='/account']")

# Кнопка "Войти" на странице ввода логина и пароля
    login_page = (By.XPATH, "//button[contains(text()='Войти')]")

# Поле для ввода адреса электронной почты на странице ввода логина и пароля
    email_login = (By.XPATH, "//form[contains(@class, 'Account_profile__')]//input[@name='name']")

# Поле для ввода пароля на странице ввода логина и пароля
    password_login = (By.XPATH, "//form[contains(@class, 'Account_profile__')]//input[@name='Пароль']")

# Поле для ввода адреса электронной почты на странице регистрации
    email = (By.XPATH, ".//label[contains(text(), 'Email')]/following-sibling::input")

# Поле для ввода пароля на странице регистрации
    password = (By.XPATH, ".//input[@type='password']")

# Поле для ввода имени на странице регистрации
    name = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")

# Кнопка "Зарегистрироваться" 
    registration_button = (By.XPATH, ".//button[text()='Зарегистрироваться']")

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

# Ошибка ввода пароля при регистрации
    mistake = (By.XPATH, ".//p[text()='Некорректный пароль']")