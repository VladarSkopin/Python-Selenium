import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://google.com/")

time.sleep(5)
# search_field = driver.find_element(By.NAME, 'q')
# search_field = driver.find_element(By.CSS_SELECTOR, '.gLFyf')
search_field = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_field.send_keys('iPhone 11')
search_field.submit()
