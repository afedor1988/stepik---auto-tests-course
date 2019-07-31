# -*- coding: utf8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys("Petrov")
input3 = browser.find_element(By.NAME, "email")
input3.send_keys("petrov@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_dir = os.path.abspath(os.path.join(current_dir, '..\\files')) # получаем путь к директории с файлом
file_path = os.path.join(file_dir, 'bio.txt')           # добавляем к этому пути имя файла 
send = browser.find_element(By.ID, "file")
send.send_keys(file_path)

# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
button.click()
