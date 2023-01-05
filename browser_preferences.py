import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser_normal = webdriver.Firefox()
browser_normal.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent/')

options = webdriver.FirefoxOptions()
options.set_preference('dom.webdriver.enabled', False)  # to pretend we are not a robot
options.set_preference('dom.webnotifications.enabled', False)  # so that notifications don't block out scripts
options.set_preference('media.volume_scale', '0.0')  # disable sounds
options.set_preference('general.useragent.override', 'Garrett Master Thief')  # could be ANY user agent !

browser = webdriver.Firefox(options=options)
browser.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent/')  # website to check your user agent

time.sleep(5)
browser_normal.quit()
browser.quit()
