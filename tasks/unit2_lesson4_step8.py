from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book_btn = browser.find_element_by_id("book")
    book_btn.click()

    # Ваш код, который заполняет обязательные поля
    input_value = browser.find_element_by_id("input_value")
    # Считываем значение переменной. К int не приводим, т.к. это внутри calc
    x = input_value.text
    # Вычисляем значение функции от полученной переменной x
    result = calc(x)
    # Ищем элемент поля ввода
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(result)

    button = browser.find_element_by_id("solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
