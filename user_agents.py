import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://mynickname.com/ru/generate')
time.sleep(5)
button_generate_nickname = browser.find_element(By.CSS_SELECTOR, '#generate')
text_field = browser.find_element(By.CSS_SELECTOR, '#nickname')
nicknames = []
button_generate_nickname.click()
time.sleep(3)
nicknames.append(text_field.get_attribute('value'))
button_generate_nickname.click()
time.sleep(3)
nicknames.append(text_field.get_attribute('value'))
button_generate_nickname.click()
time.sleep(3)
nicknames.append(text_field.get_attribute('value'))
time.sleep(5)
#browser.quit()

# print out the recorded nicknames
for n in nicknames:
    print(n)
print(f'Nicknames: {nicknames}')
