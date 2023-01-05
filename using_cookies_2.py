import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle  # to save sessions

url_to_use = 'https://b4g-akk.ru/register'
browser = webdriver.Firefox()
browser.get(url_to_use)
time.sleep(5)

for cookie in pickle.load(open('session', 'rb')):
    browser.add_cookie(cookie)
    print(cookie)

print('Cookies are loaded')
browser.refresh()
time.sleep(10)
browser.quit()
