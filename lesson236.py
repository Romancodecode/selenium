from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/redirect_accept.html"

import math



try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.TAG_NAME, 'button')
    button1.click()

    nw = browser.window_handles[1]
    browser.switch_to.window(nw)

    p = browser.find_element(By.ID, "input_value")
    p1 = p.text

    def calc(p1):
        return str(math.log(abs(12 * math.sin(int(p1)))))

    y = calc(p1)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button2 = browser.find_element(By.TAG_NAME, 'button')
    button2.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла