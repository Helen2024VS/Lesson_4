# Shop: отображение, скидка товара
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
book_android = driver.find_element_by_css_selector(".post-169 h3")
book_android.click()
old_price = driver.find_element_by_css_selector(".price>del>span")
old_price_text = old_price.text
assert old_price_text == "₹600.00"
new_price = driver.find_element_by_css_selector(".price>ins>span")
new_price_text = new_price.text
assert new_price_text == "₹450.00"
image = wait.until(
EC.visibility_of_element_located((By.CSS_SELECTOR, ".images>a>img")))
image.click()
image_book = wait.until(
EC.visibility_of_element_located((By.CLASS_NAME, "pp_content_container")))
close = wait.until(
EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
close.click()

driver.quit()