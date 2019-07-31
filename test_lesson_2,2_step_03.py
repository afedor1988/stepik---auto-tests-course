# -*- coding: utf8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


#link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
number1 = browser.find_element(By.ID, "num1")
x = int(number1.text)
number2 = browser.find_element(By.ID, "num2")
y = int(number2.text)
sum = str(x + y)
#browser.find_element(By.ID, "dropdown").click()
#browser.find_element(By.TAG_NAME, "select").click()
#browser.find_element_by_css_selector("option:nth-child(2)").click()
#browser.find_element_by_css_selector("[value='1']").click()
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(sum)

# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
button.click()
