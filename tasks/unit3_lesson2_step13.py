from selenium import webdriver
import unittest
import time


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        user_firstname = browser.find_element_by_css_selector(".first_block input.first")
        user_firstname.send_keys("Пётр")
        user_lastname = browser.find_element_by_css_selector(".first_block input.second")
        user_lastname.send_keys("Иванов")
        user_email = browser.find_element_by_css_selector(".first_block input.third")
        user_email.send_keys("p.ivanov@ma.il")
        user_phone = browser.find_element_by_css_selector(".second_block input.first")
        user_phone.send_keys("+79001234567")
        user_address = browser.find_element_by_css_selector(".second_block input.second")
        user_address.send_keys("119019, Москва, Красная пл., 1")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        user_firstname = browser.find_element_by_css_selector(".first_block input.first")
        user_firstname.send_keys("Пётр")
        user_lastname = browser.find_element_by_css_selector(".first_block input.second")
        user_lastname.send_keys("Иванов")
        user_email = browser.find_element_by_css_selector(".first_block input.third")
        user_email.send_keys("p.ivanov@ma.il")
        user_phone = browser.find_element_by_css_selector(".second_block input.first")
        user_phone.send_keys("+79001234567")
        user_address = browser.find_element_by_css_selector(".second_block input.second")
        user_address.send_keys("119019, Москва, Красная пл., 1")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
