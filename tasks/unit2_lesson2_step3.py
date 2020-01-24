from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")

    total = int(num1.text) + int(num2.text)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(total))

    submit = browser.find_element_by_tag_name("button")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
