# Shop: работа в корзине
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
driver.execute_script("window.scrollBy(0, 300);")
book_html = driver.find_element_by_css_selector(".post-182>a:nth-child(2)")
book_html.click()
time.sleep(10)
book_java = driver.find_element_by_css_selector(".post-180>a:nth-child(2)")
book_java.click()
cart = driver.find_element_by_class_name("wpmenucart-contents")
cart.click()
time.sleep(10)
remove_1 = driver.find_element_by_css_selector(".cart_item [data-product_id='182']")
remove_1.click()
undo_1 = driver.find_element_by_link_text("Undo?")
undo_1.click()
quantity_1 = driver.find_element_by_css_selector(".cart_item:nth-child(1) input")
quantity_1.clear()
quantity_1.send_keys(3)
update = driver.find_element_by_css_selector(".button:nth-child(2)")
update.click()
quantity = driver.find_element_by_css_selector(".cart_item:nth-child(1) input")
quantity_check = quantity.get_attribute("value")
assert quantity_check == "3"
time.sleep(10)
apply = driver.find_element_by_css_selector(".coupon>.button")
apply.click()
coupon = driver.find_element_by_css_selector("ul.woocommerce-error>li")
coupon_text = coupon.text
assert coupon_text == "Please enter a coupon code."

driver.quit()