import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_first_registration():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first').send_keys('answer')
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second').send_keys('answer2')
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third').send_keys('answer3')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert 'Congratulations! You have successfully registered!' == welcome_text, 'expected text != actual text'


def test_second_registration():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first').send_keys('answer')
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second').send_keys('answer2')
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third').send_keys('answer3')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").txt
    assert welcome_text == 'Congratulations! You have successfully registered!', 'expected text != actual text'


if __name__ == '__main__':
    pytest.main()