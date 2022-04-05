from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = int(browser.find_element_by_id('num1').text)
    b = int(browser.find_element_by_id('num2').text)
    y = a+b


    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(str(y))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()