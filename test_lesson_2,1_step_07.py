# -*- coding: utf8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
digit = browser.find_element(By.ID, "treasure")
x = digit.get_attribute("valuex")
y = calc(x)
input = browser.find_element(By.ID, "answer")
input.send_keys(y)
checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()
radiobutton = browser.find_element(By.ID, "robotsRule")
radiobutton.click()

# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
button.click()
