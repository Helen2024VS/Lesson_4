# Login_registration: регистрация аккаунта
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
email = driver.find_element_by_id("reg_email")
email.send_keys("helen_1@post.com")
password = driver.find_element_by_id("reg_password")
password.send_keys("My%PaSS#aCC")
register = driver.find_element_by_css_selector("p.form-row:nth-child(4)>input:nth-child(3)")
register.click()

driver.quit()