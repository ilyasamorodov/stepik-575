from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Ivan")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Petrov")
    email = browser.find_element_by_name("email")
    email.send_keys("i.petrov@ema.il")
    file = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_path)
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
