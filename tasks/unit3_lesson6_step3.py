import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
#@pytest.mark.parametrize('lesson', ["236895"])
def test_guest_should_see_login_link(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    textarea = browser.find_element_by_css_selector("textarea.textarea")
    answer = str(math.log(int(time.time())))
    textarea.send_keys(answer)
    submit = browser.find_element_by_css_selector("button.submit-submission")
    submit.click()
    result = browser.find_element_by_css_selector(".smart-hints__hint")
    assert "Correct!" in result.text, "Incorrect"
