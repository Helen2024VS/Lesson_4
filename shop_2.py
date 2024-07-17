# Shop: сортировка товаров
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(25)
from selenium.webdriver.support.select import Select

driver.get("https://practice.automationtesting.in")

my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
email = driver.find_element_by_id("username")
email.send_keys("helen_1@post.com")
password = driver.find_element_by_id("password")
password.send_keys("My%PaSS#aCC")
login = driver.find_element_by_css_selector("p.form-row:nth-child(3)>input:nth-child(3)")
login.click()
shop = driver.find_element_by_css_selector("#menu-item-40>a")
shop.click()
sorting_method = driver.find_element_by_class_name("orderby")
select_sorting = sorting_method.get_attribute("value")
if select_sorting == ("menu_order"):
    print("В селекторе выбран вариант сортировки по умолчанию")
else:
    print("В селекторе выбрана не сортировка по умолчанию")
sort_selection = Select(sorting_method)
sort_selection.select_by_value("price-desc")
sorting_method = driver.find_element_by_class_name("orderby")
select_sorting = sorting_method.get_attribute("value")
if select_sorting == ("price-desc"):
    print("В селекторе выбран вариант сортировки по цене от большей к меньшей")
else:
    print("В селекторе выбрана не та сортировка: не по цене от большей к меньшей")

driver.quit()