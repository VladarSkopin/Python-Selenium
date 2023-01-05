import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""options = webdriver.FirefoxOptions()
options.set_preference('dom.webdriver.enabled', False)  # to pretend we are not a robot
options.set_preference('dom.webnotifications.enabled', False)  # so that notifications don't block out scripts
options.set_preference('media.volume_scale', '0.0')  # disable sounds
"""
# browser = webdriver.Firefox(options=options)
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
