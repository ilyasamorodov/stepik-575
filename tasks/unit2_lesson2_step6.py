from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_value = browser.find_element_by_id("input_value")
    # Считываем значение переменной. К int не приводим, т.к. это внутри calc
    x = input_value.text
    # Вычисляем значение функции от полученной переменной x
    result = calc(x)
    # Ищем элемент поля ввода
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(result)
    # Ищем чекбоксы и радио, кликаем по ним
    checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
