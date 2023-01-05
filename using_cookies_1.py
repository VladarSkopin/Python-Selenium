import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle  # to save sessions

url_to_use = 'https://b4g-akk.ru/register'
browser = webdriver.Firefox()
browser.get(url_to_use)
time.sleep(100)  # time to register a user
pickle.dump(browser.get_cookies(), open('session', 'wb'))  # save all cookies to a file named "session"

