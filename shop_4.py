# Shop: проверка цены в корзине
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(25)
from selenium.webdriver.support.select import Select
wait = WebDriverWait(driver, 20)

driver.get("https://practice.automationtesting.in")

shop = driver.find_element_by_css_selector("#menu-item-40>a")
shop.click()
book_html = driver.find_element_by_css_selector(".post-182>a:nth-child(2)")
book_html.click()
time.sleep(10)
cart_item = driver.find_element_by_class_name("cartcontents")
cart_item_text = cart_item.text
assert cart_item_text == "1 Item"
cart_price = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
cart_price_text = cart_price.text
assert cart_price_text == "₹180.00"
cart = driver.find_element_by_class_name("wpmenucart-contents")
cart.click()
price = wait.until(
EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount.amount")))
price_text = price.text
substr_price_text = price_text[1:]
if float(substr_price_text) != 0:
    print("В Subtotal отобразилась стоимость товара без налога")
else:
    print("Стоимость товара без налога не отображается")
price_tax = wait.until(
EC.visibility_of_element_located((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount.amount")))
price_tax_text = price_tax.text
substr_price_tax_text = price_tax_text[1:]
if float(substr_price_tax_text) != 0:
    print("В Total отобразилась полная стоимость товара (с налогом)")
else:
    print("Полная стоимость товара не отображается")

driver.quit()