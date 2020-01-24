from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    time.sleep(1)

    # Ваш код, который заполняет обязательные поля
    input_value = browser.find_element_by_id("input_value")
    # Считываем значение переменной. К int не приводим, т.к. это внутри calc
    x = input_value.text
    # Вычисляем значение функции от полученной переменной x
    result = calc(x)
    # Ищем элемент поля ввода
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(result)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
