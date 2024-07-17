# Shop: количество товаров в категории
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(25)

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
html = driver.find_element_by_css_selector(".cat-item.cat-item-19>a")
html.click()
quantity_of_goods = driver.find_elements_by_css_selector(".products.masonry-done>li")
if len(quantity_of_goods) == 3:
    print("На вкладке HTML отображается 3 товара")
else:
    print("Ошибка!На вкладке HTML отображается: " + str(len(quantity_of_goods)))

driver.quit()