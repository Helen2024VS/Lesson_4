# Login_registration: логин в систему
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
logout = WebDriverWait(driver,20).until
(EC.element_to_be_clickable((By.CSS_SELECTOR,".woocommerce-MyAccount-navigation li:nth-child(6)>a")))
if logout is not False:
    print("Элемент Logout есть на странице")
else:
    print("Элемент Logout куда-то делся!")
driver.quit()