import time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://duckduckgo.com")
time.sleep(5)
browser.get("https://google.com")
time.sleep(2)
browser.save_screenshot('1.png')
time.sleep(3)
browser.refresh()
time.sleep(2)
browser.quit()
