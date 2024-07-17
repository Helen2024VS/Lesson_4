# Shop: отображение страницы товара
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
book_html = driver.find_element_by_css_selector(".post-181 h3")
book_html.click()
book_name = WebDriverWait(driver,20).until
(EC.text_to_be_present_in_element_value(".product_title.entry-title", "HTML5 Forms"))
if book_name is not False:
    print("Книга называется 'HTML5 Forms'")
else:
    print("Это не та книга!")

driver.quit()