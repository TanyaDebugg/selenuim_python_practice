from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
	browser = webdriver.Chrome()
	link = "http://SunInJuly.github.io/execute_script.html"
	browser.get(link)

	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
	x = x_element.text
	y = calc(x)

    # Ввести ответ в текстовое поле
	input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
	input1.send_keys(y)

    # Отметить checkbox "I'm the robot"
	option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    #scroll
	button = browser.find_element(By.TAG_NAME, "button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Выбрать radiobutton "Robots rule!"
	option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

	# Click on Submit
	button.click()

    #button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
	time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()
