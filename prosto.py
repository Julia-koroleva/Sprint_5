from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Найти элемент и вывести все атрибуты
element = driver.find_element(By.ID)
print("Все атрибуты элемента:")
