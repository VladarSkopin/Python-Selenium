import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://youtube.com')
time.sleep(5)
button = browser.find_element('xpath', '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')
print(button.text)
print(button.get_attribute('class'))
button.click()
time.sleep(10)


# browser.quit()
