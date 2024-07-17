# Shop: покупка товара
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(25)
from selenium.webdriver.support.select import Select
wait = WebDriverWait(driver, 30)

driver.get("https://practice.automationtesting.in")

shop = driver.find_element_by_css_selector("#menu-item-40>a")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
book_html = driver.find_element_by_css_selector(".post-182>a:nth-child(2)")
book_html.click()
time.sleep(10)
cart = driver.find_element_by_class_name("wpmenucart-contents")
cart.click()
checkout = wait.until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button")))
checkout.click()
first_name = wait.until(
EC.visibility_of_element_located((By.ID, "billing_first_name")))
first_name.send_keys("Helen")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Ivanova")
email = driver.find_element_by_id("billing_email")
email.send_keys("helen_1@post.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("9999887771")
country = driver.find_element_by_class_name("select2-choice")
country.click()
input_country = driver.find_element_by_id("s2id_autogen1_search")
input_country.send_keys("alban")
input_country.click()
chosen_country = driver.find_element_by_id("select2-results-1")
chosen_country.click()
street = driver.find_element_by_id("billing_address_1")
street.send_keys("Lenina")
city = driver.find_element_by_id("billing_city")
city.send_keys("Mirage")
state = driver.find_element_by_id("billing_state")
state.send_keys("York")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("123456")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(10)
payment = driver.find_element_by_id("payment_method_cheque")
payment.click()
order = driver.find_element_by_id("place_order")
order.click()
order_status = wait.until(
EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-thankyou-order-received")))
order_status_text = order_status.text
assert order_status_text == "Thank you. Your order has been received."
payment_method = wait.until(
EC.visibility_of_element_located((By.CSS_SELECTOR, ".method>strong")))
payment_method_text = payment_method.text
assert payment_method_text == "Check Payments"

driver.quit()