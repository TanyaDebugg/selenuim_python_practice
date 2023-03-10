from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = int(browser.find_element(By.ID, "num1").text)
    number2 = int(browser.find_element(By.ID, "num2").text)

    #def calc(x):
    #    return str(number1 + number2)
    #y = calc(treasure_check)
    
    result = number1 + number2

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))

    # Click on Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
