import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# PROXY FOR CHROME
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=5.134.216.58:8080')  # this will be used as a proxy

browser = webdriver.Chrome(options=options)
browser.get('https://google.com')
#time.sleep(5)
btn_search = browser.find_element(By.NAME, 'q')
btn_search.send_keys('What is my IP?')
btn_search.submit()
time.sleep(20)

# PROXY FOR FIREFOX
ip = '5.134.216.58'
port = 8080

options = webdriver.FirefoxOptions()
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.http', ip)
options.set_preference('network.proxy.http_port', port)
options.set_preference('network.proxy.https', ip)
options.set_preference('network.proxy.https_port', port)
options.set_preference('network.proxy.ssl', ip)
options.set_preference('network.proxy.ssl_port', port)

browser = webdriver.Firefox(options=options)
browser.get('https://google.com')
# time.sleep(5)
btn_search = browser.find_element(By.NAME, 'q')
btn_search.send_keys('What is my IP?')
btn_search.submit()
time.sleep(20)
browser.quit()
