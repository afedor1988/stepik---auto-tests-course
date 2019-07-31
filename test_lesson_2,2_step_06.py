# -*- coding: utf8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
digit = browser.find_element(By.ID, "input_value")
x = digit.text
y = calc(x)

# Отправляем заполненную форму
# По умолчанию в качестве аргумента, передаваемого в функцию scrollIntoView используется true - указывает на то, что элемент нужно скролить к верхней границе окна.
# Если передавать false - то элемент будет скролиться к нижней границе окна. Для очевидности мы здесь все-таки явно указываем, что аргумент равен truе.

# Эта команда проскроллит страницу на 100 пикселей вниз:
# browser.execute_script("window.scrollBy(0, 100);")

input = browser.find_element(By.ID, "answer")
input.send_keys(y)



checkbox = browser.find_element(By.ID, "robotCheckbox")
#browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
#browser.execute_script("return arguments[0].scrollIntoView(false);", checkbox)
checkbox.click()


radiobutton = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
#browser.execute_script("return arguments[0].scrollIntoView(false);", radiobutton)
radiobutton.click()


button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#browser.execute_script("return arguments[0].scrollIntoView(false);", button)
button.click()


