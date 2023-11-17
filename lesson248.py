from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

import math



try:
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))

    bt = browser.find_element(By.ID, "book")
    bt.click()

    p = browser.find_element(By.ID, 'input_value')
    p1 = p.text


    def calc(p1):
        return str(math.log(abs(12 * math.sin(int(p1)))))

    y = calc(p1)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button2 = browser.find_element(By.ID, 'solve')
    button2.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла