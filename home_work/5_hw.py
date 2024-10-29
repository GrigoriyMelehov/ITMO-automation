from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#поиск элементов
def poisk_elementov():
    text_pole = driver.find_element(By.CSS_SELECTOR, '#user-name')
    if text_pole is None:
        print('элемент "поле Username" не найден')
    else:
        print('элемент "поле Username" найден!УРА!')
    text_pole = driver.find_element(By.CSS_SELECTOR, '#password')
    if text_pole is None:
        print('элемент "поле Password" не найден')
    else:
        print('элемент "поле Password" найден!УРА!')
    text_pole = driver.find_element(By.CSS_SELECTOR, '#login-button') #кнопка называется "Login"
    if text_pole is None:
        print('элемент "кнопка Submit" не найден')
    else:
        print('элемент "кнопка Submit" найден!УРА!')

poisk_elementov()