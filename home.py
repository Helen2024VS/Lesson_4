# Home: добавление комментария
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(25)

driver.get("https://practice.automationtesting.in")

driver.execute_script("window.scrollBy(0, 800);")
selenium_ruby = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 h3")
selenium_ruby.click()
reviews = driver.find_element_by_css_selector(".reviews_tab>a")
reviews.click()
rating = driver.find_element_by_css_selector(".stars .star-5")
rating.click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Helen_1")
email = driver.find_element_by_id("email")
email.send_keys("helen_1@post.com")
submit = driver.find_element_by_css_selector("#submit.submit")
submit.click()

driver.quit()